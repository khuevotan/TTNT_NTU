// Enter the number of villages: 4

// Enter the Cost Matrix

// Enter Elements of Row: 1
// 0 4 1 3

// Enter Elements of Row: 2
// 4 0 2 1

// Enter Elements of Row: 3
// 1 2 0 5

// Enter Elements of Row: 4
// 3 1 5 0
// The cost list is:
// 0 4 1 3
// 4 0 2 1
// 1 2 0 5
// 3 1 5 0

// The Path is:
// 1—>3—>2—>4—>1

// Minimum cost is 7

#include <iostream>

using namespace std;

int ary[10][10], completed[10], n, cost = 0;

void takeInput()
{
    int i, j;

    cout << "Nhap so hang so cot: ";
    cin >> n;

    cout << "\nNhan chi phi cua ma tran\n";

    for (i = 0; i < n; i++)
    {
        cout << "\nNhap cac phan tu cua hang: " << i + 1 << "\n";

        for (j = 0; j < n; j++)
            cin >> ary[i][j];

        completed[i] = 0;
    }

    cout << "\n\nDanh sach chi phi:";

    for (i = 0; i < n; i++)
    {
        cout << "\n";

        for (j = 0; j < n; j++)
            cout << "\t" << ary[i][j];
    }
}

int least(int c)
{
    int i, nc = 999;
    int min = 999, kmin;

    for (i = 0; i < n; i++)
    {
        if ((ary[c][i] != 0) && (completed[i] == 0))
            if (ary[c][i] + ary[i][c] < min)
            {
                min = ary[i][0] + ary[c][i];
                kmin = ary[c][i];
                nc = i;
            }
    }

    if (min != 999)
        cost += kmin;

    return nc;
}

void mincost(int city)
{
    int i, ncity;

    completed[city] = 1;

    cout << city + 1 << "--->";
    ncity = least(city);

    if (ncity == 999)
    {
        ncity = 0;
        cout << ncity + 1;
        cost += ary[city][ncity];

        return;
    }

    mincost(ncity);
}

int main()
{
    takeInput();

    cout << "\n\nThe Path is:\n";
    mincost(0); // passing 0 because starting vertex

    cout << "\n\nGia nho nhat " << cost;

    return 0;
}
