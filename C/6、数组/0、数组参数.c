#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>

void _change (char a[])
{
    a[0] = 'f';
    printf ("%s, %p   %p	%p	%p	%p	%p\n", a, &a, &a[0], &a[1], &a[2], &a[3], &a[4]);
}
void main()
{
    // 数组没有副本机制，其他类型都有，但是结构变量包含的数组没有副本机制
    char a[5] = "abc";
    printf ("%s, %p   %p	%p	%p	%p	%p\n", a, &a, &a[0], &a[1], &a[2], &a[3], &a[4]);
    _change (a);
    printf ("%s, %p   %p	%p	%p	%p	%p\n", a, &a, &a[0], &a[1], &a[2], &a[3], &a[4]);
    system ("pause");
	// 当数组当做参数传递时，会发生数组本身的拷贝，但是每个元素还是本身。
	// 数组索引越界访问，不会报错。但是访问的地址有可能会导致崩溃
}