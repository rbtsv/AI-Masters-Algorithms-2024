#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<string>

using namespace std;


int main (int argc, char const *argv[])
{
	set<int> s = {1,3,5,7,9};
	for(auto x: s)
        cout << x << " ";
    cout << endl;
	
	auto x = s.lower_bound(7);
    //auto x = s.upper_bound(7);
	cout << *x;
	return 0;
}