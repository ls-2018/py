#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>


void main()
{
    // 32	4�ֽ�	 8��16����		4G	4*1024*1024*1024
	// 64	8�ֽ�	16��16����
	int *p;
	printf("%d\n", sizeof(p));
	printf("%d\n", sizeof(int));
    getchar();
}