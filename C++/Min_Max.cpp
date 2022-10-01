#include <bits/stdc++.h>
using namespace std;
#define lli long long int

int main()
{
    int n;
    cout<<"Enter Size of the array:";
    cin>>n;
    vector<int> v;
    for(int i=0; i<n; i++)
    {
        int input;
        cin>>input;
        v.push_back(input);
    }
    int min_e=v[0];
    int max_e=v[0];
    for(int i=1; i<n; i++)
    {
        min_e=min(v[i], min_e);
        max_e=max(v[i], max_e);
    }
    cout<<"Maximum element="<<max_e<<endl;
    cout<<"Minimum element="<<min_e<<endl;
    return 0;
}