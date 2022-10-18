main : main.o libsum
	g++ $^ -Wall -o $@
main.o : main.cc complexe.h
	g++ -c main.cc
complexe.o : complexe.cc complexe.h
	g++ -c complexe.cc
libsum.a : complexe.o
		ar cr $@ complexe.o
		ranlib libsum.a
