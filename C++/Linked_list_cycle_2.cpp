#include <bits/stdc++.h>
using namespace std;
struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution
{
public:
    ListNode *detectCycle(ListNode *head)
    {
        if (head == NULL || head->next == NULL)
            return NULL;
        ListNode *slow = head, *fast = head;
        do
        {
            slow = slow->next;
            fast = fast->next->next;
        } while (fast != slow and fast and fast->next);
        if (fast == slow)
        {
            while (head != slow)
            {
                head = head->next;
                slow = slow->next;
            }
            return head;
        }
        return NULL;
    }
};
