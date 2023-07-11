
class Node:

    def __init__(self, state, h, path_cost=0, parent=None):
        self.state = state
        self.h = h
        self.path_cost = path_cost
        self.parent = parent

    def to_solution(self):
        seq = []
        node = self
        s0 = None
        while node is not None:
            if node.parent is None:
                s0 = node.state
            if node.parent is not None:
                seq.append(node.state)
            node = node.parent
        assert s0 is not None
        return list(reversed(seq))
    
    def __repr__(self):
        s = f'Node(state={self.state}, path_cost={self.path_cost}'
        s += ')' if self.parent is None else f', parent={self.parent.state})'
        return s


def a_star(
    initial_state,
    goal_test,
    successor_fn,
    heuristic_fn
):
    """Implementare l'algoritmo di ricerca A*.

    Parametri:
    - initial_state: posizione (x, y) della cella di partenza
    - goal_test: funzione da usare come goal_test(s), che ritorna
      True se e solo se s è uno stato di goal
    - successor_fn: funzione da usare come successor_fn(s), che ritorna
      una lista di tuple (s1, c) dove s1 è un successore di s, mentre
      c è il costo della transizione da s ad s1
    - heuristic_fn: funzione da usare come heuristic_fn(s), che ritorna
      un valore numerico.
    
    Questa funzione deve ritornare l'ultimo nodo della soluzione (un
    oggetto di tipo Node).
    """

    #indico con frontiera la lista dei nodi candidati da esplorare
    frontiera = [Node(initial_state, heuristic_fn(initial_state))]#all'inizio la frontiera contiene solo il nodo iniziale
    #nodo iniziale non ha padre, quindi il suo costo del percorso è 0 

    lista_esplorati = set()

    while frontiera:#finchè la frontiera non è vuota
        nodo = min(frontiera, key=lambda x: x.h + x.path_cost)#scelgo il nodo con il valore f più basso

        
        if goal_test(nodo.state):#se il nodo scelto è quello finale vuol dire che ho trovato la soluzione
            return nodo
        #in caso non avessi trovato la soluzione, genero i successori del nodo scelto e li aggiungo alla frontiera
        for (successore,costo) in successor_fn(nodo.state):
            if successore in lista_esplorati:
                continue
            new_cost = nodo.path_cost + costo #il costo del percorso è dato dal costo del percorso del nodo padre + 1
           
            new_h = heuristic_fn(successore) #il valore h è dato dalla funzione euristica che calcola la distanza di Manhattan
            #aggiungo a front
            a = Node(successore, new_h, new_cost, nodo)
            frontiera.append(a)
        #aggiungo il nodo corrente alla lista dei nodi esplorati e lo rimuovo dalla frontiera
        lista_esplorati.add(nodo.state)
        frontiera.remove(nodo)

    # Se la frontiera è vuota e non ho trovato la soluzione, ritorno None
    return None
   
#SCELTA EURISTICA
# Se i movimenti possibili in una griglia sono solo verticali e orizzontali e non obliqui, la distanza di Manhattan è una scelta ottima, questo perchè
# calcola la distanza tra due punti considerando solo gli spostamenti orizzontali e verticali necessari per raggiungere la
# destinazione. Questo è perfettamente adatto al nostro caso, poichè ci troviamo in un gridWorld privo di movimenti obliqui
# Un'altra scelta potrebbe essere la distanza euclidea che calcola la distanza geometrica tra due punti nello spazio. 
# Sebbene la distanza euclidea possa essere utilizzata anche per problemi su una griglia con movimenti limitati a orizzontale e verticale,
# potrebbe sovrastimare la distanza effettiva poiché tiene conto anche degli spostamenti obliqui che non sono consentiti nelle regole del nostro problema. 
# Di conseguenza, potrebbe portare ad una ricerca meno efficiente.

def heuristic(s, goal, is_solid):
    """Implementare l'euristica da utilizzare per l'esercizio 1.

    Parametri:
    - s: stato sul quale va calcolato il valore di h(s)
    - goal: posizione (x, y) della cella di goal
    - is_solid: funzione da usare come is_solid(p), che ritorna True
      se e solo se la cella in posizione p = (x_p, y_p) è piena
    
      Questa funzione deve ritornare un valore numerico.
    """
    return abs(s[0] - goal[0]) + abs(s[1] - goal[1]) 

