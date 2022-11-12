#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main() {
   int n,a;
   cin>>n;
   for(int i=0;i>a;
  vector b;
  for(int i=1; i <= a; i++) {
   if (a % i == 0){
    b.push_back(i);
   }
  }
  
  for (auto i = b.begin(); i != b.end(); ++i)
   {
    int temp=*i;    
    int m=*i;   
    int r,sum = 0; 
    while(m>0)    
     {    
     r=m%10;    
     sum=(sum*10)+r;    
     m=m/10;    
     }    
    if(temp==sum){
     count++;
    }
   }
        
  cout<<"Case #"<
}