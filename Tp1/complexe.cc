#include <iostream>
#include <cmath>
#include "complexe.h"
using namespace std;

void AfficherComplexe(const Complexe &a){
  cout<<a.re<<"\t"<<a.im<<"\t"<<a.ident<<endl;
}
Complexe Somme(const Complexe &a, const Complexe &b){
  Complexe t;
  Init(t);
  t.re=a.re+b.re;
  t.im=a.im+b.im;
  return t;
}
Complexe Produit(const Complexe &a, const Complexe &b){
  Complexe t;
  Init(t);
  t.re=(a.re*b.re-a.im*b.im);
  t.im=(a.im*b.re+a.re*b.im);
  return t;
}
float Module(const Complexe &t){
  float x=t.re*t.re+t.im*t.im;
  return sqrt(x);
}
Complexe Conjuge(const Complexe &t){
  Complexe temp;
  Init(temp);
  temp.re=t.re;
  temp.im=-1*t.im;
  return temp;
}
void Init(Complexe &a){
  static int i=0;
  a.ident=i++;
  a.re=0;
  a.im=0;
}
Complexe Bidon(Complexe &b){
  Complexe Bidonade=b;
  return Bidonade;
}
void CreerComplexe(Complexe** pc){
  *pc=new Complexe;
  Init(**pc);
}
void CreerComplexe(ptComplexe &pc2){
  pc2=new Complexe;
  Init(*pc2);
}
Complexe* CreerComplexe(){
  Complexe* pc3=new Complexe;
  Init(*pc3);
  return pc3;
}
Complexe* CreerVecteurComplexes(unsigned int a){
  Complexe* tc=new Complexe[a];
  for(int i=0;i<a;i++){
    Init(tc[i]);
  }
  return tc;
}
