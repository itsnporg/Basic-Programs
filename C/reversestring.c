#include<stdio.h>
#include<string.h>

char *reverse(char *string){
    int len,i;
    char temp;
    len=strlen(string);  // this builtin function returns the lenght of a string
    for (i=0;i<=len/2;i++){
        temp=string[i];
        string[i]=string[len-1-i];
        string[len-1-i]=temp;
        
        /*
            reversing a string is simply swapping first and last character lets see how its work 

            lets take "APPLE" 
            temp = A
            A=(len-1-i) = E   --> since we are starting our counting from 0 so len-1-i returns last character
            E=temp 
            the first and last value are swapped succesfully 

        */




    }
    return string;
}

int main(int argc, char* argv){
    char string[500];
    printf("\n Enter String : ");
    scanf("%[^\n]s",string); // fgets(string,500,stdin)
    printf("\n\n \t\t The reverse of the string is : %s",reverse(string));
    return 0;
}