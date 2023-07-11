% ESERCIZIO 1,a

fibonacci(1, 0). % La prima regola stabilisce che il primo numero di Fibonacci è 0.
fibonacci(2, 1). % La seconda regola stabilisce che il secondo numero di Fibonacci è 1
fibonacci(N, F) :- % La terza regola viene utilizzata per calcolare l N-esimo numero di Fibonacci quando N è maggiore di 2.
    N > 2, % essendoci già regole definite per 2 e 1 se il valore è superiore a due non entra 
    N_1 is N - 1,
    N_2 is N - 2,
    fibonacci(N_1, F_1),
    fibonacci(N_2, F_2),
    F is F_1 + F_2. 


% ESERCIZIO 1,b

prime(2).
prime(3).
prime(N) :-
    integer(N), % Verifico che N sia un numero intero positivo
    N > 3, 
    N mod 2 =\= 0, % Verifico che N non sia divisibile per 2
    \+ check_divisibile(N, 3). % controllo che N non sia divisibile per nessun numero dispari tra 3 e la radice quadrata di N.

check_divisibile(N, Divisor) :-    
    Divisor * Divisor < N, % Verifico che Divisor sia minore della radice quadrata di N.
    Divisor_2 is Divisor + 2, % Incremento Divisor di 2. 
    
    check_divisibile(N, Divisor_2). % Richiamo ricorsivamente divisible_by con il nuovo valore di Divisor.

check_divisibile(N, Divisor) :-  
    N mod Divisor =:= 0. % Verifico che N sia divisibile per Divisor. Se lo è, allora N non è primo.


% ESERCIZIO 2,a

cdot([], [], 0). % caso base della ricorsione è che il prodotto scalare di due liste vuote è 0.
cdot([T_1|C_1], [T_2|C_2], X) :- 
    cdot(C_1, C_2, X_1),    
    X is T_1 * T_2 + X_1. 

% uso la ricorsione per calcolare il prodotto scalare di due liste di interi.
% La regola ricorsiva calcola il prodotto scalare tra code delle due liste e aggiunge il prodotto tra loro teste.


% Esercizio 2,b

% calcola somma degli elementi della lista
somma_lista([], 0).
somma_lista([X|X_2], somma) :-
    somma_lista(X_2, RestSum),
    somma is X + RestSum.

% Funzionalità principale vede se lista è ripida o meno
steep(L) :- 
    steep(L, 0). 

steep([], _).      
steep([X|X_2], PrevSum) :-      
    X >= PrevSum,   
    Somma_2 is X + PrevSum, 
    steep(X_2, Somma_2). 


% Esercizio 2,c

seg([], []).    % caso base della ricorsione è che lista vuota ha un unico segmento, che è la lista vuota stessa.
seg(S, [_|Coda]) :-     % La prima regola ricorsiva scarta il primo elemento della lista e richiama ricorsivamente seg sulla coda della lista. 
    seg(S, Coda).
seg([Testa|C_1], [Testa|C_2]) :-
    seg(C_1, C_2).


% La seconda regola ricorsiva verifica se la testa di S corrisponde alla testa della lista, 
% e se sì, richiama ricorsivamente seg sui restanti elementi di S e sulla coda della lista.


% Esercizio 2,d

isort(X, [], [X]).  % caso base se la lista di partenza L è vuota, allora la lista ordinata L1 sarà la lista con solo X dentro.
isort(X, [Testa|Coda], [X,Testa|Coda]) :-
    X =< Testa.     % inserimento di X all inizio della lista se X è minore o uguale alla testa di L.
isort(X, [Testa|Coda], [Testa|Coda_2]) :-
    X > Testa,
    isort(X, Coda, Coda_2).


% Esercizio 3
% knowledge base per es 3

arc(a,b).
arc(a,c).
arc(b,d).
arc(b,e).
arc(c,b).
arc(e,c).


dfv(R, N) :-
    dfv(R, [], N).

dfv(Nodo, Visited, N_2) :-
    member(Nodo, Visited), 
    arc(Nodo, Next),
    dfv(Next, Visited, N_2).

    
dfv(Nodo, Visited, Nodo) :-
    \+ member(Nodo, Visited).  % Verifico che Nodo non sia già stato visitato. attraverso predicato member.

dfv(Nodo, Visited, N_2) :-
    \+ member(Nodo, Visited),   % Verifico che Nodo non sia già stato visitato
    arc(Nodo, Next),
    dfv(Next, [Nodo | Visited], N_2).



