#include<bits/stdc++.h>
using namespace std;struct P{int x,y;}p[500000];int x,y,d,m=INT_MAX,n,i,j;main(){cin>>n;for(i=0;i<n;++i)cin>>p[i].x>>p[i].y;sort(p,p+n,[](P a,P b){return a.x<b.x;});for(i=0;i<n;++i)for(j=i+1;j<n;++j){x=p[i].x-p[j].x;y=p[i].y-p[j].y;x*=x;if(x>m)break;d=x+y*y;if(d<m)m=d;}cout<<m<<'\n';}
