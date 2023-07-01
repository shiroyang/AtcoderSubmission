#include<bits/stdc++.h>
using namespace std;

const int MAX = 510;
int H, W;
string grid[MAX];
bool visited[MAX][MAX][5];
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};
string pattern = "snuke";

struct State {
    int x, y, idx;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> H >> W;
    for (int i = 0; i < H; i++) cin >> grid[i];
    
    queue<State> q;
    q.push({0, 0, 0});
    visited[0][0][0] = true;

    while(!q.empty()){
        State cur = q.front();
        q.pop();

        if(cur.x == H - 1 && cur.y == W - 1){
            cout << "Yes\n";
            return 0;
        }

        for(int i = 0; i < 4; i++){
            int nx = cur.x + dx[i];
            int ny = cur.y + dy[i];
            int nidx = (cur.idx + 1) % 5;
            if(nx < 0 || nx >= H || ny < 0 || ny >= W) continue;
            if(visited[nx][ny][nidx]) continue;
            if(grid[nx][ny] != pattern[nidx]) continue;
            visited[nx][ny][nidx] = true;
            q.push({nx, ny, nidx});
        }
    }

    cout << "No\n";
    return 0;
}
