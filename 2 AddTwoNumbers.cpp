#include <iostream>

using namespace std;

/*Definition for singly-linked list.*/
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
  
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int sum=0;  // to calculate each digit
        ListNode *p1=l1,*p2=l2,*p,*header=new ListNode();
        p=header;
        while(p1&&p2){
            p->next=new ListNode();
            p=p->next;
            sum+=p1->val+p2->val;
            p->val=sum%10;
            sum/=10;  // calculate the carry
            p1=p1->next,p2=p2->next;
        }
        while(p1){
            p->next=new ListNode();
            p=p->next;
            sum+=p1->val;
            p->val=sum%10;
            sum/=10;
            p1=p1->next;
        }
        while(p2){
            p->next=new ListNode();
            p=p->next;
            sum+=p2->val;
            p->val=sum%10;
            sum/=10;
            p2=p2->next;
        }
        if(sum!=0)
            p->next=new ListNode(sum);

        return header->next;
    }
};

ListNode* create1() {
    ListNode* p= new ListNode(5);
    p->next=new ListNode(6);
    p->next->next=new ListNode(4);
    return p;
}

ListNode* create2() {
    ListNode* p= new ListNode(7);
    p->next=new ListNode(0);
    p->next->next=new ListNode(8);
    return p;
}

int main()
{
    ListNode *l1=create1(),*l2=create2();
    Solution soln=Solution();
    ListNode *r=soln.addTwoNumbers(l1,l2);
    while(r){
        cout << r->val << endl;
        r=r->next;
    }
    return 0;
}