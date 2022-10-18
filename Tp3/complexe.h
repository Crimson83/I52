#ifndef COMPLEXE_
#define COMPLEXE_
#include <iostream>

using namespace std;

class complexe{
  private:
    float re;
    float im;
  public:
    complexe();
    complexe(float,float);
    complexe(const complexe&);
    ~complexe();
    void AfficherComplexe();
    complexe operator+(const complexe&);
    complexe operator-(const complexe&);
    complexe operator*(const complexe&);
    complexe operator*(float);
    friend complexe operator*(float,const complexe&);
    complexe operator/(const complexe&);
    friend ostream& operator<<(ostream&,const complexe&);
};
#endif
