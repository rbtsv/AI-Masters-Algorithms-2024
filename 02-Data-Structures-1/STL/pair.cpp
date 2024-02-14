#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<algorithm>

using namespace std;

struct CmpSecond{
    bool operator( ) (const pair<string, int> x, const pair<string, int> y) const{
        if( x.second < y.second ) return true;
        if( x.second > y.second ) return false;
        return x.first < y.first;
    }
};

int main (int argc, char const *argv[]){
	std::pair<int, int> p1, p2;
    p1 = make_pair(1, 2);
    p2 = {2, 3};    
	
    cout << p1.first << " " << p1.second << endl;
    cout << (p1 < p2) << endl; // false == 0, true == не 0
    cout << (p1 < make_pair(0, 3)) << endl; // false == 0, true == не 0
    
    int a,b;
    tie(a, b) = p2;
    cout << a << " " << b << endl;
    		
            
	//return 0;
    cout << "===\n";
    
    std::less<int> _less;
    cout << _less(1,2) << " " << _less(2, 1) << " " << _less(1, 1) << endl;
    
    vector<pair<string, int> > vsi {make_pair("Z", 17), make_pair("C", 10),
    make_pair("A", 13), make_pair("B", 13), make_pair("A", 1)};
    
    for(auto [s, i] : vsi){
        cout << s << ": " << i << "; ";
    }cout << endl;
    
    std::sort(vsi.begin(), vsi.end());
    for(auto [s, i] : vsi){
        cout << s << ": " << i << "; ";
    }cout << endl;
    
    std::sort(vsi.begin(), vsi.end(), std::greater<pair<string, int> >());
    for(auto [s, i] : vsi){
        cout << s << ": " << i << "; ";
    }cout << endl;
    
    std::sort(vsi.begin(), vsi.end(), CmpSecond());
    for(auto [s, i] : vsi){
        cout << s << ": " << i << "; ";
    }cout << endl;
    
    make_heap(vsi.begin(), vsi.end(), CmpSecond());
    for(auto [s, i] : vsi){
        cout << s << ": " << i << "; ";
    }cout << endl;
    
    
    
}