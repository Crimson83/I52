#include "echangiste.h"
#include "complexe.h"
#include <iostream>
using namespace std;
int main(){
  int x=10,y=15;
  Complexe a,b;
  Init(a);
  Init(b);
  static Complexe c;
  Init(c);
  static Complexe& cref=c;
  //cout<<"adresse du Complexe C : "<<&c<<"\n"<<"Adresse du champ Réel : "<<&c.re<<"\n"<<"Adresse du Champ Imaginaire : "<<&c.im<<endl;
  //cout<<"adresse du Complexe reférence à C : "<<&cref<<"\n"<<"Adresse du champ Réel : "<<&cref.re<<"\n"<<"Adresse du Champ Imaginaire : "<<&cref.im<<endl;
  static Complexe d=Bidon(c);
  static Complexe& dref=d;
  //cout<<"adresse du Complexe Bidon : "<<&d<<"\n"<<"Adresse du champ Réel : "<<&d.re<<"\n"<<"Adresse du Champ Imaginaire : "<<&d.im<<endl;
  //cout<<"adresse du Complexe reférence à Bidon : "<<&dref<<"\n"<<"Adresse du champ Réel : "<<&dref.re<<"\n"<<"Adresse du Champ Imaginaire : "<<&dref.im<<endl;
  //a.re=8.9;
  //a.im=4.6;
  //b.re=7.6;
  //b.im=6.4;
  //Complexe* pc;
  //ptComplexe pc2;
  //Complexe* pc3=CreerComplexe();
  //Permuter(x,y);

  //Permuter(a,b);
  //AfficherComplexe(a);
  //AfficherComplexe(b);
  //AfficherComplexe(Somme(a,b));
  //AfficherComplexe(Produit(a,b));
  //cout<<Module(a)<<endl;
  //AfficherComplexe(Conjuge(a));
  //CreerComplexe(&pc);
  //AfficherComplexe(*pc);
  //CreerComplexe(pc2);
  //AfficherComplexe(*pc2);
  //AfficherComplexe(*pc3);
  Complexe* tc=CreerVecteurComplexes(5);
  for(int i=0;i<5;i++){
    AfficherComplexe(tc[i]);
    cout<<&tc[i]<<endl;
  }
}
