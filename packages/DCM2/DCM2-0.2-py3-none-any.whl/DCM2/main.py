# original Emir Chacra july 2023
# modified Axel Osses sept 2023
import numpy as np
from graphviz import Digraph
import scipy.sparse as sparse
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
class Init_DCM:
    def __init__(self, nodes, forcers = None, bias = None,
                 saturation = lambda x: min(max(0.0,x),1)):
        #Inicializa la matriz de pesos e información de los nodos
        self._n_nodes = len(nodes)
        self.W = sparse.lil_matrix((self._n_nodes, self._n_nodes))
        self._init_W = sparse.lil_matrix((self._n_nodes, self._n_nodes))

        #Inicialización del grafo
#        self.graph = Digraph(engine='sfdp',strict=True)
#        self.graph = Digraph(engine='sfdp',strict=True)
        self.graph = Digraph(strict=True)

        #Diccionario que almacena el índice asociado a cada nodo.
        nodes_id = {}
        nodes_names = {}
        for k in range(self._n_nodes):
          nodes_id[nodes[k][0]] = k
          nodes_names[nodes[k][0]] = nodes[k][1]
        self.nodes_id = nodes_id
        self._nodes_names = nodes_names
        for node in np.array(nodes)[:,0]:
          self.graph.node(self._nodes_names[node],style='filled', color='lightgrey')

        # modificado Axel:
        if forcers == None:
            no_forcers=1
            forcers = [['None','None']]
        else:
           no_forcers=0
        
        #Inicializa la influencia de los forzantes
        self._n_forcers = len(forcers)
        self.fW = sparse.lil_matrix((self._n_nodes, self._n_forcers))
        self._init_fW = sparse.lil_matrix((self._n_nodes, self._n_forcers))
        self.forcers_state = np.array([0.0 for j in range(self._n_forcers)])

        #Diccionario que almacena el índice asociado a cada forzante.
        forcers_id = {}
        forcers_names = {}
        for k in range(self._n_forcers):
          forcers_id[forcers[k][0]] = k
          forcers_names[forcers[k][0]] = forcers[k][1]
        self.forcers_id = forcers_id
        self._forcers_names = forcers_names
        if no_forcers==0:
            for forcer in np.array(forcers)[:,0]:
              self.graph.node(self._forcers_names[forcer], shape = 'box',style='filled', color='lightgrey')
        
        #Variables que guardan tanto el estado inicial como el actual de los nodos.
        self.__init_state = None
        self._state = None

        #Variable para guardar el escenario simulado
        self.scene = None
        self.f_scene = None

        #Variable para guardar el tiempo
        self.iteration = 0

        #Bias
        if bias == None:
          self.bias = np.array([0.0 for j in range(self._n_nodes)])
        else: self.bias = bias

        #Función de saturación
        self.saturation = saturation
        
        #Variable que guarda las interacciones no lineales
        self.nonlinear = []
        self.nonlinear_count = 0

    def show_graph(self, outputs = None, title = None,save = None, engine = None):
        if outputs == None: pass
        else:
          for node in outputs:
            self.graph.node(self._nodes_names[node], shape = 'octagon')

        if title == None: pass
        else: self.graph.attr(label=title, labelloc = 't')

        if save != None: 
            if engine == None: self.graph.render(save, format='pdf')
            else: self.graph.render(save, format='pdf', engine= engine) 
        
        #self.graph.view()
        
        return self.graph

    def reset(self): #Reinicializa el estado de la red al estado inicial
        self._state = self.__init_state
        self.scene = None       
        self.fW = self._init_fW.copy()
        self.f_scene = None
        self.iteration = 0

    def set_init_state(self, state): #Fija el estado inicial
        self.__init_state = state

    def set_forcer_state(self, forcer, state, error = 0.0): #Fija el estado del forzante
        self.forcers_state[self.forcers_id[forcer]] = (1 + error * np.random.normal()) * state

    def set_nodes_weight(self, source, target, weight): #Fija pesos entre nodos
        if self.nodes_id.get(source) == None or self.nodes_id.get(target) == None:
          raise ValueError('Una de las variables no pertenece al sistema')
        # modificado Axel (comentado):
        #elif source == target:
        #  raise ValueError('No se admiten valores en la diagonal, usar memoria')
        else:
          self.W[self.nodes_id[target], self.nodes_id[source]] = weight
          self._init_W[self.nodes_id[target], self.nodes_id[source]] = weight
          self.graph.edge(self._nodes_names[source], self._nodes_names[target], label = str(weight))

    def set_forcers_weight(self, source, target, weight): #Fija pesos inciales forzante -> nodo
        if self.forcers_id.get(source) == None or self.nodes_id.get(target) == None:
          raise ValueError('Una de las variables no pertenece al sistema')
        else:
          self.fW[self.nodes_id[target], self.forcers_id[source]] = weight
          self._init_fW[self.nodes_id[target], self.forcers_id[source]] = weight
          self.graph.edge(self._forcers_names[source], self._nodes_names[target], label = str(weight))

    def get_time(self): #Returns the value of the iteration. Useful for interactions depending on time.
        return self.iteration
    
    def set_nonlinear(self, *args): #Fija interaciones no lineales
        self.nonlinear.append(list(args)) 
        self.nonlinear_count = self.nonlinear_count+1
        inter_node = 'NL'+str(self.nonlinear_count)
        self.graph.node(inter_node,shape='point')
        
        if self.nodes_id.get(args[len(args)-2]) == None:
            raise ValueError('El último label de la relación no lineal debe ser un nodo')
        else:
            target = args[len(args)-2]
        self.graph.edge(inter_node,self._nodes_names[target],label = inter_node)
        for j in range(len(args)-2):
            source = args[j]
            if self.nodes_id.get(args[j]) == None:
                self.graph.edge(self._forcers_names[source], inter_node, arrowhead='none')
            else:
                self.graph.edge(self._nodes_names[source], inter_node, arrowhead='none')
        
class DCM(Init_DCM):

    def scene_sim(self, init_state, forcer_f = None, nonlinear = None, transf = None, nosaturation = None,
                  error = None, N_iter = None, memory_state=None, alpha=None, beta1=None, beta2=None, dt=None):
        #Función que simula escenarios.

        if forcer_f == None: #Inicializa forzantes si no se entregan.
          forcer_f = [lambda x: 0.0*x for k in range(self._n_forcers)]
        if error == None: #Inicializa error de forzantes si no se entregan.
          error = [0.0 for k in range(self._n_forcers)]
        
        if memory_state != None and dt != None:
            beta1 = np.array([dt for j in range(len(memory_state))])

        X = np.empty((N_iter+1, self._n_nodes))
        F = np.empty((N_iter+1, self._n_forcers))
        X[0] = init_state
        F[0] = np.array([forcer_f[self.forcers_id[forcer]](0.0) for forcer in list(self.forcers_id.keys())])

        self.set_init_state(init_state)
        self.reset()

        for k in range(1,N_iter+1):
            self.iteration = k

            for forcer in list(self.forcers_id.keys()):
              self.set_forcer_state(forcer, forcer_f[self.forcers_id[forcer]](k), error[self.forcers_id[forcer]])

            if transf != None :
              for j in range(len(transf)):
                self.transform(transf[j], k, F)

            self.iter(X, n_iter = k, memory_state= memory_state, nosaturation = nosaturation, 
                      alpha = alpha, beta1=beta1, beta2=beta2, nonlinear = nonlinear)
            X[k] = self._state
            F[k] = self.forcers_state

        self.scene = X
        self.f_scene = F
        
    # modificado Axel:
    def iter(self, X, n_iter = None, memory_state = None, nosaturation = None,
             alpha = None, beta1 = None, beta2 = None, nonlinear = None, print_state = False):
        # Función que realiza una iteración de la red.
        k = n_iter
        # Evolución de la parte lineal de la dinámica
        new_state = self.W @ (self._state) + self.fW @ self.forcers_state + self.bias

        # Agrega no-linealidades originales en la definicion del DCM
        if len(self.nonlinear)>0 : #si hay no-linealidades agrega estas dinámicas
            for j in range(len(self.nonlinear)):
              new_state = self.nonlinearity2(new_state, self.nonlinear[j])
        
        # Agrega no-linealidades como argumentos
        if nonlinear != None : #si hay no-linealidades agrega estas dinámicas
            for j in range(len(nonlinear)):
              new_state = self.nonlinearity2(new_state, nonlinear[j])
                
        # Agrega memoria
        if memory_state != None: #si hay memoria agrega estas dinámicas
            memory_nodes = [self.nodes_id[state] for state in memory_state]
            # si no se definen los valores de memoria se dejan por default en alpha=0
            if alpha == None:
              alpha = np.array([0.0 for j in range(len(memory_nodes))])  
            for a_j in range(len(alpha)):
                if np.isclose(alpha[a_j],1.0):
                  Omega_k = 1
                else:
                  Omega_k = (1-alpha[a_j]**k)/(1-alpha[a_j])
                # si no se dan los valores de los pesos beta se dejan por default en beta=1
                # sino se asignan a los valores proporcionados
                if np.all(beta1 == None) :
                    beta1f = 1.0
                else:
                    beta1f = beta1[a_j]
                if np.all(beta2 == None) :
                    beta2f = 1.0
                else:
                    beta2f = beta2[a_j]
                # Se acumulan todos los términos de memoria
                m_j = memory_nodes[a_j]
                summed_memory = np.sum([alpha[a_j]**(k-1 - i) * X[i,m_j] for i in range(k - 1)])
                new_state[m_j] = beta1f*new_state[m_j] + beta2f*(X[k-1,m_j] + summed_memory)/Omega_k
                        
        # Se aplica saturación al nuevo estado total, incluyendo memoria o no linealidades si existen
        if nosaturation==None: 
            self._state = np.array([self.saturation(state) for state in new_state])
        else:
            self._state = new_state

        if print_state:
          print(f'Estado actual: {self._state}')

    # modificado Axel:
    def nonlinearity(self, new_state, weight):
        target = self.nodes_id[weight[1]]
        func = weight[2]

        if self.nodes_id.get(weight[0]) == None:
          source = self.forcers_id[weight[0]]
          new_state[target] = new_state[target] + func(self.forcers_state[source])
#          new_state[target] = func(self.forcers_state[source])
        else:
          source = self.nodes_id[weight[0]]
          new_state[target] = new_state[target] + func(self._state[source])
#          new_state[target] = func(self._state[source])
        return new_state

    # modificado Axel:
    def nonlinearity2(self, new_state, weight):
        ### 
        nargs = len(weight)
        if nargs<2 :
            raise ValueError('No hay suficientes argumentos en la definición de la no linealidad')
        nl_state = weight[0:nargs-2]
        if self.nodes_id.get(weight[nargs-2]) == None:
            print(weight[nargs-2])
            raise ValueError('La última etiqueta de la parte no lineal no puede ser un forzante')
        else:
            target = self.nodes_id[weight[nargs-2]]
        func = weight[nargs-1]
        state_value = np.array([0.0 for j in range(len(nl_state))])  

        for s_j in range(len(nl_state)):
            if self.nodes_id.get(weight[s_j]) == None:
              source = self.forcers_id[weight[s_j]]
              state_value[s_j] = self.forcers_state[source]
            else:
              source = self.nodes_id[weight[s_j]]            
              state_value[s_j] = self._state[source]
        
        new_state[target] = new_state[target] + func(state_value)
        return new_state      
            
    def transform(self, weight, n_iter, F):
        if self.nodes_id.get(weight[0]) == None:
          source = self.forcers_id[weight[0]]
        else:
          source = self.nodes_id[weight[0]]

        target = self.nodes_id[weight[1]]

        m_sign = weight[2]

        k = n_iter
        alpha = 5e-4
        Omega_k = (1-alpha**k)/(1-alpha)
        summed_memory = F[k-1,source] + np.sum([alpha*(k-1 - i) * F[i,source] for i in range(k - 1)])

        if self.nodes_id.get(weight[0]) == None:
          self.fW[target, source] = np.tanh( np.arctanh(self._init_fW[target,source]) \
                                  + m_sign * summed_memory/Omega_k)
        else:
          self.W[target, source] = np.tanh( np.arctanh(self._init_W[target,source]) \
                                 + m_sign * summed_memory/Omega_k)

# Modificado Axel
    def plots(self, nodes, forcers, N_iter=None, title=None, xlabel=None, ylabel=None,
              full_name = False, fig = None, rows = 1, cols = 1, ax_num = 1, linewidth = 2, markersize = 4,
             begin = None, end = None):
        # Función que inicializa el gráfico de los nodos seleccionados.
        # Como la función entrega la axis pueden agregarse cosas (Ver ejemplo).

        if N_iter==None:
            N_iter=np.size(self.scene,0)
        if begin==None:
            begin = 0
        if end==None:
            end = N_iter
        ax = fig.add_subplot(rows,cols,ax_num)

        ax.set_title(title, size = 25)
        ax.set_xlabel(xlabel, size = 25)
        ax.set_ylabel(ylabel, size = 25)
        ax.tick_params(axis='both', which='major', labelsize=25)
        
        ax.set_ylim(-0.1,1.1)

#        xticks = np.arange(0, N_iter +1, 20)
#        xticks = np.arange(begin, end, 20)
#        xmajorLocator = tick.FixedLocator(locs=xticks)
#        plt.gca().xaxis.set_major_locator( xmajorLocator )

        rr = np.arange(begin,end,1)
        if full_name:

          if nodes == None: pass
          else:              
            for node in nodes:
              ax.plot(rr, self.scene[rr, self.nodes_id[node] ], '-o',
                        label = self._nodes_names[node], markersize = markersize, linewidth = linewidth)
              
          if forcers == None: pass
          else:
            for forcer in forcers:
              ax.plot(rr, self.f_scene[rr, self.forcers_id[forcer] ], '-',
                        label = self._forcers_names[forcer] + ' (Forcer)', markersize = markersize, linewidth = linewidth)
              
        else:

          if nodes == None: pass
          else:
            for node in nodes:
              ax.plot(rr, self.scene[rr, self.nodes_id[node] ], '-o',
                        label = node, markersize = markersize, linewidth = linewidth)
              
          if forcers == None: pass
          else:
            for forcer in forcers:
              ax.plot(rr, self.f_scene[rr, self.forcers_id[forcer] ], '-',
                        label = forcer + ' (Forcer)', markersize = markersize, linewidth = linewidth)
        
        return ax