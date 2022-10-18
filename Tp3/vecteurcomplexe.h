#ifndef VECTEURCOMPLEXE_
#define VECTEURCOMPLEXE_
#include "complexe.h"
#include <iostream>
#include <fstream>
using namespace std;

class vecteurcomplexe{
  private :
    complexe* vec;
    int nb;
  public :
    vecteurcomplexe();
    vecteurcomplexe(complexe*,int);
    vecteurcomplexe(const vecteurcomplexe&);
    vecteurcomplexe(const complexe*,unsigned short);
    vecteurcomplexe(ifstream&);
    ~vecteurcomplexe();
    void afficherveccomplexe();
    friend ostream& operator<<(ostream&,const vecteurcomplexe&);
    vecteurcomplexe& operator=(const vecteurcomplexe&);
    complexe& operator[](int);
};
#endif
