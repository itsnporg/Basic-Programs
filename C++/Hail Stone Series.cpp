/*
Hail Stone Series

Hail Stone series is series of these 3 steps:
1. Take any number, print it
2. If the number is even then print num/2
3. If the number is odd then print num*3+1
		eg: 16,8,4,2,1,4,2,1...

FunFact about it:- Take any real no. it'll end as ...,4,2,1
*/

#include <iostream>
using namespace std;
int main()
{
	cout << "\t\tProgram to print Hail Stone Series"<< endl;
	int num, nterm;
	cout << "Enter starting number\t";
	cin >> num;
	cout << "How many terms do you want to print\t";
	cin >> nterm;

	for (int i = 0; i < nterm; i++)
	{
		cout << num << " ";
		if (num % 2 == 0)
			num /= 2; //this means n = n/2
		else
			num = num * 3 + 1;
	}
	return 0;
}
