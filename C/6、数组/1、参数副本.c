#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>

struct MyStruct
{
    int a[5];
    int n;

};
void _change (struct MyStruct my1)
{
    my1.n = 10000;
    my1.a[0] = 5;
}
void main()
{
    // 数组没有副本机制，其他类型都有，但是结构变量包含的数组没有副本机制
    struct MyStruct my1 = { { 1, 2, 3, 4, 5 }, 10 };
    printf ("%d,%d		%x	%p\n", my1.n, my1.a[0], &my1, &my1);
    _change (my1);
    printf ("%d,%d		%x	%p\n", my1.n, my1.a[0], &my1, &my1);
    system ("pause");
}