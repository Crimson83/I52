#ifndef ETUDIANT2_
#define ETUDIANT2_
#include "Etudiant1.h"
#include <string>
using namespace std;
class Etudiant2 : public Etudiant1{
  private :
    Matiere* Vec;
  public:
    Etudiant2(string,string,int,int,Matiere*);
    Etudiant2(const Etudiant2&);
    ~Etudiant2();
    void affic();
    float Moyenne();
    Etudiant2& operator=(const Etudiant2&);
}
