#include "complexe.h"
#include <iostream>
using namespace std;
int main(){
  //complexe a,b(5,9),c(b);
  //cout<<"Partie Réelle de b: "<<b.getRe()<<"\t"<<"Partie Imaginaire de C: "<<c.getIm()<<endl;
  //a.Print();
  //bool t1=b.Identical(c);
  //cout<<t1<<endl;
  //b.Sum(c);
  //b.Print();
  //t1=b.Identical(c);
  //cout<<t1<<endl;
  complexe x(1,2);
  complexe y(3,4);
  complexe z(y);
  x.Print();
  (x.Sum1(y));
  x.Print();
  (x.Sum2(y)).Print();
  x.Print();
  ((x.Sum2(y)).Sum2(z)).Print();
  x.Print();
  ((x.Sum3(y)).Sum3(z)).Print();
  x.Print();
  ((x.Sum4(y)).Sum4(z)).Print();
  x.Print();
}
