#include <stdio.h>
#include <string.h>
#include <conio.h>
#include <stdlib.h>
#include <windows.h>

struct login{
    char fname[100];
    char lname[100];
    char username[20];
    char password[20];
} r ;

int login(); 
int signup();
int loading();
COORD coord= {0,0};
int gotoxy();
int main(int argc, char const *argv[])
{
    system("color 0b");
    for(;;){
        int a;
        system("CLS");
        gotoxy(32,10);
        printf("Press 1 to Sign up");
        gotoxy(32,12);
        printf("Press 2 to Log In\n");
        gotoxy(32,14);
        scanf("%d", &a);
        if (a==1)
        {
            signup();
        }

        else if (a==2)
        {
            login();
            break;
        }

        else{
            system("CLS");
            gotoxy(32,10);
            printf("Plese press the correct key");
            break;
        }
    } //infinite loop close
    return 0;
}

// SIGN UP FUNCTION
int signup(){
    system("CLS");
    gotoxy(32,10);
    loading();
    
    FILE *log;
    log= fopen("login00.txt", "w");
    system("CLS");
    gotoxy(32,10);

    printf("Enter first name: ");
    scanf("%s", r.fname);
    gotoxy(32,12);
    printf("Enter last name: "); scanf("%s", r.lname);

    gotoxy(32,14);
    printf("Enter Username: "); 
    scanf("%s", r.username);
    gotoxy(32,16);
    printf("Enter Password: "); scanf("%s", r.password);
    fwrite(&r, sizeof(r), 1, log);
    system("CLS");
    fclose(log);
}

// LOGIN FUNCTION
int login(){
    system("CLS");
    gotoxy(32,10);
    loading();

    char username1[100], password1[20];
    FILE *log;
    log= fopen("login00.txt", "r");
    system("CLS");
    gotoxy(32,10);

    printf("Username: ");
    scanf("%s", username1);
    gotoxy(32,12);
    printf("Password: "); 
    scanf("%s", password1);
    while(fread(&r,sizeof(r),1,log)){
        if(strcmp(username1, r.username)==0 && strcmp(password1, r.password)==0){
            gotoxy(26,14);
            printf("Successful logged in user %s\n", r.username );
        }

        else{
            system("CLS");
            gotoxy(32,10);
            printf("Please enter correct Username or Password\n");
        }
    }
    fclose(log);
}

//Loading Loop Function
int loading(){
    for (int i = 0; i < 11; i++)
    {
        printf("-/");
        Sleep(50);
    }
}

// X-axis and Y-axis Function
int gotoxy(int x,int y)
{
    coord.X=x;
    coord.Y=y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),coord);
}