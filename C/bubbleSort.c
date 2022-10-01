#include<stdio.h>

void bubblesort(int arr[]);
void main(){
    int arr[10],i,j,temp;
    printf("Enter 10 items in array\n");

    // Assigning value to the array
    for(i=0; i<10; i++){
        scanf("\n%d",&arr[i]);
    }

    // Sorting
    bubblesort(arr);
    // for(i=0;i<10;i++){
    //     for(j=i+1;j<10;j++){
    //         if(arr[i] > arr[j]){
    //             temp = arr[i];
    //             arr[i] = arr[j];
    //             arr[j] = temp;
    //         }
            
    //     }
    // }

    // Printing the sorted array
    for(i=0;i<10;i++){
        printf("%d\t",arr[i]);
    }
}

void bubblesort(int arr[]){
    int i, j, temp;
    for(i=0;i<10;i++){
        for(j=i+1;j<10;j++){
            if(arr[i] > arr[j]){
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
            
        }
    }
}
