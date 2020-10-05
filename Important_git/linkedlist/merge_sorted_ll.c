#include <stdio.h>
#include <stdlib.h>

typedef struct ListNode {
    int val;
    struct ListNode *next;
}node_t;



struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){

    struct ListNode* head = NULL, *tmp=NULL;
    if(!l1)
        return l2;
    if(!l2)
        return l1;

    if(l1->val < l2->val){
        head = l1;
    }else{
        head = l2;
    }
    while(1){

        if(l1 == NULL || l2 == NULL){
            break;
        }

        //printf("l1=%d,l2=%d\n",l1->val,l2->val);
        //equal case
        if(l1->val == l2->val){
            if(l1->next == NULL && l2->next == NULL){
                l1->next = l2;
                l2->next = l1;
                break;
            }
            if(l2->next == NULL){
                tmp = l2->next;
                l2->next = l1;
                l2 = tmp;
            }else{
                tmp = l2->next;
                l2->next = l1;
                l2 = tmp;
            }
            continue;
        }

        if(l1->val > l2->val){
            //2cases
            //1 next =null
            if(l2->next == NULL){
                tmp = l2->next;
                l2->next = l1;
                l1 = tmp;

            }
            //2 next is bigger
            else if(l2->next->val > l1->val){
                 tmp = l2->next;
                l2->next = l1;
                l1 = tmp;

            }else{
                l2 = l2->next;
            }
            continue;
        }


        if(l2->val > l1->val){
            //2cases
            //1 next =null
            if(l1->next == NULL){
                tmp = l1->next;
                l1->next = l2;
                l2 = tmp;
            }
            //2 next is bigger
            else if(l1->next->val > l2->val){
                 tmp = l1->next;
                l1->next = l2;
                l2 = tmp;
            }else{
                l1 = l1->next;
            }
            continue;
        }

    }

    return head;
}



struct ListNode* mergeTwoLists_obi(struct ListNode* l1, struct ListNode* l2){
  node_t *head=NULL,*cur=NULL;

  if(!l1) return l2;
  if(!l2) return l1;

  if(l1->val<=l2->val){
    head = l1;
    l1=l1->next;
  }else{
    head = l2;
    l2=l2->next;
  }

  cur = head;
  while(l1&&l2){
    //printf("cur->val=%d->",cur->val);
    if(l1->val<=l2->val){
      cur->next = l1;
      l1 = l1->next;
    }else{
      cur->next = l2;
      l2 = l2->next;
    }
    cur=cur->next;
  }

  if(l1){
    cur->next = l1;
  }
  if(l2){
    cur->next = l2;
  }
  return head;
}

struct ListNode* newNode(int data){
	struct ListNode* tmp=NULL;
	tmp = (struct ListNode*)malloc(sizeof(struct ListNode));
	tmp->next = NULL;
	tmp->val = data;
	return tmp;
}

void printLL(struct ListNode* head){
printf("\n");
	while(head){
		printf("%d->",head->val);
		head = head->next;
	}
printf("\n");
}

int main(){
	struct ListNode *head1 = NULL,*head2=NULL;
	//int i=0;

	head1 = newNode(1);
	head1->next = newNode(2);
	head1->next->next = newNode(4);
	printLL(head1);

	head2 = newNode(1);
	head2->next = newNode(3);
	head2->next->next = newNode(4);
	printLL(head2);

	struct ListNode* merged = mergeTwoLists_obi(head1,head2);
	printLL(merged);

  return 0;
}
