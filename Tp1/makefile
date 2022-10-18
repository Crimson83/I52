main : main.o echangiste.o complexe.o
	g++ $^ -Wall -lm -o main

echangiste.o : echangiste.h echangiste.cc complexe.h
	g++ -c echangiste.cc

complexe.o : complexe.h complexe.cc
	g++ -c complexe.cc

main.o : main.cc echangiste.h
	g++ -c main.cc
