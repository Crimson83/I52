main: main.o personne.o professeur.o Etudiant1.o
	g++ $^ -Wall -o $@

main.o: main.cc personne.h professeur.h
	g++ -Wall -c $<

Matiere.o: Matiere.cc Matiere.h
	g++ -Wall -c $<
	
Etudiant2.o: Etudiant2.cc Etudiant2.h Etudiant1.h
	g++ -Wall -c $<

Etudiant1.o: Etudiant1.cc Etudiant1.h personne.h
	g++ -Wall -c $<

personne.o: personne.cc personne.h
	g++ -Wall -c $<

professeur.o: professeur.cc professeur.h personne.h
	g++ -Wall -c $<
