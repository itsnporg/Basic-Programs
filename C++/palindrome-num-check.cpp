#include <iostream>
using namespace std;

int isPalindrome(int x) {
    //complete the function
    int y;
    int num = 0;
    while(x!=0){
      y = x%10;
        num = num*10 + y;
        x /= 10; 
    }
     return num;
    
}

int main() {
    int n;
    cin >>n;
    if(isPalindrome(n) == n) {
        cout <<n<<" is a palindrome";
    }
    else {
        cout << n<<" is NOT a palindrome";
    }
    return 0;
}
