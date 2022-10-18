#ifndef MATIERE_
#define MATIERE_
#include <string>
using namespace std;

class Matiere{
  private:
    string nom;
    int coef;
  public:
    Matiere();
    Matiere(string,int);
    void affic();
    string getnom(){return nom;}
    int getcoef(){return coef;}
};
#endif
