#include <iostream>
#include "oeuvre.h"
using namespace std;
Oeuvre::Oeuvre(){
  titre="";
  artiste="";
  annee=0;
  art="";
}

Oeuvre::Oeuvre(string t,string a,int ann,string ar){
  titre=t;
  artiste=a;
  annee=ann;
  art=ar;
}

Oeuvre::Oeuvre(const Oeuvre& o){
  titre=o.titre;
  artiste=o.artiste;
  annee=o.annee;
  art=o.art;
}

string Oeuvre::get_titre()const{
  return titre;
}
string Oeuvre::get_artiste()const{
  return artiste;
}

int Oeuvre::get_annee()const{
  return annee;
}

string Oeuvre::get_art()const{
  return art;
}

void Oeuvre::cartel()const{
  cout<<titre<<" "<<artiste<<" "<<annee<<" "<<art<<" ";
}
