#include<iostream>
#include<vector>

using namespace std;

void print_anything(void * any){
	//int* thing = (int*) any; 
	cout << "any:" << *((int*) any) << endl;
}

void int_p_anything(int *any){
	//int* thing = (int*) any; 
	cout << "any:" << *any << endl;
}


template <typename C> void p_anything(C *any){
	//int* thing = (int*) any; 
	cout << "any:" << *any << endl;
}

// -> 


bool is_greater(vector<int> x, vector<int> y){ // x и y будут скопированны
    return x < y;
}

bool is_greater(vector<int> & x, vector<int> & y){ // при изменении x и y их оригиналы изменятся
    return x < y;
}

bool is_greater(const vector<int> & x, const vector<int> & y){ // оригиналы x и y не изменятся
    return x < y;
}



int main (int argc, char const *argv[]){
	int x, y, *px, * py;
    int &lx = x;
    const int &ly = y;
    
    x = 7;
    y = -1;
    
    cout << y << " " << ly << endl;
    x = 6;
    cout << x << " " << lx << endl;
    y = 5;
    cout << y << " " << ly << endl;
    lx = 4;
    cout << x << " " << lx << endl;
    //ly = 4; // Error
    cout << y << " " << ly << endl;
    px = &x;
    cout << x << " " << lx  << " " << *px << endl;
    *px -= 1;
    cout << x << " " << lx  << " " << *px << endl;
    px = &y;
    cout << x << " " << lx  << " " << *px << endl;    
    
    py = &x;
    px = py;
    cout << x << " " << lx  << " " << *px << endl;    
    
    
    vector<int> vx{1,2,3}, vy;
    vy = vx; // vy is a copy of vx
    
                    
    
    int **ppx; // int * — pointer to int; int ** — pointer to (int *)
    ppx = &px;
    
    cout << **ppx << endl;
    
    print_anything(px);
    p_anything<int>(&y);
        
	//system("open link-pointer.jpeg");
	//system("open pointer-pointer.jpeg");
	//system("open int_star.jpeg");
	//system("open void_star.jpeg"); 	
    return 0;		
}    