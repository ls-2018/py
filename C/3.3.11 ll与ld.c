#include<stdio.h> // 数据类型的极限值
#include<stdlib.h>
#include<limits.h>
#include<float.h>

void main()
{
	long long moblie = 13433334444;
	printf("%d\n%Ld\n", sizeof(moblie), moblie);
	// 8个字节  32位
	printf("%lld\n%lld\n", LLONG_MAX,LLONG_MIN);


	printf("%d\n%Ld\n", sizeof(double), sizeof(long double));
	// 8

	printf("%f\n%f\n", LDBL_MAX,LDBL_MIN );
    system ("pause");

	// Ld	显示  long double
	// lld	显示  long long
}
