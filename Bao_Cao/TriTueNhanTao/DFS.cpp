#include <bits/stdc++.h>
using namespace std;

int n, m; 

//mang vector de luu danh sach ke
vector<int> adj[1001];

// kiem tra mot dinh da duoc tham hay chua
bool visited[1001];

void inp(){
	cin >> n >> m;
	for (int i = 0; i< m; i++)
	{
		int x, y; 
		cin >> x >> y;
		adj[x].push_back(y);
		// co huong thi bo dong nay
		adj[y].push_back(x);
	}
	memset(visited, false, sizeof(visited));
}

void dfs(int u){
	cout << u << " ";;
	//danh dau la u da duoc tham
	visited[u] = true;
	//dung foreach de duyet tung diem ke cua U
	for(int v : adj[u]){
		//veu diem v chua dc tham thi
		if(!visited[v]){
			dfs(v);
		}
	}	
}

int main(){
	inp();
	dfs(1);
}
