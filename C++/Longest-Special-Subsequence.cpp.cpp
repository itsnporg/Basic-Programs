#include<bits/stdc++.h>
#define FastRead ios_base::sync_with_stdio(false);cin.tie(0),cout.tie(0)
using namespace std;

static map<pair<int,char>,int>dp;

int rec(int n, int k, string s, char lastch){
	if(n==0) return dp[{n,lastch-'a'}]=0;
	if(dp[{n,lastch-'a'}]) return dp[{n,lastch-'a'}];

	if(lastch == ' ' || abs((int)(s[n-1] - lastch))<=k){
		return dp[{n,lastch-'a'}] = max(1+rec(n-1,k,s,s[n-1]),rec(n-1,k,s,lastch));
	}else{
		return dp[{n,lastch-'a'}] = rec(n-1,k,s,lastch);
	}
}

int longestSpecialSubsequence(int n, int k, string s){
	int soln = rec(n,k,s,' ');
	return soln;
}

void solve(){
	int n,k; 
	string s;
	cin>>n>>k;
	cin>>s;
	cout<<longestSpecialSubsequence(n,k,s)<<endl;
}

int main(){
	FastRead;
	int t;
	cin>>t;
	while(t--) solve();
	return 0;
}

// QUESTION:
// You are given a string s of the length n consisting of only lowercase English alphabets. You are also given an integer k.
// If the two consecutive characters in a subsequence have a difference that is no more than k, then it is called a special subsequence. Find the length of the longest special subsequence.

// INPUT:
// 1
// 7 2 afcbedg

// OUTPUT:
// 4

// EXPLANATION:
// One of the longest special sequence present in "afcbedf" is a, c, b, d. 
// It is special because |a-c|<=2, |c-b|<=2 and |b-d|<=2