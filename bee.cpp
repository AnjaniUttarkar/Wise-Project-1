#include<iostream>
#include<conio.h>
#include<math.h>
using namespace std;
int main() {
 //clrscr();
 int n1,n2,n1x=0,n1y=0,n2x=0,n2y=0,x=0,y=0,k=1,i,j;
 cout<<"Enter the first cell no: ";
 cin>>n1;
 cout<<"Enter the second cell no: ";
 cin>>n2;
 if (n1>n2) {
  n1+=n2;
  n2=n1-n2;
  n1=n1-n2;
 }
 for (int i=1;k<n2;i++) {
  y-=2;
  k++;
  if (k==n1) {
   n1x=x;
   n1y=y;
  }
  if (k==n2) {
   n2x=x;
   n2y=y;
  }
  for (int j=0;j<i-1;j++) {
   x--;
   y--;
   k++;
   if (k==n1) {
    n1x=x;
    n1y=y;
   }
   if (k==n2) {
    n2x=x;
    n2y=y;
   }
  }
  for (int j=0;j<i;j++) {
   x--;
   y++;
   k++;
   if (k==n1) {
    n1x=x;
    n1y=y;
   }
   if (k==n2) {
    n2x=x;
    n2y=y;
   }
  }
  for (j=0;j<i;j++) {
   y+=2;
   k++;
   if (k==n1) {
    n1x=x;
    n1y=y;
   }
   if (k==n2) {
    n2x=x;
    n2y=y;
   }
  }
  for (j=0;j<i;j++) {
   x++;
   y++;
   k++;
   if (k==n1) {
    n1x=x;
    n1y=y;
   }
   if (k==n2) {
    n2x=x;
    n2y=y;
   }
  }
  for (j=0;j<i;j++) {
   x++;
   y--;
   k++;
   if (k==n1) {
    n1x=x;
    n1y=y;
   }
   if (k==n2) {
    n2x=x;
    n2y=y;
   }
  }
  for (j=0;j<i;j++) {
   y-=2;
   k++;
   if (k==n1) {
    n1x=x;
    n1y=y;
   }
   if (k==n2) {
    n2x=x;
    n2y=y;
   }
  }
 }
 cout<<n1<<" "<<n1x<<" "<<n1y<<endl;
 cout<<n2<<" "<<n2x<<" "<<n2y<<endl;
 int a=abs(n1x-n2x);
 int b=abs(n1y-n2y);
 int c=0;
 for (;a>0||b>0;c++) {
  if (b>a) b-=2;
  else {
   a--;
   b--;
  }
 }
 cout<<c<<endl;
 getch();
}