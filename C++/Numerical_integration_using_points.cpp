//using data trapezoidal,simpson' 1/3 and simpson's 3/8 rule
#include <iostream>
#include <cmath>
using namespace std;

float trapezoid(float h, float y[10], int n){
    float sum;
    sum = (y[0]+y[n]);
    for(int i=1; i<=n-1;i++){
        sum += 2*y[i];
    }
    sum= sum*(h/2);
    return sum;
}
float simpson_1_3(float h, float y[10], int n){
    float sum;
    sum = (y[0]+y[n]);
    for(int i=1; i<=n-1;i++){
        if(i % 2 == 0){
            sum += 2*y[i];
        }else{
            sum += 4*y[i];
        }   
    }
    sum= sum*(h/3);
    return sum;
}
float simpson_3_8(float h, float y[10], int n){
    float sum;
    sum = (y[0]+y[n]);
    for(int i=1; i<=n-1;i++){
        if(i % 3 == 0){
            sum += 2*y[i];
        }else{
            sum += 3*y[i];
        }
    }
    sum= sum*(3*h/8);
    return sum;
}
int main(){
    int n;
    float x0,xn,y[10],h;
    cout<<"Input n"<<endl;
    cin>>n;
    cout<<"Input x0 and xn"<<endl;
    cin>>x0>>xn;
    cout<<"Input y"<<endl;
    for(int i=0; i<=n; i++){
        cin>>y[i];
    }
    h=(xn-x0)/n;
    cout<<"Result using trapezoid is "<<trapezoid(h,y,n)<<endl;
    if(n%2==0){
        cout<<"Result using simpson_1_3 is "<<simpson_1_3(h,y,n)<<endl;
    }else{
        float sum;
        sum = simpson_1_3(h,y,n-1) + (h*(y[n-1]+y[n]))/2;
        cout<<"Result using simpson_1_3 is "<<sum<<endl;
    }
    if(n%3==0){
        cout<<"Result using simpson_1_3 is "<<simpson_3_8(h,y,n)<<endl;
    }else if(n%3==2){
        float sum;
        sum = simpson_3_8(h,y,n-2) + (h*(y[n-2]+2*y[n-1]+y[n]))/2;
        cout<<"Result using simpson_3_8 is "<<sum<<endl;
    }
    else{
        float sum;
        sum = simpson_3_8(h,y,n-1) + (h*(y[n-1]+y[n]))/2;
        cout<<"Result using simpson_1_3 is "<<sum<<endl;
    }
    return 0;   
}