#include<iostream>
#include<string>

using namespace std;

struct list_item{
    string key;
    int val;
    list_item * next;
    list_item * prev;
    list_item(){};
    list_item(string k, int v): key{k}, val{v}, next{0}, prev{0} {};
};

class List{
    list_item *left;
    list_item *right;
public:
    List(){left=0; right=0;};
    List(list_item * li);
    ~List();
    list_item * lbegin(){return left;}
    list_item * rbegin(){return right;}
    void insert_after(list_item * li, list_item * x);
    void delete_at(list_item * li);
    void print_list(){
        cout << endl;
        for(list_item * li = left; li != 0; li = li->next){
            cout <<  "(" << li->key << ", " << li->val <<  ") ";
        }cout << endl;
     }
};

List::List(list_item * li){left = li; right = li;}

List::~List(){
    for(list_item * li = left; li != 0;){
        list_item * _next = li->next;
        delete li;
        li = _next;
    }
}

void List::insert_after(list_item * li, list_item * x){
    if(li == 0 && left == 0){
        left = x;
        right = x;
        return;
    }
    // li -> li_old_next  => li -> x -> li_old_next
    list_item * li_old_next = li->next;
    li->next = x;
    x->prev = li;
    x->next = li_old_next;
    if(li == right) right = x; // li_old_next == 0
    else li_old_next->prev = x;      
}

void List::delete_at(list_item * li){
    // li_prev -> li -> li_next => li_prev -> li_next
    list_item * li_prev=li->prev, * li_next=li->next;
    if(li == left){
        left = li_next;
    }else{
        li_prev->next = li_next;
    }
    if(li == right){
        right = li_prev;
    }else{
        li_next->prev = li_prev;
    }
    delete li;
}


int main (int argc, char const *argv[]){
    list_item * l0, * l1, * l2, * l3;

    l0 = new list_item("k0", 0);
    l1 = new list_item("k1", 1);
    l2 = new list_item("k2", 2);    
    l3 = new list_item("k3", 3);    
        
    List initially_empty_list, my_list(l1);
         
    initially_empty_list.insert_after(initially_empty_list.lbegin(), l0);
         
    cout << initially_empty_list.lbegin()->key << " " << initially_empty_list.rbegin()->key;

         
    my_list.insert_after(l1, l2);
    my_list.insert_after(l2, l3);
    my_list.print_list();
        
         
    my_list.delete_at(l2);
    my_list.print_list();
         
         
    cout << "l3->prev: " << l3->prev->key << endl; 
    cout << "l3->next: " << l3->next << endl; 
         
    cout << "l3 == right ? " << (l3 == my_list.rbegin()) << " " << my_list.rbegin()->key << endl; 

    my_list.print_list();
    my_list.delete_at(l3);
    my_list.print_list();
    
    my_list.delete_at(l1);
    my_list.print_list();
    cout << "There should have been an empty list";
    
    
    l1 = new list_item("k1'", 1);
    l2 = new list_item("k2'", 2);    
    l3 = new list_item("k3'", 3);
    my_list.insert_after(0, l1);
    my_list.insert_after(l1, l2);
    my_list.insert_after(l2, l3);
    my_list.print_list();
    
    my_list.delete_at(l1);
    my_list.print_list();
    
    list_item * l25 = new list_item("k2.5", 25);    
    my_list.insert_after(l2, l25); 
    my_list.print_list();

    
    return 0;
}