#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>


void main()
{
    int a[3][4] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

    for (int *p = &a[0][0]; p < &a[0][0] + 12; p++)
    {
        //&a[0][0]   int*
        printf ("%d,%p\n", *p, p);
    }

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            printf ("%d,%p\n", * (* (a + i) + j), * (a + i) + j);
        }
    }

    getchar();
}