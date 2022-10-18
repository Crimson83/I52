#include "Etudiant2.h"
#include "Etudiant1.h"
#include <string>

Etudiant2::Etudiant2(string n,string p,int a,int nb,Matiere* tab)Etudiant(n,p,a,nb){
  mat=new Matiere[nb];
  for(int i=0;i<nb;i++){
    mat[i]=tab[i];
  }
}

Etudiant2::Etudiant2(const Etudiant2& e):Etudiant1(e){
  nb=e.nb;
  mat=new Matiere[nb];
  for(int i=0;i<n;i++){
    mat[i]=e.mat[i];
  }
}

Etudiant2::~Etudiant2(){
  delete [] mat;
}
void Etudiant2::affic(){
  Etudiant1::affic()
  for(int i=0;i<nb;i++){
    cout<<mat[i].getnom<<" : "<<notes[i]<<endl;
  }
}
float Etudiant2::Moyenne(){
  float temp=0;
  int cpt=0;
  for(int i=0;i<nb;i++){
    temp=temp+(mat[i].getcoef()*notes[i]);
    cpt=cpt+mat[i].getcoef();
  }
  return temp/cpt;
}
