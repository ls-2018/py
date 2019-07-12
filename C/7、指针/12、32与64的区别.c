#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>


void main()
{
    // 32	4字节	 8个16进制		4G	4*1024*1024*1024
	// 64	8字节	16个16进制
	int *p;
	printf("%d\n", sizeof(p));
	printf("%d\n", sizeof(int));
    getchar();
}