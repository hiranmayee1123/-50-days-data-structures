#include <bits/stdc++.h> 
using namespace std; 
int main()
{
	int m,n;
	cout<<"Enter size of array1: ";
	cin>>m;
	cout<<"Enter size of array2: ";
	cin>>n;
	int arr1[m];
	int arr2[n];
	cout<<"Enter elements in the first array: "<<endl;
	for(int i=0;i<m;i++){
		cin>>arr1[i];
	}
	cout<<"Enter elements in the second array:  "<<endl;
	for(int j=0;j<n;j++){
		cin>>arr2[j];
	}
	int i,j;
    while (i < m && j < n) { 
        if (arr1[i] < arr2[j]) 
            cout << arr1[i++] << " "; 
  
        else if (arr2[j] < arr1[i]) 
            cout << arr2[j++] << " "; 
  
        else { 
            cout << arr2[j++] << " "; 
            i++; 
        } 
    }
    while (i < m) 
        cout << arr1[i++] << " "; 
  
    while (j < n) 
        cout << arr2[j++] << " "; 
    return 0;
    
}
