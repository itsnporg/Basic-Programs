//using data trapezoidal,simpson' 1/3 and simpson's 3/8 rule
#include <iostream>
#include <cmath>
using namespace std;
float f(float x){
    return pow(x,3)+1;                        
}

void trapezoid(float x0, float xn,float h, int n){
    float sum;
    sum = f(x0)+f(xn);
    for(int i=1; i<=n-1;i++){
        sum += 2*f(x0+i*h);
    }
    sum= sum*(h/2);
    cout<<"Result using trapezoid is "<<sum<<endl;
}
void simpson_1_3(float x0, float xn,float h, int n){
    float sum;
    sum = f(x0)+f(xn);
    for(int i=1; i<=n-1;i++){
        if(i % 2 == 0){
            sum += 2*f(x0+i*h);
        }else{
            sum += 4*f(x0+i*h);
        }   
    }
    sum= sum*(h/3);
    cout<<"Result  using simpson 1/3 is "<<sum<<endl;
}
void simpson_3_8(float x0, float xn,float h, int n){
    float sum;
    sum = f(x0)+f(xn);
    for(int i=1; i<=n-1;i++){
        if(i % 3 == 0){
            sum += 2*f(x0+i*h);
        }else{
            sum += 3*f(x0+i*h);
        }
    }
    sum= sum*(3*h/8);
    cout<<"Result using simpson 3/8 is "<<sum<<endl;
}

int main(){
    int n;
    float x0,xn,y[10],h;
    cout<<"Input n"<<endl;
    cin>>n;
    cout<<"Input x0 and xn"<<endl;
    cin>>x0>>xn;
    h=(xn-x0)/n;
    if(n%2!=0 && n%3!=0){
        cout<<"n must be multiple of 3 and even"<<endl;
        exit(0);
    }    
    trapezoid(x0,xn,h,n);
    simpson_1_3(x0,xn,h,n);
    simpson_3_8(x0,xn,h,n);
    
    
}