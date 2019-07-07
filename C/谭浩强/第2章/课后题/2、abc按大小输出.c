#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<windows.h>

void main()
{
    int a = 2, b = 3, c = 1;
    int temp;

    if (a < b)
    {
        temp = a;
        a = b;
        b = temp;
    }

    if (a >= c)
    {
        //a>b a>=c
        if (b < c)
        {
            temp = b;
            b = c;
            c = temp;
        }
    }

    printf ("%d,%d,%d", a, b, c);
    system ("pause");
}