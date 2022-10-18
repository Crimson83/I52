class complexe{
  private :
    float re;
    float im;
  public :
    complexe();
    complexe(float,float);
    complexe(const complexe&);
    ~complexe();
    void Print();
    float getRe();
    float getIm();
    //void Sum(const complexe&);
    complexe Sum(const complexe&);
    void Sum1(const complexe&);
    complexe Sum2(const complexe&);
    complexe Sum3(const complexe&);
    complexe& Sum4(const complexe&);
    bool Identical(const complexe&);
};
