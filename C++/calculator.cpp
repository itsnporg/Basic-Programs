#include<iostream>
using namespace std;


void single(){
 unsigned int a,b;
   char m;
cout<<"Enter the type of process that you wana do(+,-,*,/) :";
cin>>m;

    switch(m){
        case '+':{
            cout<<"Enter the first number :";
            cin>>a;
             cout<<"Enter the second number :";
            cin>>b;

            cout<<"The sum is :"<<a+b;
            break;
        }
         case '*':{
            cout<<"Enter the first number :";
            cin>>a;
             cout<<"Enter the second number :";
            cin>>b;

            cout<<"The sum is :"<<a*b;
            break;
        }
         case '-':{
            cout<<"Enter the first number :";
            cin>>a;
             cout<<"Enter the second number :";
            cin>>b;

            cout<<"The sum is :"<<a-b;
            break;
        }
         case '/':{
            cout<<"Enter the first number :";
            cin>>a;
             cout<<"Enter the second number :";
            cin>>b;

            cout<<"The sum is :"<<a/b;
            break;
        }

         default :{
            cout<<"invalid";
        }
    }
}

void multi(){
  float a,b;
   char m;
cout<<"Enter the type of process that you wana do(+,-,*,/) :";
cin>>m;

    switch(m){
        case '+':{
            cout<<"Enter the first number :";
            cin>>a;
             cout<<"Enter the second number :";
            cin>>b;

            cout<<"The sum is :"<<a+b;
            break;
        }
         case '*':{
            cout<<"Enter the first number :";
            cin>>a;
             cout<<"Enter the second number :";
            cin>>b;

            cout<<"The sum is :"<<a*b;
            break;
        }
         case '-':{
            cout<<"Enter the first number :";
            cin>>a;
             cout<<"Enter the second number :";
            cin>>b;

            cout<<"The sum is :"<<a-b;
            break;
        }
         case '/':{
            cout<<"Enter the first number :";
            cin>>a;
             cout<<"Enter the second number :";
            cin>>b;

            cout<<"The sum is :"<<a/b;
            break;
        }

         default :{
            cout<<"invalid";
        }
    }
}

int main(){
    char value;
   cout<<"------------WELCOME!!!!------------"<<"\n";
   cout<<"What type of process would you wana do?"<<"\n"<<"1)Press (a) for non-decimal "<<"\n"<<"2)Press (b) for decimal operation(Can be done for positive value only)"<<"\n";
   cin>>value;
   if(value='a'){
    single();
   }else if(value='b'){
    multi();
   }else{
    cout<<"You have entered a wrong value.";
   }
}