#include<bits/stdc++.h>
using namespace std;

/*
You are given two arrays value and weight of N items and capacity of bag W.
Find the maximum possible profit(sum of value of items in bag) we can get taking items that bag can hold
*/

// Recursive Approach
int KSRec(vector<int>weight,vector<int>val,int capacity, int n){
	if(n==0 || capacity==0) return 0;
	if(weight[n-1]<=capacity){
		return max(
			val[n-1]+KSRec(weight,val,capacity-weight[n-1],n-1),
			KSRec(weight,val,capacity,n-1)
		);
	}else{
		return KSRec(weight,val,capacity,n-1);
	}
}

// Recursion + Memoization
int KSMem(vector<int>weight,vector<int>val,int capacity, int n, vector<vector<int>> &memT){
	if(n==0 || capacity==0) memT[n][capacity]=0;
	if(memT[n][capacity]!= -1) return memT[n][capacity]; 
	if(weight[n-1]<=capacity){
		return memT[n][capacity]=max(
			val[n-1]+KSMem(weight,val,capacity-weight[n-1],n-1,memT),
			KSMem(weight,val,capacity,n-1,memT)
		);
	}else{
		return memT[n][capacity]=KSMem(weight,val,capacity,n-1,memT);
	}
}

// Dynamic Programming Top-Down Aproach
int KSDP(vector<int>weight,vector<int>val,int capacity, int n){
	int t[n+1][capacity+1];
	
	for(int i=0;i<=n;i++){
		for(int j=0;j<=capacity;j++){
			if(i==0 || j==0) t[i][j]=0; //Base Cases or Initializations
			else if(weight[i-1]<=j){
				t[i][j]=max(t[i-1][j],val[i-1]+t[i-1][j-weight[i-1]]); //Actual Recursive Convesion
			}else{
				t[i][j]=t[i-1][j];
			}
		}
	}
	return t[n][capacity];
}

void solve(){
	int n,W;
	cout<<"Enter the number of items: ";
	cin>>n;
	
	vector<int>val(n);
	vector<int>weight(n);
	
	cout<<"Enter weight of Items: ";
	for(int i=0;i<n;i++) cin>>weight[i];
	cout<<"Enter value of Items: ";
	for(int i=0;i<n;i++) cin>>val[i];
	
	cout<<"Enter the weight capacity of bag: ";
	cin>>W;
	
	cout<<"Solution using Recursion: ";
	cout<<KSRec(weight,val,W,n)<<endl<<endl;
	
	vector<vector<int>>memT(n+1,vector<int>(W+1,-1));
	cout<<"Solution using Memoization: ";
	cout<<KSMem(weight,val,W,n,memT)<<endl<<endl;
	
	cout<<"Enter value of DP Top-Down approach: ";
	cout<<KSDP(weight,val,W,n)<<endl<<endl;
}

int main(){
	int t;
	cout<<"Enter the number of testcases: ";
	cin>>t;
	while(t--)
	   solve();
	return 0;
}

