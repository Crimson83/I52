#include "Etudiant1.h"
#include "personne.h"
#include <string>
#include <iostream>
using namespace std;

Etudiant1::Etudiant1(string n,string p,int a,int nbr):personne(n,p,a){
  nb=nbr;
  notes=new float[nb];
}
Etudiant1::Etudiant1(const Etudiant1& e):personne(e){
  nb=e.nb;
  notes=new float[nb];
  for(int i=0;i<nb;i++){
    notes[i]=e.notes[i];
  }
}

Etudiant1::~Etudiant1(){
  delete [] notes;
}

void Etudiant1::AjouterNotes(float *tab){
  for(int i=0;i<nb;i++){
    notes[i]=tab[i];
  }
}

void Etudiant1::affic(){
  cout<<"M/Mme "<<getnom()<<" "<<getprenom()<<" "<<"Notes :";
  for(int i=0;i<nb;i++){
    cout<<" "<<notes[i];
  }
  cout<<endl;
}
float Etudiant1::Moyenne(){
  float tmp;
  for(int i=0;i<nb;i++){
    tmp=tmp+notes[i];
  }
  return tmp/nb;
}
Etudiant1& Etudiant1::operator=(const Etudiant1& e){
  if(this!=&e){
    this->personne::operator=(e);
    nb=e.nb;
    delete [] notes;
    notes=new float[nb];
    for(int i=0;i<nb;i++){
      notes[i]=e.notes[i];
    }
  }
  return *this;
}
