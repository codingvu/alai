nar(aakash).
nar(agastya).
nar(rohit).
nar(vansh).
nar(vidit).
nar(aryan).

maheela(priyanka).
maheela(sonam).
maheela(vaishnavi).
maheela(rohini).
maheela(shalini).
maheela(kiran).

jeevanasaathee(aakash, priyanka).
jeevanasaathee(vidit, sonam).
jeevanasaathee(vansh, rohini).
jeevanasaathee(rohit, vaishnavi).

maata_pita(aakash, sonam).
maata_pita(aakash, vansh).
maata_pita(priyanka, sonam).
maata_pita(priyanka, vansh).
% --
maata_pita(vansh, shalini).
maata_pita(vansh, aryan).
maata_pita(rohini, shalini).
maata_pita(rohini, aryan).
% --
maata_pita(vidit, rohit).
maata_pita(vidit, kiran).
maata_pita(sonam, rohit).
maata_pita(sonam, kiran).
% --
maata_pita(rohit, agastya).
maata_pita(vaishnavi, agastya).

pati(X, Y) :- nar(X), jeevanasaathee(X, Y).
patnee(X, Y) :- maheela(X), jeevanasaathee(Y, X).

pita(X, Y) :- nar(X), maata_pita(X, Y).
maata(X, Y) :- maheela(X), maata_pita(X, Y).

beta(X, Y) :- nar(X), maata_pita(Y, X).
beti(X, Y) :- maheela(X), maata_pita(Y, X).

daada(X, Y) :- nar(X), maata_pita(X, Koee_Vyakti), nar(Koee_Vyakti), maata_pita(Koee_Vyakti, Y).
daadi(X, Y) :- maheela(X), maata_pita(X, Koee_Vyakti), nar(Koee_Vyakti), maata_pita(Koee_Vyakti, Y).

naana(X, Y) :- nar(X), maata_pita(X, Koee_Vyakti), maheela(Koee_Vyakti), maata_pita(Koee_Vyakti, Y).
naani(X, Y) :- maheela(X), maata_pita(X, Koee_Vyakti), maheela(Koee_Vyakti), maata_pita(Koee_Vyakti, Y).

bhai(X, Y) :- nar(X), maata_pita(Koee_Vyakti, X), maata_pita(Koee_Vyakti, Y), \==(X, Y).
bahan(X, Y) :- maheela(X), maata_pita(Koee_Vyakti, X), maata_pita(Koee_Vyakti, Y), \==(X, Y).

bhatija(X, Y) :- nar(X), bhai(Koee_Vyakti, Y), pita(Koee_Vyakti, X).
bhatiji(X, Y) :- maheela(X), bhai(Koee_Vyakti, Y), pita(Koee_Vyakti, X).

bhanja(X, Y) :- nar(X), bahan(Koee_Vyakti, Y), maata(Koee_Vyakti, X).
bhanji(X, Y) :- maheela(X), bahan(Koee_Vyakti, Y), maata(Koee_Vyakti, X).

sala(X, Y) :- nar(X), bahan(Koee_Vyakti, X), pati(Y, Koee_Vyakti).
sali(X, Y) :- maheela(X), bahan(Koee_Vyakti, X), pati(Y, Koee_Vyakti).

jamai(X, Y) :- nar(X), pati(X, Koee_Vyakti), maata_pita(Y, Koee_Vyakti).
bahu(X, Y) :- maheela(X), patnee(X, Koee_Vyakti), maata_pita(Y, Koee_Vyakti).

:- write("Pati"), nl.
:- forall(pati(X, Y), (write(X), write(" is "), write(Y), write("'s pati"), nl)).
:- nl.

:- write("Maata"), nl.
:- forall(maata(X, Y), (write(X), write(" is "), write(Y), write("'s maata"), nl)).
:- nl.

:- write("Beta"), nl.
:- forall(beta(X, Y), (write(X), write(" is "), write(Y), write("'s beta"), nl)).
:- nl.

:- write("Daadi"), nl.
:- forall(daadi(X, Y), (write(X), write(" is "), write(Y), write("'s daadi"), nl)).
:- nl.

:- write("Naani"), nl.
:- forall(naani(X, Y), (write(X), write(" is "), write(Y), write("'s naani"), nl)).
:- nl.

:- write("Bhai"), nl.
:- forall(bhai(X, Y), (write(X), write(" is "), write(Y), write("'s bhai"), nl)).
:- nl.

:- write("Bhatiji"), nl.
:- forall(bhatiji(X, Y), (write(X), write(" is "), write(Y), write("'s bhatiji"), nl)).
:- nl.

:- write("Bhanja"), nl.
:- forall(bhanja(X, Y), (write(X), write(" is "), write(Y), write("'s bhanja"), nl)).
:- nl.

:- write("Sali"), nl.
:- forall(sali(X, Y), (write(X), write(" is "), write(Y), write("'s sali"), nl)).
:- nl.

:- write("Jamai"), nl.
:- forall(jamai(X, Y), (write(X), write(" is "), write(Y), write("'s jamai"), nl)).
:- nl.

:- halt.
