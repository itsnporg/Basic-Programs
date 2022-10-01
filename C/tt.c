#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


//let's complete the print board function
//we will be using ternary operator to add X if xState is 1 else leave the same number
//and same to the zState
void printBoard(int xState[], int zState[]){
    for (int i=0; i<9; i++){
        if (xState[i] == 1){
            printf(i%3 == 0?"\nX":"\tX");
        }
        else if(zState[i] == 1){
            printf(i%3 == 0?"\nO":"\tO");

        }
        else{
            printf(i%3==0?"\n%d":"\t%d",i);
        }
    }
}

//function to check if position is already filled
bool alreadyFilled(int choosen[], int a){
    if (choosen[a] != 1){
        return false;
    }
    else{
        return true;
    }
}

void checkWins(int xState[], int zState[]){
    int sum = 0;
    //sum to exit the program if all box are filled and the result is tie.
    //we can do it in another way too by adding else conditional
    for (int i=0; i<9; i++){
        sum = sum + xState[i] + zState[i];
    }
    //we need to check what are the wins condition. 0,1,2 or 3,4,5 or 6,7,8 or 0,3,6 or 1,4,7 or 2,5,8 or diagonally 0,4,8 or 2,4,6
    //if the sum of any of this triplets equals 3 then the corresponding player wins.
    if ((xState[0] + xState[1] + xState[2] == 3) || (xState[3] + xState[4] + xState[5] == 3) || (xState[6] + xState[7] + xState[8] == 3) || (xState[0] + xState[3] + xState[6] == 3) || (xState[1] + xState[4] + xState[7] == 3) || (xState[2] + xState[5] + xState[8] == 3) || (xState[0] + xState[4] + xState[8] == 3) || (xState[2] + xState[4] + xState[6] == 3)){
        printBoard(xState, zState);
        printf("\n\nX wins! Match Over...;");
        exit(1);
    }
    if ((zState[0] + zState[1] + zState[2] == 3) || (zState[3] + zState[4] + zState[5] == 3) || (zState[6] + zState[7] +zState[8] == 3) || (zState[0] + zState[3] + zState[6] == 3) || (zState[1] + zState[4] + zState[7] == 3) || (zState[2] + zState[5] + zState[8] == 3) || (zState[0] + zState[4] + zState[8] == 3) || (zState[2] + zState[4] + zState[6] == 3)){
        printBoard(xState, zState);
        printf("\n\nZ wins! Match Over...;");
        exit(1);
    }
    if (sum >= 9 ){
        printf("\n\nTIE! Match Over...");
        exit(1);
    }

}

//now lets try our code, still we need to check the winner!

int main(){
    int xState[] = {0,0,0,0,0,0,0,0,0};
    int zState[] = {0,0,0,0,0,0,0,0,0};
    int turn = 1;
    int choose;
    int choosen[] = {0,0,0,0,0,0,0,0,0};


    while(1){
        if (turn == 1){
            printBoard(xState, zState);
            printf("\n\nX's Turn!");
            printf("\nChoose a position(0-9): ");
            scanf("%d", &choose);
            //let's make a function to check if the position is empty or not
            //this check whether the choosen number is empty or filled
            while(1){
                if (alreadyFilled(choosen, choose)){
                    printf("\nPosition already entered. Choose another position: ");
                    //we also need to take input again if it's already filled
                    scanf("%d",&choose);
                }
                else{
                    break;
                }
            }
            xState[choose] = 1;
            //add the choosen position to the choosen array
            choosen[choose] = 1;
            
        }
        if (turn == 0){
            printBoard(xState, zState);
            printf("\n\nZ's Turn!");
            printf("\nChoose a position(0-9): ");
            scanf("%d", &choose);
            while(1){
                if (alreadyFilled(choosen, choose)){
                    printf("\nPosition already entered. Choose another position: ");
                    scanf("%d",&choose);
                }
                else{
                    break;
                }
            }
            //forget to change the x here.
            zState[choose] = 1;
            choosen[choose] = 1;
        }
        turn = !turn;
        //let's add a check win function here
        checkWins(xState, zState);
    }


}
//works perfectly fine till now
//lets add checkWin function
//we're done but what if no one wins
//nothing happens so lets add a condition