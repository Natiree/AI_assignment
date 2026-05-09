parent(james, nathaniel).
parent(james, maryanne).
parent(james, jamelick).

parent(josephine, nathaniel).
parent(josephine, maryanne).
parent(josephine, jamelick).

parent(hannah, james).
parent(loyce, josephine).

parent(jamelick, anna).
parent(jamelick, mwangi).


sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.


grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).


cousin(X, Y) :-
    parent(A, X),
    parent(B, Y),
    sibling(A, B).


uncle_aunt(X, Y) :-
    sibling(X, Z),
    parent(Z, Y).
