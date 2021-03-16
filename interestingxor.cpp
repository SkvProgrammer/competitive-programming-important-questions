#include <stdio.h>
#include <math.h>
int main(void) {
	long long int t;
	scanf("%lld",&t);
	while(t--)
	{
	    long long int c,a,b;
	    scanf("%lld",&c);
	    a=pow(2,floor(log2(c)))-1;
      printf("%lld\n",a);
	    b=a^c;
	    printf("%lld\n",a*b);
	}
	return 0;
}
