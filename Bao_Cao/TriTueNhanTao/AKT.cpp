#include <stdio.h>
#include<conio.h>
#include<math.h>

int a[3][3]={ {2,8,3},{1,6,4},{7,0,5} };
int A[3][3]={ {1,2,3},{8,0,4},{7,6,5} };
int b[3][3]={ {2,8,3},{1,6,4},{7,0,5} };

int I,J,I1,J1,g=0,h;
void xuly();
int ketthuc();
int tinh();
int tim(int );
void timdinhtrong();
void swap(int & , int &);
void xetchon();
void chep1();
void chep2();

int main()
{// clrscr();
	xuly();
	printf("\n So buoc lap la : %d",g);
	getch();
}

void xuly(){
	while(!ketthuc())
	{
		g++;
		xetchon();
		printf("%d \n",h);
		for(int i=0; i<3; i++)
		{
			for(int j=0; j<3; j++)
				printf("%d ",a[i][j]);printf("\n");
		}
		getch();
	}
}

int ketthuc()
{
	for(int i=0;i<3;i++)
		for(int j=0;j<3;j++)
			if (a[i][j]!=A[i][j])
			return 0;
	return 1;
}

int tinh()
{
	int bac=0;
	for(int i=0;i<3;i++)
		for(int j=0;j<3;j++)
		{
			if(tim(b[i][j]))
			bac+=abs(I1-i)+abs(J1-j);
		}
	return bac;
}

int tim(int x)
{
	for(int i=0;i<3;i++)
		for(int j=0;j<3;j++)
			if (A[i][j]==x && x!=0 )
			{
				I1=i;
				J1=j;
				return 1;
			}
	return 0;
}

void timdinhtrong()
{
	for(int i=0;i<3;i++)
		for(int j=0;j<3;j++)
			if (a[i][j]==0)
			{
				I=i;J=j;
			}
}

void swap( int &x , int &y)
{
	int temp;
	temp=x;
	x=y;
	y=temp;
}

void xetchon()
{
	int min=100;
	timdinhtrong();
	for(int j=0;j<3;j++)
	for(int l=0;l<3;l++)
	{
		if ((abs(I-j)+(abs(J-l))==1))
		{
			swap(b[j][l],b[I][J]);
			h=tinh();
			if( h<min )
			{
				min=h;
				chep2();
			}
			swap(b[j][l],b[I][J]);
		}
	}
	chep1();
	h=min;
}

void chep1()
{
	for(int i=0;i<3;i++)
		for(int j=0;j<3;j++)
			b[i][j]=a[i][j];
}

void chep2()
{
	for(int i=0;i<3;i++)
		for(int j=0;j<3;j++)
			a[i][j]=b[i][j];
}
