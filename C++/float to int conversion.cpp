/*
When rounding floating numbers to integers, we have several options available.
Macro definitions exist in cfenv or fenv.h for each of those options.
*/

#include <iostream>
#include <cmath>
#include <cfenv>
using namespace std;

int main() {
    double n = 3.14;
    cout << n << endl;
    cout << "To nearest\n";
    fesetround(FE_TONEAREST);
    cout << rint(n) << endl;
    cout << "Upward\n";
    fesetround(FE_UPWARD);
    cout << rint(n) << endl;
    cout << "Downward\n";
    fesetround(FE_DOWNWARD);
    cout << rint(n) << endl;
    cout << "Toward zero\n";
    fesetround(FE_TOWARDZERO);
    cout << rint(n) << endl;
    
    n = -3.14;
    cout << endl << endl << n << endl;
    cout << "To nearest\n";
    fesetround(FE_TONEAREST);
    cout << rint(n) << endl;
    cout << "Upward\n";
    fesetround(FE_UPWARD);
    cout << rint(n) << endl;
    cout << "Downward\n";
    fesetround(FE_DOWNWARD);
    cout << rint(n) << endl;
    cout << "Toward zero\n";
    fesetround(FE_TOWARDZERO);
    cout << rint(n) << endl;
    return 0;
}
