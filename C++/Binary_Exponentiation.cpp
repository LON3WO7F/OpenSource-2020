#include<bits/stdc++.h>
using namespace std;



// Recursive Code..
int binaryExponentiationRecursive(int x, int n)
{
    if (n == 0)
        return 1;
    else if (n % 2 == 0)
        return binaryExponentiationRecursive(x * x, n / 2);
    else
        return x * binaryExponentiationRecursive(x * x, (n - 1) / 2);
}



// Iterative Code..
int binaryExponentiationIterative(int x, int n)
{
    int result = 1;
    while (n > 0)
    {
        if (n % 2 == 1)
            result = result * x;
        x = x * x;
        n = n / 2;
    }
    return result;
}

int main()
{
    int n, x; cin >> n >> x;
    cout << "Binary_Exponentiation_Recursive: " << binaryExponentiationRecursive(n, x) << "\n";
    cout << "Binary_Exponentiation_Iterative: " << binaryExponentiationIterative(n, x) << "\n";
    return 0;
}
