#include <iostream>
#include <string>

using namespace std;

struct luat
{
	string trai;
	string phai;
};

string gt;
string kl;

int ktCM(string gt, string kl){
	if (gt.find(kl) != string::npos) 
		return 1;
	else return 0;
}

int kt(string gt, string kl){
	string gtCm = "";
	for(int i = 0; i < kl.length(); i++)
	{
		for(int j = 0; j < gt.length(); j++ )
		{
			if(kl[i] == gt[j])
				gtCm = gtCm + gt[j]; 
		}
	}
	
	if(gtCm == kl || ktCM(gtCm, kl))
	return 1;
	return 0;
}

void xoaPT(luat dsLuat[100], int n, int vt){
	for(int i = vt; i < n-1; i++) {
        dsLuat[i] = dsLuat[i+1];
    }
    n = n-1;
}

int ktXoaLuat(string &gt,luat dsLuat[100], int &n){
	for(int i =1 ; i < n-1; i++)
	{
		if(kt(gt,dsLuat[i].trai) == 1)
		{
			cout<<"\t"<<dsLuat[i].trai<<"->"<<dsLuat[i].phai<<endl;
			gt = gt + dsLuat[i].phai;
			xoaPT(dsLuat,n, i);
			return 1;	
		}
		
	}
	return 0;
}

int ktLuat(string gt,luat dsLuat[100], int n){
	for(int i =1 ; i < n-1; i++)
	{
		if(kt(gt,dsLuat[i].trai) == 1)
		{
			return 1;	
		}
		
	}
	return 0;
}

void suyDienTien(string gt, string kl, luat dsLuat[100], int n){
	string gtCm = gt;
	while(ktLuat(gt, dsLuat, n) != 0)
	{
		if(ktCM(gt, kl) == 1)
		{
			cout<< gtCm << "->"<< kl<< "(dpcm)";
			return;
		}
		
		ktXoaLuat(gt, dsLuat, n);
	}
	if(ktCM(gt, kl) == 1)
	{
		cout<< gtCm << "->"<< kl<< "(dpcm)";
	}
	else {
		cout<<gt;
		cout<<"Tu gia thiet khong the dua ra ket luan";
	}
}

int main()
{
	luat dsLuat[100];
	int soLuat;
	cout<<"Nhap cac luat: "<<endl;
	int n = 1;                   
	do 
	{
		cin>>dsLuat[n].trai;
		cin>>dsLuat[n].phai;
		n++;
	}
	while(dsLuat[n-1].trai !="0" || dsLuat[n-1].phai !="0");
	
	cout<<"Nhap gia thiet: ";
	cin>>gt;
	cout<<"Nhap ket luan: ";
	cin>>kl;
	cout<<"Danh sach cac luat: "<<endl;
	for(int i =1 ; i < n-1; i++)
	{
		cout<<"\t"<< dsLuat[i].trai << "->"<<dsLuat[i].phai<<endl;
	}
	
	cout<<"Ket Qua"<<endl;
	suyDienTien(gt,kl,dsLuat, n);
	
	return 0;
}                             
