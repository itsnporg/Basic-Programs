#include<bits/stdc++.h>
#define FastRead ios_base::sync_with_stdio(false);cin.tie(0),cout.tie(0)
using namespace std;

static int counter=0;

void dfs(int node, vector<vector<int>>&adj, vector<int>&vis){
	if(vis[node]==0) return;
	vis[node]=1;
	counter++;
	for(auto &x:adj[node]){
		if(vis[x]==-1){
			dfs(x,adj,vis);
		}
	}
}

int safe_paths(vector<int>theives, vector<vector<int>>edges){
	int n=edges.size()+1;
	vector<vector<int>>adj(n+1);
	vector<int>vis(n+1,-1);
	for(auto &edge:edges){
		adj[edge[0]].push_back(edge[1]);
		adj[edge[1]].push_back(edge[0]);
	}
	for(auto &theive: theives) { vis[theive]=0;}
	dfs(1,adj,vis);
	return counter-1;
}

void solve(){
	int n,k,u,v;
	cin>>n>>k;
	vector<int>trees(k);
	vector<vector<int>>edges(n-1,vector<int>(2));
	for(int i=0;i<n-1;i++){
		cin>>u>>v;
		edges[i][0]=u;
		edges[i][1]=v;
	}
	for(int i=0;i<k;i++) cin>>trees[i];
	cout<<safe_paths(trees, edges)<<endl;
}

int main(){
	FastRead;
	int t;
	cin>>t;
	while(t--) solve();
	return 0;
}

// DESCRIPTION:
// There are n cities numbered from 1 to n and there are n-1 bidirectional roads such that all cities are connected 
// There are k trees, each one is in a different city. You are currently in the 1st city. 
// You want to visit city X such that neither X nor the cities in the path from 1 to X has a tree
// Find out how many such X you can visit (X = 1)


// INPUT
// 1
// 6 3
// 1 2 
// 1 6
// 2 3
// 2 4 
// 2 5
// 2 3 4

// OUTPUT:
// 1

// EXPLANATION:
// There are total 5 possibilities
// 1) 1-2
// 2) 1-2-3
// 3) 1-2-4
// 4) 1-2-5
// 5) 1-6
// In the first 4 cases the 2nd city has a thief so he can't go 2nd 3rd 4th and 5th city, 
// but in 5th cose none of the city on the simple path has thief so he can go 6th city