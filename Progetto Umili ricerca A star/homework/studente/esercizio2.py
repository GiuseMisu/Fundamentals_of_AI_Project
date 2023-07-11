import math

def successors(s, is_solid, region_width, region_height):
    """Implementare le funzioni di successione e costo.

    Parametri:
    - s: stato del quale vanno calcolati i successori e i costi delle
      relative transizioni
    - is_solid: funzione da usare come is_solid(p) che ritorna True
      se e solo se la cella in posizione p è piena
    - region_width: numero di colonne della griglia
    - region_height: numero di righe della griglia

    Questa funzione deve ritornare una lista di tuple (s1, c), dove s1
    è un successore di s, mentre c è il costo della transizione da s
    ad s1.
    """
    lista_successori = []
    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        x, y = s[0] + dx, s[1] + dy
        if x < 0 or x >= region_width or y < 0 or y >= region_height:
            continue
        # calcolo il costo della transizione
        if is_solid((x, y)):
            costo_transizione = 10000
        else:
          costo_transizione = 1 #perche prendiamo la distanza di manhattan e se lo spostamento è di 1 allora il costo è 1
        lista_successori.append(((x, y), costo_transizione)) # aggiungo alla lista anche il costo della transizione
    return lista_successori
   
   
#SCELTA EURISTICA
# Se i movimenti possibili in una griglia sono solo verticali e orizzontali e non obliqui, la distanza di Manhattan è una scelta ottima, questo perchè
# calcola la distanza tra due punti considerando solo gli spostamenti orizzontali e verticali necessari per raggiungere la
# destinazione. Questo è perfettamente adatto al nostro caso, poichè ci troviamo in un gridWorld privo di movimenti obliqui
# Un'altra scelta potrebbe essere la distanza euclidea che calcola la distanza geometrica tra due punti nello spazio. 
# Sebbene la distanza euclidea possa essere utilizzata anche per problemi su una griglia con movimenti limitati a orizzontale e verticale,
# potrebbe sovrastimare la distanza effettiva poiché tiene conto anche degli spostamenti obliqui che non sono consentiti nelle regole del nostro problema. 
# Di conseguenza, potrebbe portare ad una ricerca meno efficiente.
def heuristic(s, goal, is_solid, region_width, region_height):
    """Implementare l'euristica da utilizzare per l'esercizio 2.

    Parametri:
    - s: stato sul quale va calcolato il valore di h(s)
    - goal: posizione (x, y) della cella di goal
    - is_solid: funzione da usare come is_solid(p), che ritorna True
      se e solo se la cella in posizione p = (x_p, y_p) è piena
    - region_width: numero di colonne della griglia
    - region_height: numero di righe della griglia

      Questa funzione deve ritornare un valore numerico.
    """
    return abs(s[0] - goal[0]) + abs(s[1] - goal[1]) 
    
