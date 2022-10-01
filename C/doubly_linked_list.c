#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
    struct node *prev;
};
struct node *creat_list(struct node *head, int data)
{
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    temp->data = data;
    if (head == NULL)
    {
        temp->next = NULL;
        temp->prev = NULL;
        head = temp;
        return head;
    }
    head->prev = temp;
    temp->next = head;
    head = temp;
    head->prev = NULL;
    return head;
}
struct node *insert_at_index(struct node *head, int data, int index)
{
    struct node *ptr = (struct node *)malloc(sizeof(struct node));
    ptr->data = data;
    struct node *p = head;
    struct node *q = head->next;
    int i = 0;
    while (i < index - 1)
    {
        p = p->next;
        q = q->next;
        i++;
    }
    ptr->prev = p;
    ptr->next = q;
    p->next = ptr;
    q->prev = ptr;
    return head;
};
struct node *insert_at_end(struct node *head, int data)
{
    struct node *ptr = (struct node *)malloc(sizeof(struct node));
    ptr->data = data;
    struct node *p = head;
    while (p->next != NULL)
    {
        p = p->next;
    }
    p->next = ptr;
    ptr->prev = p;
    ptr->next = NULL;
    return head;
}
void print(struct node *head)
{
    struct node *ptr = head;
    printf("\nThe linked list is:\n");
    while (ptr != NULL)
    {
        printf("Element : %d \n", ptr->data);
        ptr = ptr->next;
    }
    printf("\n");
}
void reverse(struct node *head)
{
    struct node *current = head;
    while (current->next != NULL)
    {
        current = current->next;
    }
    head = current;
    struct node *ptr = head;
    printf("\nThe linked list is:\n");
    while (ptr != NULL)
    {
        printf("Element : %d \n", ptr->data);
        ptr = ptr->prev;
    }
    printf("\n");
}
struct node *delet_at_first(struct node *head)
{
    struct node *ptr = head;
    head = head->next;
    head->prev = NULL;
    free(ptr);
    return head;
}
struct node *delet_at_end(struct node *head)
{
    struct node *ptr = head;
    struct node *p = head->next;
    while (p->next != NULL)
    {
        p = p->next;
        ptr = ptr->next;
    }
    ptr->next = NULL;
    free(p);
    return head;
}
struct node *delet_at_index(struct node *head, int index)
{
    struct node *ptr = head;
    struct node *p = head->next;
    struct node *q;
    int i = 0;
    while (i != index - 2)
    {
        p = p->next;
        ptr = ptr->next;
        i++;
    }
    ptr->next = p->next;
    q = p;
    q = q->next;
    q->prev = ptr;
    free(p);
    return head;
}
int main()
{
    struct node *head = NULL;
    int n, data, pos;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        printf("Element: ");
        scanf("%d", &data);
        head = creat_list(head, data);
    }

    print(head);

    delet_at_first(head);
    print(head);

    printf("Enter the elements to enter at end: ");
    scanf("%d", &data);
    insert_at_end(head, data);
    print(head);

    printf("Enter the position of elements to delete: ");
    scanf("%d", &pos);

    delet_at_index(head, pos);
    print(head);

    reverse(head);
    return 0;
}
