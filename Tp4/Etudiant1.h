#ifndef ETUDIANT1_
#define ETUDIANT1_
#include "personne.h"
#include <string>
using namespace std;

class Etudiant1: public personne{
  protected :
    int nb;
    float* notes;
  public :
    Etudiant1(string,string,int,int);
    Etudiant1(const Etudiant1&);
    ~Etudiant1();
    void AjouterNotes(float*);
    void affic();
    float Moyenne();
    Etudiant1& operator=(const Etudiant1&);
};
#endif
