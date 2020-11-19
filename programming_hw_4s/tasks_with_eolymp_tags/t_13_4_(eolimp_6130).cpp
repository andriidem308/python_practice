#include <iostream>
#include <string>
using namespace std;

struct Node{
	int value;
	Node *next, *prev;
};

struct deque{
	Node *head=nullptr;
	Node *tail=nullptr;
	int count=0;
	void push_back(int num){
		Node* element=new Node;
		element->value=num;
		count++;
		if(!head){
			head=element;
			tail=head;
		}
		else{
			element->prev=tail;
			tail->next=element;
			tail=element;
		}
		cout<<"ok"<<endl;
	}
	void push_front(int num){
		Node *element=new Node;
		element->value=num;
		count++;
		if(!head){
			head=element;
			tail=head;
		}
		else{
			element->next=head;
			head->prev=element;
			head=element;
		}
		cout<<"ok"<<endl;
	}
	void pop_back(){
		if(count!=0){
			cout<<tail->value<<endl;
			if(count>1){
				Node *element=tail;
				tail=tail->prev;
				tail->next=nullptr;
				delete element;
				count--;
			}
			else{
				head=tail=0;
				count--;
			}
		}
		else cout<<"error"<<endl;
	}
	void pop_front(){
		if(count!=0){
			cout<<head->value<<endl;
			if(head->next){
				Node *element=head;
				head=head->next;
				head->prev=nullptr;
				delete element;
				count--;
			}
			else if(head==tail){
				head->next=nullptr;
				head=nullptr;
				delete head;
				count=0;
			}
		}
		else cout<<"error"<<endl;
	}
	void back(){
		if(count!=0)cout<<tail->value<<endl;
		else cout<<"error"<<endl;
	}
	void front(){
		if(count!=0)cout<<head->value<<endl;
		else cout<<"error"<<endl;
	}
	void size(){
		cout<<count<<endl;
	}
	void clear(){
		count=0;
		cout<<"ok"<<endl;
		while(head)
		{
			tail=head->next;
			delete head;
			head=tail;
		}
	}
	void exit(){
		cout<<"bye";
	}
};

int main() {
	deque deq;
	string str;
	while(cin>>str){
		if(str=="push_front"){
			int num;
			cin>>num;
			deq.push_front(num);
		}
		if(str=="push_back"){
			int num;
			cin>>num;
			deq.push_back(num);
		}
		if(str=="pop_front")deq.pop_front();
		if(str=="pop_back")deq.pop_back();
		if(str=="clear")deq.clear();
		if(str=="size")deq.size();
		if(str=="front")deq.front();
		if(str=="back")deq.back();
		if(str=="exit"){
			deq.exit();
			break;
		}
	}
	return 0;
}