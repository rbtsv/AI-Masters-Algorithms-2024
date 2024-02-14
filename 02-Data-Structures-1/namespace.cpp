#include<iostream>
#include<vector>


using std::cout, std::endl;
// using namespace std; Not recommended

namespace One{
    int first;
    int second;
    struct int_pair{
        int first;
        int second;
    };
    
}

namespace Two{
    int first;
    int second;
    struct int_pair{
        bool flag;
        int first;
        int second;
    };
    
}

//using namespace Two;

using Two::int_pair;
using One::first;

int main (){
    //One::first = 1;
    first = 1;
    Two::first = 3;
    
    cout << "One::first == " << One::first << " Two::first == " << Two::first << endl;
    
    int_pair p, p2, p3;
    
    p.first = 1; p.second = 7;
    p2.first = -1; p3.second = -7;
    
    cout << p.first << " " << p.second << " " << p.flag << endl;
    
    
    return 0;
    
	int x=7, vector = 5;
    for(size_t i = 0; i < 5; ++i){
        int x = i;
        cout << x << " ";
    }
	cout << endl << "x from main: " << x << endl;
    
    std::vector<int> v = {1,2,3};
    cout  << vector << " " << v[0] << endl;	
    
	return 0;	
}