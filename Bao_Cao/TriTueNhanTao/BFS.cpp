#include <bits/stdc++.h>
using namespace std;

int n,m;

// mang vecto de luu danh sach ke
vector<int> adj[1001];

// nhap input va chuyen thanh ds ke
bool visited[1001];

void inp(){
	cin >> n >> m;
	for(int i=0; i<m; i++){
		int x, y;
		cin >> x >> y;
		adj[x].push_back(y);
		adj[y].push_back(x);
	}
	memset(visited, false, sizeof(visited));
	
}

void bfs(int u){
	// Buoc khoi tao
	queue<int> q;
	q.push(u);
	visited[u] = true;
	
	// Buoc Lap
	while(!q.empty()){
		// lay dinh o dau hang doi
		int v = q.front();
		// lay ra va xoa no di
		q.pop();
		cout << v << " ";
		for(int x : adj[v]){
			//visited[x] == false
			if(!visited[x]){
				q.push(x);
				visited[x] = true;
			}
		}
	}	
}

int main(){
	inp();
	bfs(1);
	return 0;
}

