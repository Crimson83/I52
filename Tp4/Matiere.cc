#include "Matiere.h"
#include <string>
#include <iostream>
using namespace std;

Matiere::Matiere(){
  nom="";
  coef=0;
}

Matiere::Matiere(string n,int c){
  nom=n;
  coef=c;
}

void Matiere::affic(){
  cout<<"nom : "<<nom<<" "<<"Coefficient : "<<coef<<endl;
}
