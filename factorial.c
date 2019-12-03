#include <stdio.h>
#include <time.h>
long double term (int n)
{long double fact=1;
if(n==1)
	{
	return 1;}
fact=n*term(n-1);
return fact;
}
int main() {
  float start=clock();
printf("%Lf",term(20));
 float end=clock();
 printf("time for C's Factorial program %f /n",(end-start)/CLOCKS_PER_SEC);
return 0;
}

