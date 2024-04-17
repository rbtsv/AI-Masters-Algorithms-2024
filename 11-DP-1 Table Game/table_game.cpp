#include<iostream>
#include<algorithm>
#include<vector>

#define DEBUG true

#define Next 1
#define Prev 0

using namespace std;

template<class C> void pr_2d_xy_vec(const vector<C> &field){ 
	int N = field.size() -1;
	for(int j = N; j >= 0; --j){
		for(size_t i = 0; i <= N; ++i){
						cout << field[i][j] <<  " ";
		}
		cout << endl;
	}
	
}
	
struct Sol{
	int N, M;
	long Rsq;	
	const vector<pair<int,int> > & moves;	
	
	/* Sol(int NN, int RR, int MM, long RRsq, const vector<pair<int,int> > * mmoves){
		N = NN; R= RR; M = MM; Rsq = RRsq; pmoves = mmoves;
	}*/
	
	Sol(int NN,  int MM, long RRsq, const vector<pair<int,int> > & mmoves) :
			N{NN},  M{MM}, Rsq{RRsq}, moves(mmoves) {}
	
	bool operator ()(){ return comp_pos(0,0); }
	
	virtual bool comp_pos(int x, int y) = 0;
    /*{
		cout << "Wrong Function!" << endl;
		return Prev; // remove
	}*/
	
};

struct RecursiveSol : public Sol{
	
	using Sol::Sol;
	
    //bool operator ()(){ return comp_pos(0,0); } // Thanks to virtual comp_pos
    
	bool comp_pos(int x, int y){
        if(x*x + y*y >= Rsq) return Prev;
        for(auto [xx, yy] : moves){
            if(x + xx <= N && y + yy <= N && comp_pos(x+xx, y+yy) == Prev)
                return Next;
        }
        return Prev;
	}	
};


struct DPsol{
	int N, M;
	long Rsq;	
	const vector<pair<int,int> > & moves;	
    vector<vector<bool> > & field;
    vector<vector<bool> > & computed;
	
	
	DPsol(int NN,  int MM, long RRsq, const vector<pair<int,int> > & mmoves,
          vector<vector<bool> > & ffield, vector<vector<bool> > & ccomputed) :
		  N{NN},  M{MM}, Rsq{RRsq}, moves(mmoves), field(ffield), computed(ccomputed) {}
	
	bool operator ()(){ return comp_pos(0,0); }
    
	bool comp_pos(int x, int y){
        if (computed[x][y]) return field[x][y];
        field[x][y] = Prev;
        
        if(x*x + y*y < Rsq){
            for(auto [xx, yy] : moves){
                if(x + xx <= N && y + yy <= N && comp_pos(x+xx, y+yy) == Prev){
                    field[x][y] =  Next;
                    break;
                }
            }
        }
        computed[x][y] = true;
        return field[x][y];
	}
};


int main (int argc, char const *argv[]){
	std::ios::sync_with_stdio(false); std::cin.tie(0);
	if(DEBUG) freopen("./tests/1", "r", stdin);
		
	int N, R, M;
	cin >> N >> R >> M;
	long Rsq = R*R;
	
	// 0 == Prev, 1 == Next 
	
	vector<pair<int, int> > moves;
	for(size_t i = 0; i < M; ++i){
		int x, y;		
		cin >> x >> y;
		//if(DEBUG) cout << x << ", " << y << endl;
		moves.emplace_back(x, y);
	}
	

	RecursiveSol rec_sol(N, M, Rsq, moves);
    if(DEBUG) cout << ((rec_sol() == Prev) ?  "2\n" : "1\n");
    
    
    if(DEBUG){
        	vector<vector<bool> > field = vector<vector<bool> >(N+1, vector<bool>(N+1, 0)); 
        	vector<vector<bool> > computed = vector<vector<bool> >(N+1, vector<bool>(N+1, 0));
    
        	DPsol dp_sol(N, M, Rsq, moves, field, computed);
        	cout << ((dp_sol() == Prev) ?  "2\n" : "1\n");			
	    
    		cout << "Dp sol field:\n";
    		pr_2d_xy_vec(dp_sol.field);
    		cout << "\n";
    		cout << "Dp sol computed:\n";
    		pr_2d_xy_vec(dp_sol.computed);
    }

    vector<vector<bool> > field = vector<vector<bool> >(N+1, vector<bool>(N+1, 0)); 
    for(int d = 2*N; d >= 0; --d){        
        for(int y = min(d, N), x = d - y; x <= N && y >= 0; ++x, --y){
            field[x][y] = Prev;        
            if(x*x + y*y < Rsq){
                for(auto [xx, yy] : moves){
                    if(x + xx <= N && y + yy <= N && field[x+xx][y+yy] == Prev){
                        field[x][y] =  Next;
                        break;
                    }
                }
            }
        }
    }
    
	cout << ((field[0][0] == Prev) ?  "2\n" : "1\n");					   
		
	cout << "Dp bottom-up sol field:\n";
	pr_2d_xy_vec(field);	
	
	return 0;
}