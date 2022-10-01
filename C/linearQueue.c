#include<stdio.h>
#include<stdlib.h>
#define MAXSIZE 5
int queue[MAXSIZE],data,rear=-1,front=-1;
void enqueue();
void dequeue();
void display();
void main(){
	system("cls");
	int choice;
	start:
		printf("*** Queue Operation ***\n");
		printf("1: Enqueue Operation\n");
		printf("2: Dequeue Operation\n");
		printf("3: Display Operation\n");
		printf("4: Exit Operation\n");
		printf("Enter your choice = ");
		scanf("%d",&choice);
		switch(choice){
			case 1:enqueue();
			break;
			case 2:dequeue();
			break;
			case 3:display();
			break;
			case 4:exit(0);
			break;
			default:printf("Invalid Choice!!! Try Again");
			break;
		}
		goto start;
		getch();
	}

void enqueue(){
	if(rear==MAXSIZE-1){
		printf("\n**********************\n");
		printf("Queue Overflow");
		printf("\n**********************\n");
	}
	else{
		if(front == -1){
			rear = 0;
			front = 0;
		}
		else{
			rear = rear +1;
		}
		printf("\n**********************\n");
		printf("Enter Data: ");
		scanf("%d",&data);
		queue[rear] = data;
		printf("**********************\n");
	}
}

void dequeue(){
	if(front == -1){
		printf("\n**********************\n");
		printf("Queue Underflow");
		printf("\n**********************\n");
	}
	else{
		data = queue[front];
		if(front == rear){
			rear = -1;
			front = -1;
		}
		else{
			front = front +1;
		}
		printf("\n**********************\n");
		printf("The Dequeue Element = %d",data);
		printf("\n**********************\n");
	}
}

void display(){
	int i;
	printf("The Content of Queue: ");
	if(front==-1){
		printf("\n**********************\n");
		printf("The queue is empty");
		printf("\n**********************\n");
	}
	else{
		printf("\n**********************\n");
		for(i=front;i<=rear;i++){
			printf("%d\t",queue[i]);
		}
		printf("\n**********************\n");
	}
}