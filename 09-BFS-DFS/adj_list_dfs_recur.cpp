#include<iostream>
#include<vector>
#include<deque>
#include<algorithm>

using namespace std;

#define MAX_COST 1000000001

struct vertex{
	int cost;
	vertex(int c){cost = c;}
	vertex(){}
};

class Graph{
	int n; // Number of vertices ≤ 10^5
public: 
	int64_t TC; // total cost;
	vector<vertex> V;
	vector<vector<int> > adj_list;
	void add_edge(pair<int, int> p){ 
        adj_list[p.first-1].push_back(p.second-1);
        adj_list[p.second-1].push_back(p.first-1);
    }
	Graph(int nn);
	void BFS();
	void printV();
	void printE();
	const vector<int> & neighbours(int v);
};

const vector<int> & Graph::neighbours(int v){	
    return adj_list[v];
}

/*vector<int> Graph::neighbours(int v){
	vector<int> neigh;
    for(size_t u = 0; u < n; ++u){
        if(E[v][u]) neigh.push_back(u);
    }
    return neigh;
}*/

void Graph::BFS(){
	deque<int> q;
    vector<bool> touched(n, false);
    for(size_t i = 0; i < n; ++i){
        if(!touched[i]){
            int min_cost = V[i].cost;
            q.push_back(i);
            touched[i] = true;
            while(q.size() > 0){                
                min_cost = min(min_cost, V[q.front()].cost);
                //vector <int> neigh = neighbours(q.front());
                for(auto u : neighbours(q.front())){
                    if(!touched[u]){ q.push_back(u); touched[u] = true;}
                }
                q.pop_front();
            } // EoF BFS
            TC += min_cost;
        }// New connected component
    }
}

Graph::Graph(int nn){
	n = nn;
	TC = 0;	
	V = vector<vertex>(n, vertex());
	adj_list = vector<vector<int> >(n, vector<int>());	
}

void Graph::printV(){
	for(size_t i = 0; i < n; ++i){
		cout << V[i].cost << " ";
	}
	cout << endl << endl;
}

struct DFS{
    Graph *G;
    int n; // num of vertices
    int t; // time
    vector<int> d, f;
    
    int64_t TC; 
    int min_cur;
    
    DFS(Graph * GG){
        G = GG;
        n = G->V.size();
        t = 0;
        f = d = vector<int>(n, 0);
        
        TC = 0;
        min_cur = MAX_COST;
    }
    
    void operator()(){
        for(size_t v = 0; v < n; ++v){
            if(d[v] == 0){
                search(v);
                TC += min_cur;
                min_cur = MAX_COST;
            }
        }
        G->TC = TC;
    }
    
    void search(int v){
        d[v] = ++t;
        min_cur = min(min_cur, G->V[v].cost);
        for(auto u: G->neighbours(v)){
            if(d[u] == 0) search(u);
        }
        f[v] = ++t;
    }
};

int main (int argc, char const *argv[]){
	//freopen("t3", "r", stdin); // open file with test data to reed and acces it through stdin
    std::ios::sync_with_stdio(false); std::cin.tie(0);
	int n, m; // n — V, E — 
	
	cin >> n; cin >> m;
	
	Graph G(n);
	
	for(size_t i = 0; i < n; ++i){
		int cost;
		cin >> cost;
		vertex v(cost);
		G.V[i] = v;
	}
	//G.printV();
	
	for(size_t i = 0; i < m; ++i){
		pair<int, int> p;
		cin >> p.first; cin >> p.second;
		G.add_edge(p);
	}
	//G.printE();	
	
	//G.BFS();
    DFS dfs(&G);
    dfs();
	
	cout << G.TC << "\n";
	
	return 0;
}