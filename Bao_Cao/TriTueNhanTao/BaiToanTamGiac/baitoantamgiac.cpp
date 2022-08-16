#include<iostream>
#include<math.h>
using namespace std;
double a=0,b=0,h=0,c=0;
double S=0,p=0,alpha=0,beta=0,delta=0;
int n =5;
int k[8];//mang kich hoat
int mnn[8][5]={
	-1,0,0,-1,0,
	-1,-1,0,-1,0,
	0,-1,0,-1,0,
	-1,0,-1,0,0,
	-1,-1,-1,0,0,
	0,-1,-1,0,-1,
	0,0,-1,0,-1,
	0,0,0,0,-1
	};
void init_mkh()
{
	//alpha,beta,delta,a,b,c,S,h
	for(int i=0;i<8;i++)
	{
		k[i]=0;
	}
}
void in_mkh()
{
	printf("------mang kich hoat----- \n");
	for(int i=0;i<8;i++)
	{
		printf(" %d",k[i]);
	}
	printf("\n");
}
void init(double alpha,double beta,double delta,double a,double b,double c,double S)
{
	//alpha,beta,delta,a,b,c,S,h
	if(alpha!=0.0)
		k[0]=1;
	if(beta!=0.0)
		k[1]=1;
	if(delta!=0.0)
		k[2]=1;
	if(a!=0.0)
		k[3]=1;
	if(b!=0.0)
		k[4]=1;
	if(c!=0.0)
		k[5]=1;
	if(S!=0.0)
		k[6]=1;
}
void kichhoat(int hang)
{
	for(int i=0;i<n;i++)
	{
		if(mnn[hang][i]!=0)
			mnn[hang][i]=1;
	}
	
}
void in_mnn()
{
	for(int i=0;i<8;i++)
	{
		for(int j=0;j<5;j++)
		{
			printf("\t%d",mnn[i][j]);
		}
		printf("\n");
	}
}
int kiemtra()//tong cot
{
	for(int i=0;i<5;i++)
	{
		int tong1=0;
		int tong_1=0;
		int tong=0;
		for(int j=0;j<8;j++)
		{
			if(mnn[j][i]!=0)
				tong++;
			//hieu giua tong so o co gia tri 1 va tong so o co gia tri -1
			if(mnn[j][i]==1)
				tong1++;
			else if(mnn[j][i]==-1)
				tong_1++;
		}
		if(tong_1==1)//tong so o co gia tri {-1} =1
		{
			// tinh ra
			return i;// cong thuc thu i duoc kich hoat 
		}
	}
}
//cong thuc 1
double congthuc1(double a,double b,double alpha,double beta)
{
	//a/sin(alpha)=b/sin(beta)
	alpha=alpha*3.141592/180;
	beta=beta*3.141592/180;
	if(a==0){
		return (b*sin(alpha))/sin(beta);
	}
	else if(b==0)
	{
		return (a*sin(beta))/sin(alpha);
	}
	else if(alpha==0)
	{
		return asin((a*sin(beta))/b)* 180 / 3.141592;
	}
	else if(beta==0)
	{
		return asin((b*sin(alpha))/a)* 180 / 3.141592;
	}
}
//cong thuc 2
double congthuc2(double b,double c,double beta,double delta)
{
	//c= (b*sin(delta))/sin(beta);
	//b= (c*sin(beta))/sin(delta);
	//delta= ((c*sin(beta))/b) * 180 / 3.141592;
	//beta= ((b*sin(delta))/c) * 180 / 3.141592;
	beta=beta*3.141592/180;
	delta=delta*3.141592/180;
	if(c==0)
	{
		return(b*sin(delta))/sin(beta);	
	}
	else if(b==0)
	{
		return(c*sin(beta))/sin(delta);
	}
	else if(delta==0)
	{
		return ((c*sin(beta))/b) * 180 / 3.141592;
	}
	else if(beta==0)
	{
		return ((b*sin(delta))/c) * 180 / 3.141592;
	}
}
//cong thuc 3
double congthuc3(double a,double b,double c){
	//p=(a+b+c)/2;
	if(a!=0&&b!=0&&c!=0)
	{
		double p=(a+b+c)/2;
		return sqrt(p*(p-a)*(p-b)*(p-c));//S: dien tich
	}
	//S=sqrt(p*(p-a)*(p-b)*(p-c));
	
}
//cong thuc 4
double congthuc4(double alpha,double beta,double delta)
{
	//3goc cong lai =180
	if(alpha==0)
	{
		return 180-beta-delta;
	}
	else if(beta==0)
	{
		return 180-alpha-delta;
	}
	else if(delta==0)
	{
		return 180-alpha-beta;
	}
}
//cong thuc 5
double congthuc5(double S,double h,double c)
{
	//S=0.5*h*c;
	if(S==0){
		return 0.5*h*c;
	}
	else if(h==0)
	{
		return (2*S)/c;
	}
	else if(c==0)
	{
		return (2*S)/h;	
	}
}

int main()
{
	
	printf("--------------Bai toan tam giac-------------\n");
	printf("Nhap vao canh a: ");scanf("%lf",&a);
	printf("Nhap vao canh b: ");scanf("%lf",&b);
	printf("Nhap vao canh c: ");scanf("%lf",&c);
	printf("Nhap vao S: ");scanf("%lf",&S);
	printf("Nhap vao goc alpha: ");scanf("%lf",&alpha);
	printf("Nhap vao goc beta: ");scanf("%lf",&beta);
	printf("Nhap vao goc delta: ");scanf("%lf",&delta);
	init_mkh();
	init(alpha,beta,delta,a,b,c,S);

	//kich hoat cac gia tri da co
	for(int i=0;i<8;i++)
	{
		if(k[i]==1)
		{
			kichhoat(i);
		}
	}
	while(h==0)
	{
		int congthuc=kiemtra();
		switch(congthuc)
		{
			case 0:{

				double kq=congthuc1(a,b,alpha,beta);
		
				for(int i=0;i<8;i++)
				{
					if(mnn[i][congthuc]==-1){
						kichhoat(i);
						switch (i){
							case 3:{
								//a
	
								a=kq;
								break;
							}
							case 4:{
								//b
					
								b=kq;
								break;
							}
							case 0:{
								//alpha
				
								alpha=kq;
								break;
							}
							case 1:{
								//beta
	
								beta=kq;
								break;
							}
						}
					}
				}
				break;
			}
			case 1:{
	
				double kq=congthuc2(b,c,beta,delta);
				for(int i=0;i<8;i++)
				{
					if(mnn[i][congthuc]==-1){
						kichhoat(i);
						switch (i){
							case 5:{
								//c

								c=kq;
								break;
							}
							case 4:{
								//b

								b=kq;
								break;
							}
							case 2:{
								//delta

								delta=kq;
								break;
							}
							case 1:{
								//beta
								beta=kq;
								break;
							}
						}
					}
				}
				break;
			}
			case 2:{
	
				double kq=congthuc3(a,b,c);
				for(int i=0;i<8;i++)
				{
					if(mnn[i][congthuc]==-1){
						kichhoat(i);
						switch (i){
							case 6:{
								//S
						
								S=kq;
								break;
							}
							case 5:{
								//a
				
								a=kq;
								break;
							}
							case 4:{
								//b
			
								b=kq;
								break;
							}
							case 3:{
								//c
			
								c=kq;
								break;
							}
						
						}
					}
				}
				break;
			}
			case 3:{
	
				double kq=congthuc4(alpha,beta,delta);
				for(int i=0;i<8;i++)
				{
					
					if(mnn[i][congthuc]==-1){
						kichhoat(i);
						switch (i){
							case 0:{
								//alpha

								alpha=kq;
								break;
							}
							case 1:{
								//beta

								beta=kq;
								break;
							}
							case 2:{
								//delta
	
								delta=kq;
								break;
							}
							
						
						}
					}
				}
				break;
			}
			case 4:{

				double kq=congthuc5(S,h,c);
				for(int i=0;i<8;i++)
				{
					if(mnn[i][congthuc]==-1){
						kichhoat(i);
						switch (i){
							case 6:{
								//S
				
								S=kq;
								break;
							}
							case 7:{
								//h
		
								h=kq;
								break;
							}
							case 5:{
								//c

								c=kq;
								break;
							}
							
						
						}
					}
				}
				break;
			}
		}
		
	}
		printf("h duoc tinh la %f\n",h);
}
