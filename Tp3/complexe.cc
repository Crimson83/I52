#include <iostream>
#include "complexe.h"

using namespace std;

complexe::complexe(){
  //cout<<this<<endl;
  re=0;
  im=0;
  //cout<<"Constructeur par défaut"<<endl;
}
complexe::complexe(float a, float b){
  //cout<<this<<endl;
  re=a;
  im=b;
  //cout<<"Constructeur par paramètre"<<endl;
}
 complexe::complexe(const complexe &c){
   //cout<<this<<endl;
   re=c.re;
   im=c.im;
   //cout<<"Constructeur par copie"<<endl;
}

complexe::~complexe(){
  //cout<<this<<endl;
  //cerr<<"Destructeur"<<endl;
}

void complexe::AfficherComplexe(){
  cout<<re<<"\t"<<im<<"\t"<<endl;
}

complexe complexe::operator+(const complexe& c){
  complexe t;
  t.re=re+c.re;
  t.im=im+c.im;
  return t;
}
complexe complexe::operator-(const complexe& c){
  complexe t;
  t.re=re-c.re;
  t.im=im-c.im;
  return t;
}

complexe complexe::operator*(const complexe& c){
  complexe t;
  t.re=(re*c.re-im*c.im);
  t.im=(im*c.re+re*c.im);
  return t;
}

complexe complexe::operator*(float i){
  complexe t;
  t.re=re*i;
  t.im=im*i;
  return t;
}

complexe operator*(float i,const complexe& c){
  complexe t;
  t.re=c.re*i;
  t.im=c.im*i;
  return t;
}

complexe complexe::operator/(const complexe& c){
  complexe t(((re*c.re+im*c.im)/(c.re*c.re+c.im*c.im)),((im*c.re-re*c.im)/(c.re*c.re+c.im*c.im)));
  return t;
}
ostream& operator<<(ostream &o,const complexe &c){
  o<<"("<<c.re<<"\t"<<c.im<<")"<<"\t";
  return o;
}
