#include "exposition.h"
#include "tableau.h"
#include <iostream>
using namespace std;

Exposition::Exposition(){
  nb=0;
  salle=NULL;
}

Exposition::Exposition(Tableau* t,int n){
  nb=n;
  salle=new Tableau[nb];
  for(int i;i<nb;i++){
    salle[i]=t[i];
  }
}

Exposition::Exposition(int n){
  nb=n;
  salle=new Tableau[nb];
  for(int i=0;i<nb;i++){
    salle[i]=Tableau();
  }
}

Exposition::Exposition(const Exposition& e){
  nb=e.nb;
  salle=new Tableau[nb];
  for(int i=0;i<nb;i++){
    salle[i]=e.salle[i];
  }
}

Exposition::~Exposition(){
  delete [] salle;
}

Exposition& Exposition::operator=(const Exposition& e){
  if(this!=&e){
    delete [] salle;
    nb=e.nb;
    salle=new Tableau[nb];
    for(int i=0;i<nb;i++){
      salle[i]=e.salle[i];
    }
  }
  return *this;
}
Exposition Exposition::operator+(const Tableau& e)const{
  Exposition Exp(nb+1);
  for(int i=0;i<nb;i++){
    Exp[i]=salle[i];
  }
  Exp[nb]=e;
  return Exp;
}

Tableau& Exposition::operator[](int i){
  return salle[i];
}

Tableau Exposition::GrandFormat()const{
  Tableau res(salle[0]);
  for(int i=1;i<nb;i++){
    if(salle[i]>res){
      res=salle[i];
    }
  }
  return res;
}
