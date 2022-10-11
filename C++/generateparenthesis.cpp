#include <bits/stdc++.h>
using namespace std;

void solve(string s, int open, int close, vector<string>&res){
        if (open==0 and close==0){
            res.push_back(s);
            return;
        }
        if (open>0){
            solve(s+"(", open-1, close, res);
        }
        if (open < close){
            solve(s+")", open, close-1, res);
        }
}

int main(){
  //n denotes the number of opening and closing parenthesis
  int n=0;
  cin >> n;
  
  vector<string> res;
  solve("", n, n, res);
  
  for (auto it: res){
    cout << it << endl;
  }
  return 0;
}
