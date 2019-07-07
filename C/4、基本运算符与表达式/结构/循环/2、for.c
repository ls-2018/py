#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
void main()
{
    for (;;)
    {
        //当型
        break;
    }

    for (int i = 2; i; i--)
    {
        //中间的值为0时，不再循环
    }

    int i = 0;
    int num = 100;

    for (; num; num /= 10)
    {
        i++;
    }

    printf ("%d", i);
    system ("pause");
}
