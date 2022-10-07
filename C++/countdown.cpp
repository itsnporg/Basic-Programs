
#include <iostream>
using namespace std;

/* You need to make a countdown app.
Given a number N as input, output numbers from N to 1 on separate lines. 
Also, when the current countdown number is a multiple of 5, the app should output "Beep".
*/

int main() {
    int n;
    cin >> n;
    
for(n=n;n=n;n--){
        cout<<n<<"\n";
              if(n%5==0){
        	cout<<"Beep"<<"\n";
        }  
    }
    
    
    return 0;
}
