#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int n,d;
    float x[10],y[10], a[10][10];
    cout<<"ENter the value of n"<<endl;
    cin>>n;
    cout<<"ENter the value of d"<<endl;
    cin>>d;
    cout<<"ENter value of x"<<endl;
    for(int k=0;k<n;k++){
        cin>>x[k];
    }
    cout<<"ENter value of y"<<endl;
    for(int k=0;k<n;k++){
        cin>>y[k];
    }
    for(int i=0; i<(d+1); i++){
        for(int j=0; j<(d+1); j++){
            a[i][j]= 0;
            for(int k=0; k<(n-1);k++){
                a[i][j]+= pow(x[k],i+j);           
            }
        }
    }
    for(int i=0;i<=d;i++){
        a[i][d+1]=0;
        for(int k=0; k<(n-1);k++){
            a[i][d+1]+= pow(x[k],i)*y[k];           
        }

    }
    for(int j=0; j<= d; j++){
        if(fabs(a[j][j])< 5E-10 ){
            break;
        }
        for(int i=0; i<=d;i++){
            if(i != j){
                float temp;
                temp = a[i][j];
                 for (int k=0; k<=(d+1); k++){
                    a[i][k]= a[i][k]-((temp/a[j][j])*a[j][k]);
            }
                }

        }
    }
    for(int i=0;i<=d;i++ ){
        //for(int j=0; j<n; j++)
            //if
            cout<<"a"<<i<<"="<<a[i][d+1]/a[i][i]<<endl;

        }





}
