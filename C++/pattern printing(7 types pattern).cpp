//C++ pattern code by Sunil Shrestha
//add me on fb :-https://www.facebook.com/sunil.xtha.311
#include <iostream>
using namespace std;

int main()
{
	cout << "Pattern 1\n";

	// *(asterik) count == word1.length()
	//applicable for any word having odd no. letters
	string word1 = "NEPAL";
	string d = "*****";
	int mid = word1.length() / 2;

	for (int i = 0; i < mid + 1; i++)
	{
		for (int j = 0; j < word1.length(); j++)
		{
			if (j == mid || (j >= mid - i && j <= mid + i))
				cout << word1[j];
			else
				cout << d[j];
		}
		cout << endl;
	}

	cout << "\n\nPattern 2" << endl;
	/*
COMPUTER
 OMPUTE
  MPUT
   PU
*/
	string word2 = "COMPUTER";
	int n = word2.length();

	for (int i = 0; i < n / 2; i++)
	{
		for (int j = 0; j <= i; j++)
		{
			cout << " ";
		}
		for (int j = i; j < n - i; j++)
			cout << word2[j];
		cout << endl;
	}

	cout << "\n\n3) Hollow Rectangle" << endl;
	/*
	n=5
	**********
	*        *
	*        *
	*        *
	**********	
	*/
	int row = 5, col = 10;
	for (int i = 1; i <= row; i++)
	{
		for (int j = 1; j <= col; j++)
		{
			if (i == 1 || i == row || j == 1 || j == col)
				cout << "*";
			else
				cout << ' ';
		}
		cout << endl;
	}

	/*Trick:-  Break Pattern into grid of matrix m*n */
	cout << "\n\n6) Binary Pattern 1" << endl;
	/*
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
*/
	int row6 = 5;
	for (int i = 1; i <= row6; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			if ((i + j) % 2 == 0)
				cout << "1 ";
			else
				cout << "0 ";
		}
		cout << endl;
	}

	cout << "\n\n7) Binary Pattern 2\n";
	/*
1
1 0
1 0 1
1 0 1 0
1 0 1 0 1
*/
	int row7 = 5;

	for (int i = 1; i <= row7; i++)
	{
		for (int j = 1; j <= i; j++)
		{
			if (j % 2 == 0)
				cout << "0 ";
			else
				cout << "1 ";
		}
		cout << endl;
	}
	return 0;
}