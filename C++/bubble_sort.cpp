#include <iostream>
using namespace std;

int n, v[1024];

void buubble_sort(int v[], int n){
    /*
    Modifies the given array for it to be sorted. 

    :param v[]: The given array of items
    :param n: The number of items in the array
    */
   bool is_sorted = false; // Considers the array not sorted by default 

   while(!is_sorted){ // While the array is not sorted...
       is_sorted = true; // ...it is first considered sorted...
       for(int i=1; i<n; i++){ // ...then we iterate to all items in the array...
           if(v[i-1] > v[i]){  // ...and if we find 2 items which are in the wrong order...
               is_sorted = false; // ...we consider the array not sorted again...

               int aux = v[i]; // ...and we interchange the wrongly arranged variables. 
               v[i] = v[i-1];
               v[i-1] = aux;
           }
       }
   }
}

int main(){
    //Handling the input
    cout << "Input the number of items\n";
    cin >> n;
    cout << "Input the numbers\n";
    for(int i=0; i<n; i++) cin >> v[i];

    //Calling the function
    buubble_sort(v, n);

    //Handling the output
    cout << "The sorted array is: ";
    for(int i=0; i<n; i++) cout << v[i] << ' ';
    cout << '\n';

    return 0;
}