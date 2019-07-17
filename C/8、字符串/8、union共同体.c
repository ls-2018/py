#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
/*
	共同体是几个不同类型的变量共占一段内存，相互覆盖；
在任何时刻只有一个成员存在；
共同体变量定义分配内存，长度=最长成员所占字节数

不能引用共同体变量，只能引用其成员
共同体变量中起作用的成员是最后一次存放的成员
不能在变量初始化只能{first}对第一个变量进行赋值
*/
union info
{
    char addr[100];
    int num;
} d2, *d3, d4[5]; //类型定义不分配内存

union info d5, *d6, d7[5];
union
{
    char addr[100];
    int num;
} d8;
union  ddf	// 16
{
    double b;	// 8
    char str[9];	// 9
} ff;// 共同体的大小，一定可以被最小类型所整除
void main()
{
    union info d1;
    strcpy (d1.addr, "world");
    //printf("%d\n", sizeof(d1)); // 最大成员变量所占的内存大小
    printf ("%d\n", sizeof (union  ddf)); // 最大成员变量所占的内存大小
    //printf ("%d	%s\n", d1.num, d1.addr);
    system ("pause");
}
