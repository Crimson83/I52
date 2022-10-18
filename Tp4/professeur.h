#ifndef PROFESSEUR_
#define PROFESSEUR_
#include "personne.h"
#include <string>
using namespace std;
class professeur : public personne{
  private :
    string status;
    int heures;
  public :
    professeur(string,string,string,int);
    void affic();
    void travailler(int);
};
#endif
