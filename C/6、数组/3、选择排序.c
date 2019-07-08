#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>


void main()
{
    time_t ts; // 设置时间变量
    unsigned int randdata = time (&ts); // 获取时间，转换为一个无符号整数
    printf ("%d\n", randdata); //设置随机数种子
    int a[10];

    for (int i = 0; i < 10; i++)
    {
        a[i] = rand();
    }

    for (int i = 0; i < 10; i++)
    {
        int max = i;

        for (int j = i; j < 10; j++)
        {
            if (a[j] > a[max])
            {
                int temp;
                temp = a[j];
                a[j] = a[max];
                a[max] = temp;
            }
        }
    }

    for (int i = 0; i < 10; i++)
    {
        printf ("%6d", a[i]);
    }

    system ("pause");
}