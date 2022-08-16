#include <iostream>
#include <iomanip>
using namespace std;

int main(int argc, char **argv)
{
    int n;
    cout << "nhap so tien can doi: ";
    cin >> n;

    int x = 8;

    cout << "cac cach doi tien co the co" << endl;
    cout << setw(x) << "500000" << setw(x) << "200000" << setw(x) << "100000" << setw(x) << "50000" << setw(x) << "20000" << setw(x) << "10000" << setw(x) << "5000" << setw(x) << "2000" << setw(x) << "1000" << endl;
    for (int x1 = 0; x1 <= n / 500000; x1++)
    {
        for (int x2 = 0; x2 <= n / 200000; x2++)
        {
            for (int x3 = 0; x3 <= n / 100000; x3++)
            {
                for (int x4 = 0; x4 <= n / 50000; x4++)
                {
                    for (int x5 = 0; x5 <= n / 20000; x5++)
                    {
                        for (int x6 = 0; x6 <= n / 10000; x6++)
                        {
                            for (int x7 = 0; x7 <= n / 5000; x7++)
                            {
                                for (int x8 = 0; x8 <= n / 2000; x8++)
                                {
                                    for (int x9 = 0; x9 <= n / 1000; x9++)
                                    {
                                        if (500000 * x1 + 200000 * x2 + 100000 * x3 + 50000 * x4 + 20000 * x5 + 10000 * x6 + 5000 * x7 + 2000 * x8 + 1000 * x9 == n)
                                        {
                                            cout << setw(x) << x1 << setw(x) << x2 << setw(x) << x3 << setw(x) << x4 << setw(x) << x5 << setw(x) << x6 << setw(x) << x7 << setw(x) << x8 << setw(x) << x9 << endl;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}