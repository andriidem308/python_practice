#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;

class deque{
private:
	struct node{
		int data;
		node *next, *prev;
		node(){ prev = next = NULL;}
		node(int a){data = a; prev = next = NULL; }
	} *FRONT, *BACK;
public:
	deque(){FRONT = BACK = NULL; }

	void push_back(int a){
		node *p = new node(a);
		if(FRONT == NULL) FRONT = BACK = p;
		else {
			p->prev = BACK;
			p->next = NULL;
			BACK->next = p;
			BACK = p;
		}
	}

	void push_front(int a){
		node *p = new node(a);
		if(FRONT == NULL)
			FRONT = BACK = p;
		else{
			p->next = FRONT;
			p->prev = NULL;
			FRONT->prev = p;
			FRONT = p;
		}
	}

	int pop_front(void){
		node *p = FRONT;
		int r = FRONT->data;
		if(FRONT == BACK)
			FRONT = BACK = NULL;
		else {
			FRONT = FRONT->next;
			FRONT->prev = NULL;
		}
		delete p;
		return r;
	}

	int pop_back(void){
		node *p = BACK;
		int r = BACK->data;
		if(FRONT == BACK) FRONT = BACK = NULL;
		else{
			BACK = BACK->prev;
			BACK->next = NULL;
		}

		delete p;

		return r;
	}

	int empty(void){return FRONT == NULL;}
	int front(void){return FRONT->data;}
	int back(void){return BACK->data;}
};

#define MAX 150001
deque q[MAX];

int main(){
	int n;
	int a, b;
	char s[100];

	scanf("%d\n",&n);
	while(n--){
		scanf("%s %d", s, &a);

		if(!strcmp(s,"pushback")){
			scanf("%d\n",&b);
			q[a].push_back(b);
		}

		if(!strcmp(s,"pushfront")){
			scanf("%d\n",&b);
			q[a].push_front(b);
		}

		if(!strcmp(s,"popfront")){
			scanf("\n");
			printf("%d\n",q[a].front());
			q[a].pop_front() ;
		}

		if(!strcmp(s,"popback")){
			scanf("\n");
			printf("%d\n",q[a].back());
			q[a].pop_back();
		}
	}
}