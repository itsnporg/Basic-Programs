#include <bits/stdc++.h>
using namespace std;

string longestPalindrome(string s) 
    {
        int best_length=0, n=s.size();
        string ans="";
        for(int mid=0; mid<n; mid++)
        {
            for(int i=0; mid-i>=0 && mid+i<n; i++)
            {
                if(s[mid-i]!=s[mid+i])
                {
                    break;
                }
                if( 2*i+1> best_length)
                {
                    best_length=2*i+1;
                    ans= s.substr(mid-i, best_length);
                }                  
            }
        }
        for(int mid=0; mid<n-1; mid++)

        {
            for(int i=1; mid-i+1>=0 && mid+i<n; i++)
            {
                if(s[mid-i+1]!=s[mid+i])
                {
                    break;
                }
                if( 2*i>best_length)
                {
                    best_length=2*i;
                    ans=s.substr( mid-i+1,best_length);
                }
            }
        }
        return ans;
    }
    
int main(){
	
	string s;
	cin>>s;
	string ans = longestPalindrome(s);
	cout<<ans<<endl;

	return 0;
}
