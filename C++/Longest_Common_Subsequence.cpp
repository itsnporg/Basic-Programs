#include <bits/stdc++.h>
using namespace std;

int longestCommonSubsequence(string a, string b) {
        int n = a.size();
        int m = b.size();
        int dp[n+6][m+7];
        memset(dp,0,sizeof(dp));

        for(int i = 1; i<=n; i++){
            for(int j = 1; j<=m; j++){
                if(a[i-1] == b[j-1])
                dp[i][j] = 1 + dp[i-1][j-1];
                else
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
        return dp[n][m];
}
    
int main(){
	
	string a,b;
	cin>>a>>b;
	int ans = longestCommonSubsequence(a,b);
	cout<<ans<<endl;

	return 0;
}
