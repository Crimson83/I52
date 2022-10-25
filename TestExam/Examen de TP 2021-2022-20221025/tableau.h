#ifndef _TABLEAU_H
#define _TABLEAU_H
#include "oeuvre.h"
#include <iostream>
using namespace std;

class Tableau : public Oeuvre{
private :
	float hauteur;
	float largeur;
	string technique;
	bool expose;
public:
	//constructeurs
	Tableau();
	Tableau(string, string, int, float, float,string, bool);
	Tableau(const Tableau &);
	//surcharge de la methode  cartel pour la classe Tableau
	void cartel()const;
	//surcharge de l'opérateur <<
	friend ostream& operator<<(ostream&,const Tableau&);
	//Surcharge de >
	bool operator>(const Tableau&);

};
#endif
