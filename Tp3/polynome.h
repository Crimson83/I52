#ifndef POLYNOME_
#define POLYNOME_
class polynome{
  private :
    float* coef;
    int deg;
  public :
    polynome();
    polynome(int,float*);
    polynome(const polynome&);
    ~polynome();
    polynome& operator=(const polynome&);
    void Affic();
};
#endif
