# include < iostream>
# include < string >
using namespace std;
int main()

{
char str1[50], str2 [35];
cout << "Enter string str1;";
cin >> str1;
cout << "Enter string str2:";
cin >> str2;
strcat(str1,str2);
cout << "strcat (str1, str2 ) : "<< str1;

    system("pause");
return 0;
}
