#include<stdio.h>
#include<string.h>

/* 
void characterConversion(char character){
    char upperChar, lowerChar;
    int ascii;
    printf("Enter an uppercase Character: ");
    scanf("%c", &upperChar);
    ascii = upperChar;
    lowerChar = ascii+32;
    printf("\nIts Lowercase = %c", lowerChar);

} */

char* uppercase(char *string){
    char ch;
   
    int len =strlen(string);
    for (int i=0;i<len;i++){
        ch=string[i];
        if (ch >='a' && ch <='z'){
            string[i] = ch-32;
<<<<<<< HEAD

=======
        }
    }
>>>>>>> master
    return string;

}
char* lowercase(char *string){
    char ch;
    
    int len =strlen(string);
    for (int i=0;i<len;i++){
        ch=string[i];
        if (ch >='A' && ch <='Z'){
            string[i] = ch+32;
        }
    }
    return string;

}

int main()
{
   char string [500];
   printf("Enter your string :");
   scanf("%[^\n]s",string);

  
   printf("\n uppercase is %s ",uppercase(string));
   printf("\n Lowercase is %s ",lowercase(string));
   
    
    return 0;
}
