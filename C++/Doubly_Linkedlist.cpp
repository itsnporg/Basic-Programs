//This is the code for implementation of Double Linked List
#include<iostream>
using namespace std;

struct node
{
    int data;
    node* prev;
    node* next;
};

node* Insert(node* head,int x,int n)
{
    node* newNode = new node();
    newNode->data=x;
    newNode->prev=NULL;
    newNode->next=NULL;
    if (head==NULL)
    {
        head = newNode;
        return head;
    }
    
    if (n==1)
    {
        head->prev = newNode;
        newNode->next = head;
        head=newNode;
        return head;
    }
    n=n-2;
    node* temp = head;
    while (temp->next!=NULL && n--)
    {
        temp=temp->next;
    }
    if (temp->next==NULL)
    {
        temp->next=newNode;
        newNode->prev=temp;
        return head;
    }
    
    newNode->prev=temp;
    newNode->next=temp->next;
    temp->next->prev=newNode;
    temp->next=newNode;
    return head;
}

void Print(node* head)
{
    while (head!=NULL)
    {
        cout<<head->data<<" ";
        head=head->next;
    }
    cout<<"\n";  
}

void ReversePrint(node* head)
{
    while (head->next!=NULL)
    {
        head=head->next;
    }
    while (head!=NULL)
    {
        cout<<head->data<<" ";
        head=head->prev;
    }  
    cout<<"\n";
}

int main()
{
    node* head=NULL;
    head = Insert(head,4,1);
    Print(head);
    ReversePrint(head);

    head = Insert(head,5,2);
    Print(head);
    ReversePrint(head);

    head = Insert(head,6,1);
    Print(head);
    ReversePrint(head);

    head = Insert(head,1,3);
    Print(head);
    ReversePrint(head);

    head = Insert(head,9,6);
    Print(head);
    ReversePrint(head);
}