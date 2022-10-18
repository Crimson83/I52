#include "polynome.h"
#include "vecteurcomplexe.h"
#include "complexe.h"
#include <fstream>
#include <iostream>

using namespace std;

int main(){
  //float t[5]={1,2,3,4,5};
  //float u[5]={6,7,8,9,10};
  //polynome y(4,t),x(4,u);
  //y.Affic();
  //x.Affic();
  //y=x;
  //y.Affic();
  complexe x;
  complexe *c=new complexe[3];
  for(int i=0;i<3;i++){
    c[i]=complexe();
  }
  vecteurcomplexe y(c,3);
  ifstream fic("data.txt");
  vecteurcomplexe w(fic);
  vecteurcomplexe z(y);
  cout<<w<<z<<endl;
  x=w[2];

  cout<<x<<endl;
  return 0;
}
