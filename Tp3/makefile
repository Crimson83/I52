main : main.o polynome.o vecteurcomplexe.o complexe.o
	g++ $^ -Wall -o $@

main.o : main.cc polynome.h vecteurcomplexe.h complexe.h
	g++ -c main.cc

vecteurcomplexe.o : vecteurcomplexe.cc vecteurcomplexe.h complexe.h
	g++ -c vecteurcomplexe.cc

polynome.o : polynome.cc polynome.h
	g++ -c polynome.cc

test : test.o complexe.o
	g++ $^ -Wall -o $@

complexe.o : complexe.cc complexe.h
	g++ -c complexe.cc

test.o : test.cc complexe.h
	g++ -c test.cc
