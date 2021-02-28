#include <iostream>
using namespace std;

void value(int b)
{
	b=2;
	cout<<b<<endl;
 } 
int main()
{
    int a=1;
    cout<<a<<endl;
    value(a);
    cout<<a<<endl;
    return 0;  
    
}
