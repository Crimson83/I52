#include "tableau.h"
#include "oeuvre.h"
#include <iostream>
using namespace std;
Tableau::Tableau():Oeuvre(){
  hauteur=0;
  largeur=0;
  technique="";
  expose=false;
}

Tableau::Tableau(string t, string a, int ann, float h, float l,string tec, bool ex):Oeuvre(t,a,ann,"Peinture"){
  hauteur=h;
  largeur=l;
  technique=tec;
  expose=ex;
}

Tableau::Tableau(const Tableau& t):Oeuvre(t){
  hauteur=t.hauteur;
  largeur=t.largeur;
  technique=t.technique;
}

void Tableau::cartel()const{
  Oeuvre::cartel();
  cout<<hauteur<<" "<<largeur<<" "<<technique<<" "<<((expose)?"Exposé":"Non Exposé")<<endl;
}

ostream& operator<<(ostream &o,const Tableau &t){
  o<<t.get_titre()<<" "<<t.get_artiste()<<" "<<t.get_annee()<<" "<<((t.expose)?"Exposé":"Non Exposé")<<endl;
  return o;
}

bool Tableau::operator>(const Tableau& t){
  return((hauteur*largeur)>(t.hauteur*t.largeur));
}
