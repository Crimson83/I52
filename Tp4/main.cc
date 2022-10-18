#include "personne.h"
#include "Matiere.h"
#include "professeur.h"
#include "Etudiant1.h"
#include "Etudiant2.h"
#include <string>
#include <iostream>
using namespace std;
int main(){
//string nom1="Gray";
//string prenom1="Dorian";
//personne Humain1(nom1,prenom1,30);
//Humain1.vieillir();
//Humain1.affic();
//cout<<endl;
//string nom2="Rogue";
//string prenom2="Severus";
//string status1="Titulaire";
//professeur Humain2(nom2,prenom2,status1,50);
//Humain2.travailler(200);
//Humain2.affic();
string nom3="Potter";
string prenom3="Harry";
//Etudiant1 Humain3(nom3,prenom3,15,4);
//float tab[]={12,9,15,14};
//Humain3.AjouterNotes(tab);
//Humain3.affic();
//cout<<Humain3.Moyenne()<<endl;
Matiere Mat1("Magie",3),Mat2("Potion",2),Mat3("Divination",4),Mat4("Info",1);
Matiere tab[]={Mat1,Mat2,Mat3,Mat4};
Etudiant2 Humain(nom3,prenom3,15,4,tab);
Humain.affic();
cout<<Humain.Moyenne()<<endl;
return 1;
}
