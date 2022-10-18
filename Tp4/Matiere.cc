#include "Matiere.h"
#include <string>
using namespace std;

Matiere::Matiere(){
  nom="";
  coef=0;
}

Matiere::Matiere(string n,int c){
  nom=n;
  coef=n;
}

void Matiere::affic(){
  cout<<"nom : "<<nom<<" "<<"Coefficient : "<<coef<<endl;
}
