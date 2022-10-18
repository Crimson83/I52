#include "polynome.h"
#include <iostream>

using namespace std;

polynome::polynome(){
  deg=0;
  coef=NULL;
}

polynome::polynome(int a,float *b){
  deg=a;
  coef=new float[deg+1];
  for(int i=0;i<deg+1;i++){
    coef[i]=b[i];
  }
}

polynome::polynome(const polynome& a){
  deg=a.deg;
  coef=new float[deg+1];
  for(int i=0;i<deg+1;i++){
    coef[i]=a.coef[i];
  }
}

polynome::~polynome(){
  delete [] coef;
}

polynome& polynome::operator=(const polynome& a){
  if(this!=&a){
    this->deg=a.deg;
    this->coef=new float[this->deg];
    for(int i=0;i<deg+1;i++){
      this->coef[i]=a.coef[i];
    }
  }
  return *this;
}

void polynome::Affic(){
  for(int i=0;i<deg;i++){
    cout<<coef[i]<<" ";
  }
  cout<<endl;
}
