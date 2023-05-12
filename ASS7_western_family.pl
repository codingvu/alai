male(aakash).
male(agastya).
male(rohit).
male(vansh).
male(vidit).

female(priyanka).
female(sonam).
female(vaishnavi).
female(rohini).
female(shalini).

spouse(aakash, priyanka).
spouse(vidit, sonam).
spouse(vansh, rohini).
spouse(rohit, vaishnavi).

parent(aakash, sonam).
parent(aakash, vansh).
parent(priyanka, sonam).
parent(priyanka, vansh).
% --
parent(vansh, shalini).
parent(rohini, shalini).
% --
parent(vidit, rohit).
parent(sonam, rohit).
% --
parent(rohit, agastya).
parent(vaishnavi, agastya).


husband(X, Y) :- male(X), spouse(X, Y).
wife(X, Y) :- female(X), spouse(Y, X).
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
son(X, Y) :- male(X), parent(Y, X).
daughter(X, Y) :- female(X), parent(Y, X).
grandfather(X, Y) :- male(X), parent(X, Somebody), parent(Somebody, Y).
grandmother(X, Y) :- female(X), parent(X, Somebody), parent(Somebody, Y).
brother(X, Y) :- male(X), parent(Somebody, X), parent(Somebody, Y), \==(X, Y).
sister(X, Y) :- female(X), parent(Somebody, X), parent(Somebody, Y), \==(X, Y).

:- write("Husband"), nl.
:- forall(husband(X, Y), (write(X), write(" is "), write(Y), write("'s husband"), nl)).
:- nl.

:- write("Wife"), nl.
:- forall(wife(X, Y), (write(X), write(" is "), write(Y), write("'s wife"), nl)).
:- nl.

:- write("Father"), nl.
:- forall(father(X, Y), (write(X), write(" is "), write(Y), write("'s father"), nl)).
:- nl.

:- write("Mother"), nl.
:- forall(mother(X, Y), (write(X), write(" is "), write(Y), write("'s mother"), nl)).
:- nl.

:- write("Son"), nl.
:- forall(son(X, Y), (write(X), write(" is "), write(Y), write("'s son"), nl)).
:- nl.

:- write("Daughter"), nl.
:- forall(daughter(X, Y), (write(X), write(" is "), write(Y), write("'s daughter"), nl)).
:- nl.

:- write("Grandfather"), nl.
:- forall(grandfather(X, Y), (write(X), write(" is "), write(Y), write("'s grandfather"), nl)).
:- nl.

:- write("Grandmother"), nl.
:- forall(grandmother(X, Y), (write(X), write(" is "), write(Y), write("'s grandmother"), nl)).
:- nl.

:- write("Brother"), nl.
:- forall(brother(X, Y), (write(X), write(" is "), write(Y), write("'s brother"), nl)).
:- nl.

:- write("Sister"), nl.
:- forall(sister(X, Y), (write(X), write(" is "), write(Y), write("'s sister"), nl)).
:- nl.

:- halt.
