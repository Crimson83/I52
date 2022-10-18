#include "personne.h"
#include <iostream>
#include <string>

using namespace std;

personne::personne(string n,string p,int a){
  nom=n;
  prenom=p;
  age=a;
}

void personne::affic(){
  cout<<"M/Mme "<<nom<<" "<<prenom<<" "<<"Age: "<<age<<" ";
}

void personne::vieillir(){
  age++;
}
