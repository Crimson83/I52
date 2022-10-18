#include "professeur.h"
#include <iostream>
#include <string>
using namespace std;
professeur::professeur(string n,string p,string s,int a):personne(n,p,a){
  status=s;
  heures=0;
}
void professeur::affic(){
 personne::affic();
 cout<<"Status :"<<status<<" "<<"Heures :"<<heures<<endl;
}
void professeur::travailler(int n){
  heures=heures+n;
}
