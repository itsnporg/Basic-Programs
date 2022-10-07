#include <iostream>
#include<cmath>
using namespace std;

int main(){
    int n;
    float a[10][10], x[10];
    cout<<"Enter n"<<endl;
    cin>>n;
    cout<<"Enter value of matrix"<<endl;
    for(int i=1;i<=n;i++ ){
        for(int j=1; j<=n+1; j++){
            cout<<"a["<<i<<"]["<<j<<"]"<<endl;
            cin>>a[i][j];
        }
    }
    for(int j=1; j<= n-1; j++){
        if(fabs(a[j][j])< 5E-10 ){
            break;
        }
        for(int i=j+1; i<=n;i++){

                float temp;
                temp = a[i][j];
                 for (int k=j; k<=(n+1); k++){
                    a[i][k]= a[i][k]-((temp/a[j][j])*a[j][k]);

                }

        }
    }
    cout<<"The solution is"<<endl;
    for(int i=n;i>=1;i-- ){
        float sum =0;
        for(int j=i+1; j<=n; j++){
            sum+= a[i][j]*x[j];
        }
        x[i]= (a[i][n+1]-sum)/a[i][i];
        cout<<"x"<<i<<"="<<x[i]<<endl;
        }


    return 0;

}
