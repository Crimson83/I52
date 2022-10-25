main : main.o  tableau.o oeuvre.o exposition.o
	g++ $^ -Wall -o $@
main.o : main.cc tableau.h oeuvre.h exposition.h
	g++ -Wall -c $<
exposition.o : exposition.cc exposition.h tableau.h oeuvre.h
	g++ -Wall -c $<
tableau.o : tableau.cc tableau.h oeuvre.h
	g++ -Wall -c $<
oeuvre.o : oeuvre.cc oeuvre.h
	g++ -Wall -c $<
