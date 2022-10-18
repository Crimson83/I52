#include "vecteurcomplexe.h"
#include "complexe.h"
#include <fstream>
#include <iostream>

using namespace std;

vecteurcomplexe::vecteurcomplexe(){
  nb=0;
  vec=NULL;
}

vecteurcomplexe::vecteurcomplexe(complexe* l,int a){
  nb=a;
  vec=new complexe[a];
  for(int i=0;i<nb;i++){
    vec[i]=l[i];
  }
}

vecteurcomplexe::vecteurcomplexe(const vecteurcomplexe& a){
  nb=a.nb;
  vec=new complexe[nb];
  for(int i=0;i<nb;i++){
        vec[i]=a.vec[i];
    }
}

vecteurcomplexe::vecteurcomplexe(const complexe* l, unsigned short t){
  nb=t;
  vec=new complexe[nb];
  for(int i=0;i<nb;i++){
      vec[i]=l[i];
  }
}

vecteurcomplexe::vecteurcomplexe(ifstream& f){
  f>>nb;
  float a,b;
  vec=new complexe[nb];
  for(int i=0;i<nb;i++){
    f>>a;
    f>>b;
    vec[i]=complexe(a,b);
  }
}

vecteurcomplexe::~vecteurcomplexe(){
  delete [] vec;
}

void vecteurcomplexe::afficherveccomplexe(){
    for(int i=0;i<nb;i++){
      vec[i].AfficherComplexe();
    }
}
ostream& operator<<(ostream &o,const vecteurcomplexe &v){
  o<<"[";
  for(int i=0;i<v.nb-1;i++){
    o<<v.vec[i]<<",";
  }
  o<<v.vec[v.nb-1]<<"]"<<endl;
  return o;
}

vecteurcomplexe& vecteurcomplexe::operator=(const vecteurcomplexe& T){
  if(this!=&T){
    delete vec;
    vec=new complexe[nb];
    vec=T.vec;
    for(int i=0;i<nb;i++){
      vec[i]=T.vec[i];
    }
  }
  return *this;
}

complexe& vecteurcomplexe::operator[](int i){
  return vec[i];
}
