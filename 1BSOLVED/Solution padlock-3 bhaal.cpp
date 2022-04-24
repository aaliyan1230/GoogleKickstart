#include <bits/stdc++.h>
using namespace std;

#define int long long 

#define pb push_back

#define el "\n"
const int mod = 1e9 + 7;


bool mycmp(pair<int,int>p1,pair<int,int>p2){
   if(p1.second>p2.second)
   return true;
  else
        return false;
    }

    pair<int,int> connections[8] ={{1,0},{-1,0},{0,1},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}};

void removeDupWord(string &str,vector<string>&ans)
{
    string word = "";
    for (auto x : str) 
    {
        if (x == ' ')
        {
            ans.pb(word);
            word = "";
        }
        else {
            word = word + x;
        }
    }
    ans.pb(word);
}
bool rev[1003][1003];

int factor_2(int ele){
   int factor=0;
  while(ele%2==0){
        factor++;
        ele/=2;
  }
  return factor;
}

int factor_5(int ele){
   int factor=0;
  while(ele%5==0){
        factor++;
        ele/=5;
  }
  return factor;
}

pair<int,int> min_pair(pair<int,int>p1,pair<int,int>p2)
{

  pair<int,int>ans={1e15,1e15};

    if(min(p1.first,p1.second)==min(p2.first,p2.second)){
        if(p1.first+p1.second>p2.first+p2.second)
         ans={p2.first,p2.second};
        else if(p1.first+p1.second<p2.first+p2.second)
         ans={p1.first,p1.second};
        else{
           //rev[][]=1;
          ans={p1.first,p1.second};
        }
      }

      else if(min(p1.first,p1.second)>min(p2.first,p2.second))
       ans={p2.first,p2.second};
      else
        ans={p1.first,p1.second};

      return ans;

}


 
// Calculate all
// divisors of number
void sieve(int ele,vector<int>&vip)
{
    for (int i = 1; i*i <= ele; i++) {
        if( ele%i==0)
        {
            if(ele==i*i)
                vip.pb(i);
            else{
                vip.pb(i);
                vip.pb(ele/i);
            }


        }
    }
}
 


int isValid(int n){
    vector<int>vola;
    while(n!=0){
          vola.pb(n%10);
          n/=10;
    }
    int i=0,j=vola.size()-1;
    while(i<j)
    {
        if(vola[i]!=vola[j])
            return 0;

        i++;
        j--;
    }
    return 1;
}




int32_t main() {
        ios::sync_with_stdio(0);cout.tie(0);cin.tie(0);
   
    int tc=1;
    int t;
    cin>>t;
    while(tc!=t+1){
         cout << "Case #" << tc << ": ";
      int n,nacchhooo;
      cin>>n>>nacchhooo;

      int khaoooo[n];
      for(int i=0;i<n;i++)
        cin>>khaoooo[i];

      int colapuri0=0;
      int colapuri1=0;
      for(int i=0;i<n;i++){
        if(khaoooo[i]==0)
        {
          int j=i;
          while(j<n and khaoooo[j]==0)
            j++;
          i=j-1;
          colapuri0++;
        }
      }
      for(int i=0;i<n;i++){
        if(khaoooo[i]==1)
        {
          int j=i;
          while(j<n and khaoooo[j]==1)
            j++;
          i=j-1;
          colapuri1++;
        }
      }

  int x=colapuri1;
  int y=colapuri0+1;
  
      if(x>y)
        cout<<y<<endl;
      else
        cout<<x<<endl;
      tc++;
    }

    return 0;
}