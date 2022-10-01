#include <iostream>

using namespace std;

void mergeSort(int arr[], int left, int right);
void merge(int arr[], int left,int right,int mid);
void printArray(int arr[], int n);

int main()
{
    int n = 10;
    int arr[n] = {4, 54, 3, 74, 24, 582, 1, 6, 2, 5};
    cout<<"Unsorted Array: ";
    printArray(arr, n); //UnSorted Array
    mergeSort(arr, 0,n-1);
    cout<<"Sorted Array: ";
    printArray(arr, n); //Sorted Array
    return 0;
}

//Recursive Call to divide the array till only array of size 1 remains.
void mergeSort(int arr[], int const left, int const right)
{
    if (left >= right)
    {
        return;
    }
    int mid =   left + (right-left) / 2;
    mergeSort(arr, left,mid);
    mergeSort(arr, mid+1,right);
    merge(arr,left,right,mid);
}

//Merging all divided array but in sorted order.
void merge(int arr[], int const left,int const right,int const mid){
    int subarrayleftsize = mid-left+1;
    int subarrayrightsize = right-mid;
    auto *tempsubarrayleft = new int[subarrayleftsize];
    auto *tempsubarrayright = new int[subarrayrightsize];

    for(int i = 0;i<subarrayleftsize;i++){
        tempsubarrayleft[i] = arr[left+i];
    }

    for(int i = 0;i<subarrayrightsize;i++){
        tempsubarrayright[i] = arr[mid+1+i];
    }
    int i = 0,j = 0;
    int k = 0;
    while(i < subarrayleftsize && j < subarrayrightsize){
        if(tempsubarrayleft[i] <= tempsubarrayright[j]){
            arr[left+k] = tempsubarrayleft[i];
            i++;
            k++;
        }
        else{
            arr[left+k] = tempsubarrayright[j];
            j++;
            k++;
        }
    }
    while(i < subarrayleftsize){
        arr[left+k] = tempsubarrayleft[i];
        i++;
        k++;
    }
    while(j < subarrayrightsize){
        arr[left+k] = tempsubarrayright[j];
        j++;
        k++;
    }
    delete[] tempsubarrayleft;
    delete[] tempsubarrayright;

}

//Just a utility function to print array.
void printArray(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << arr[i];
        if(i != n-1){
            cout<<", ";
        }
    }
    cout << endl;
}