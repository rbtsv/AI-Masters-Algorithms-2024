#include <iostream>
#include <algorithm>

int main (){
    freopen("tm2", "r", stdin);
    std::ios::sync_with_stdio(false); std::cin.tie(0);
    int64_t n, a, b, m1, m2;
    std::cin >> n >> a >> b;
    m1 = std::max(a,b);
    m2 = std::min(a,b);
        
    for(int i = 2; i < n; ++i){ // ++i == i += 1 == (i = i + 1)
        int64_t a;
        std::cin >> a;        
        if( a > m1){
            m2 = m1;
            m1 = a;
        }else{
            m2 = std::max(m2, a);
        }
    }    
    std::cout << m1 * m2 << "\n";    
    return 0;
}