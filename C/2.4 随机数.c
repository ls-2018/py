#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>


void main()
{
    time_t ts; // 设置时间变量
    unsigned int randdata = time (&ts); // 获取时间，转换为一个无符号整数
    printf ("%d\n", randdata); //设置随机数种子
    printf ("%d\n", rand());
    printf ("%d\n", rand());
    printf ("%d\n", rand());
    printf ("%d\n", rand());
    system ("pause");
}