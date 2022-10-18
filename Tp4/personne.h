#ifndef PERSONNE_
#define PERSONNE_
#include <string>
using namespace std;
class personne{
  private :
    string nom;
    string prenom;
    int age;
  public :
    personne(string,string,int);
    void affic();
    void vieillir();
    string getnom(){return nom;}
    string getprenom(){return prenom;}
};
#endif
