#include <iostream>
#include <string.h>
#include <fstream>
#include <list>
#include <iterator>
using namespace std;
fstream f("robinson.txt",ios::in);
list<string> listGT;
list<string> listKL;
list<string> listMD;
void ChuanHoa()
{
	string s;
	getline(f, s, '>');
	s.insert(s.size(),"^");
	while(!s.empty())
	{
		listGT.push_back(s.substr(0, s.find("^")));
		s.erase(0,s.find("^")+1);
	}
	getline(f,s);
	s.insert(s.size(),"v");
	while(!s.empty())
	{
		listKL.push_back(s.substr(0, s.find("v")));
		s.erase(0,s.find("v")+1);
	}
	
	
	cout<<"Chuan hoa: ";
	list<string> :: iterator it;
	string tam;
	for (it = listGT.begin(); it != listGT.end(); ++it)
	{
		tam.insert(tam.size(),*it);
		tam.insert(tam.size()," ^ ");
	}
	tam.erase(tam.size()-2,tam.size());
	tam.insert(tam.size()," => ");
	for (it = listKL.begin(); it != listKL.end(); ++it)
	{
		tam.insert(tam.size(),*it);
		tam.insert(tam.size()," v ");
	}
	tam.erase(tam.size()-2,tam.size());
	cout<<tam<<endl<<endl;
	
	
	for (int i = 0; i < listKL.size(); i++)
	{
		string tam;
		if (listKL.front().size() == 2)
			tam = listKL.front().erase(0,1);
		else
			if (listKL.front().size() == 1)
				tam = listKL.front().insert(0,"-");
		listKL.pop_front();
		listKL.push_back(tam);
	}
	listMD = listGT;
	list<string> list2 = listKL;
	listMD.merge(list2);
}
bool KTDoiNgau (string s1, string s2)
{
	if (s1.size() > s2.size())
	{
		s1.erase(0,1);
		if (s1.compare(s2) == 0)
			return true;
	}
	else
	if (s1.size() < s2.size())
	{
		s2.erase(0,1);
		if (s1.compare(s2) == 0)
			return true;
	}
	return false;
}
bool KTDoiNgayDS()
{
	list<string> listTam = listMD;
	list<string> :: iterator it;
	list<string> :: iterator ot;
	for (it = listMD.begin(); it != listMD.end(); ++it)
	{
		string s1 = *it;
		listTam.pop_front();
		for (ot = listTam.begin(); ot != listTam.end(); ++ot)
		{
			string s2 = *ot;
			if (KTDoiNgau(s1,s2) == true)
			{
				cout<<endl<<"Tim thay 2 menh de doi ngau trong danh sach {"<<s1<<" , "<<s2<<"}"<<endl;
				return true;
			}	
		}
	}
	return false;
}
string HopGiai1 (string s1, string s2)	/*x ^ (-x v y) => y*/
{
	string s = s2;
	string tam1, tam2;
	tam1 = s.substr(1,s.find("v")-1);
	s.erase(0,s.find("v")+1);
	tam2 = s.substr(0,s.find(")"));
	if (KTDoiNgau(s1,tam1))
		return tam2;
	if (KTDoiNgau(s1,tam2))
		return tam1;
	return s2;
}
string HopGiai2 (string s1, string s2)	/*(x v y) ^ (-x v z) => (y v z)*/
{
	string tam1 = s1, tam2 = s2;
	string tam1a, tam1b;
	string tam2a, tam2b;
	tam1a = tam1.substr(1,tam1.find("v")-1);
	tam1.erase(0,tam1.find("v")+1);
	tam1b = tam1.substr(0,tam1.find(")"));
	
	tam2a = tam2.substr(1,tam2.find("v")-1);
	tam2.erase(0,tam2.find("v")+1);
	tam2b = tam2.substr(0,tam2.find(")"));
	
	string s;
	if (KTDoiNgau(tam1a,tam2a) == true)
	{
		s.insert(s.size(),"(");
		s.insert(s.size(),tam1b);
		s.insert(s.size(),"v");
		s.insert(s.size(),tam2b);
		s.insert(s.size(),")");
		return s;
	}
	if (KTDoiNgau(tam1a,tam2b) == true)
	{
		s.insert(s.size(),"(");
		s.insert(s.size(),tam1b);
		s.insert(s.size(),"v");
		s.insert(s.size(),tam2a);
		s.insert(s.size(),")");
		return s;
	}
	if (KTDoiNgau(tam1b,tam2a) == true)
	{
		s.insert(s.size(),"(");
		s.insert(s.size(),tam1a);
		s.insert(s.size(),"v");
		s.insert(s.size(),tam2b);
		s.insert(s.size(),")");
		return s;
	}
	if (KTDoiNgau(tam1b,tam2b) == true)
	{
		s.insert(s.size(),"(");
		s.insert(s.size(),tam1a);
		s.insert(s.size(),"v");
		s.insert(s.size(),tam2a);
		s.insert(s.size(),")");
		return s;
	}
	
	s.insert(s.size(),"Khong the hop giai");
	return s;
}
void InTapMD()
{
	list<string> :: iterator it;
	string s;
	s.insert(s.size(),"{ ");
	for (it = listMD.begin(); it != listMD.end(); ++it)
	{
		s.insert(s.size(),*it);
		s.insert(s.size()," , ");
	}
	s.erase(s.size()-2,s.size());
	s.insert(s.size(),"}");
	cout<<"Tap menh de = ";
	cout<<s<<endl<<endl;
		
}
void ChenDSLuu (list<string> &ds, list<string> save)
{
	list<string> :: iterator st;
	for (st = save.begin(); st != save.end(); ++st)
		ds.push_front(*st);
		
}
bool Robinson()
{
	list<string> listTam = listMD;
	list<string> :: iterator it;
	list<string> :: iterator ot;
	int flag = 0;
	list<string> save;	
start: for (it = listMD.begin(); it != listMD.end(); ++it)
	{		
		if (KTDoiNgayDS() == true)
		{
			flag = 1;
			break;
		}			
		string s1 = *it;
		listTam.pop_front();
		for (ot = listTam.begin(); ot != listTam.end(); ++ot)
		{	
			string s2 = *ot;
			string s;
			if (s1.size() <= 2 && s2.size() > 2)
			{
				s = HopGiai1(s1,s2);
				if (s.size() <= 2)
				{
					listMD.remove(s1);
					listMD.remove(s2);
					listTam.remove(s2);
					listMD.push_back(s);
					listTam.push_back(s);
					cout<<s1<<" ^ "<<s2<<" => "<<s<<endl;					
					InTapMD();
					cout<<endl;
					if (save.empty() == false)
						ChenDSLuu(listTam,save);
					goto start;
				}
			}
			else if (s1.size() > 2 && s2.size() <= 2)
			{
				s = HopGiai1(s2,s1);
				if (s.size() <= 2)
				{
					listMD.remove(s1);
					listMD.remove(s2);
					listTam.remove(s2);
					listMD.push_back(s);
					listTam.push_back(s);
					cout<<s1<<" ^ "<<s2<<" => "<<s<<endl;
					InTapMD();
					cout<<endl;
					if (save.empty() == false)
						ChenDSLuu(listTam,save);
					goto start;
				}
			}
			else if (s1.size() > 2 && s2.size() > 2)
			{
				s = HopGiai2(s1,s2);
				if (s.size() <= 7)
				{
					listMD.remove(s1);
					listMD.remove(s2);
					listTam.remove(s2);
					listMD.push_back(s);
					listTam.push_back(s);
					cout<<s1<<" ^ "<<s2<<" => "<<s<<endl;
					InTapMD();
					cout<<endl;
					if (save.empty() == false)
						ChenDSLuu(listTam,save);
					goto start;
				}
			}			
		}
		save.push_front(s1);
	}
	if (flag == 1)
		return true;
	else
		return false;	
}

int main()
{
	ChuanHoa();
	InTapMD();
	if (Robinson() == true)
		cout<<"Van de duoc chung minh";
	else
		cout<<endl<<"Van de khong duoc chung minh";
}

