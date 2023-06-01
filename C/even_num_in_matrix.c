#include <stdio.h>

void main(){
    int mat[10][10], i, j, row, column;

    printf("Enter row and column : ");
    scanf("%d%d", &row, &column);
    printf("Enter %d number : ", row * column);

    // Taking value for matrix from user
    for(i=0;i<row;i++){
        for(j=0;j<column;j++){
            scanf("%d", &mat[i][j]);
        }
    }
    // Showing elements of matrix
    printf("Elements of matrix are : \n");
    for(i=0;i<row;i++){
        for(j=0;j<column;j++){
            printf("%d \t", mat[i][j]);
        }
        printf("\n");
    }

    // Now finding even number in matrix
    printf("\n Even number in matrix are : \t");
    for(i=0;i<row;i++){
        for(j=0;j<column;j++){
            if(mat[i][j]%2==0){
                printf("%d \t", mat[i][j] );
            }
        }
    }
}
