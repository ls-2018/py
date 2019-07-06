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

       // %hh 限定了字符为8位一个字节
       // 例如：   %hhd 有符号十进制字符型，%hhu无符号字符型

       // %h 限定了字符为16位两个字节
       // 例如：   %hd 有符号十进制字符型，%hu无符号字符型

       // %l 限定了字符为32位四个字节
       // 例如：   %ld 有符号十进制字符型，%lu无符号字符型

       // %ll 限定了字符为64位8个字节
       // 例如：   %lld 有符号十进制字符型，%llu无符号字符型




       // %L   输出实数，支持long  double 类型
       // 例如：   %La         // 16进制的C99计数方式











}
