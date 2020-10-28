/// create a program to return factorial of n

#include <iostream>

using namespace std;

int factorial(int number){
    if(number == 0 || number == 1){
        return 1;
    }
    else{
        return factorial(number-1) * number;
    }
}

int main()
{
    int n;

    cin>>n;

    cout<<"factorial: "<<factorial(n)<<endl;

    return 0;
}
