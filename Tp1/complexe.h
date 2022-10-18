#ifndef _COMP
#define _COMP
typedef struct{
  unsigned int ident;
  float re;
  float im;
}Complexe;
typedef Complexe* ptComplexe;
void AfficherComplexe(const Complexe &);
Complexe Somme(const Complexe&, const Complexe&);
Complexe Produit(const Complexe&, const Complexe&);
float Module(const Complexe&);
Complexe Conjuge(const Complexe&);
void Init(Complexe&);
Complexe Bidon(Complexe&);
void CreerComplexe(Complexe**);
void CreerComplexe(ptComplexe&);
Complexe* CreerComplexe();
Complexe* CreerVecteurComplexes(unsigned int);
#endif
