#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
void main()
{
    int a = 8, b = 12, t;

    if (a < b)
    {
        int temp;
        temp = a;
        a = b;
        b = temp;
    }

    t = a % b;

    while (t != 0)
    {
        a = b;
        b = t;
        t = a % b;
    }

    printf ("%d\n", b);
    system ("pause");
}