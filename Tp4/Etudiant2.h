#ifndef ETUDIANT2_
#define ETUDIANT2_
#include "Etudiant1.h"
#include "Matiere.h"
#include <string>
using namespace std;

class Etudiant2 : public Etudiant1{
  private :
    Matiere* mat;
  public:
    Etudiant2(string,string,int,int,Matiere*);
    Etudiant2(const Etudiant2&);
    ~Etudiant2();
    void affic();
    float Moyenne();
    Etudiant2& operator=(const Etudiant2&);
};
#endif
