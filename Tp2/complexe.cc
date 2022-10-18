#include <iostream>
#include "complexe.h"
using namespace std;

complexe::complexe(){
  re=0;
  im=0;
}
complexe::complexe(float a, float b){
  re=a;
  im=b;
}
 complexe::complexe(const complexe &c){
   re=c.re;
   im=c.im;
}
void complexe::Print(){
  cout<<re<<"\t"<<im<<endl;
}
complexe::~complexe(){
  cerr<<"destruction"<<endl;
}

float complexe::getRe(){
  return re;
}

float complexe::getIm(){
  return im;
}

//void complexe::Sum(const complexe& c){
//  re=re+c.re;
//  im=im+c.im;
//}

complexe complexe::Sum(const complexe& c){
  complexe oui;
  oui.re=oui.re+c.re;
  oui.im=oui.im+c.im;
  return oui;
}

void complexe::Sum1(const complexe& z)
{
  re = re + z.re;
  im = im + z.im;
}

complexe complexe::Sum2(const complexe& z)
{
  return complexe(re+z.re, im+z.im);
}

complexe complexe::Sum3(const complexe& z)
{
  re = re + z.re;
  im = im + z.im;
  return *this;
}

complexe& complexe::Sum4(const complexe& z)
{
  re = re + z.re;
  im = im + z.im;
  return *this;
}

bool complexe::Identical(const complexe& c){
  return (re==c.re)&&(im=c.im);
}
