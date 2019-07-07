#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
void main()
{
    int _max (int x, int y);
    int a, b, c;
    scanf ("%d%d", &a, &b);
    c = _max (a, b);
    printf ("max=%d\n", c);
    printf ("max=%d\n", max (3, 5));
    system ("pause");
}



int _max (int x, int y)
{
    int z;

    if (x > y) { z = x; }

    else
    {
        z = y;
    }

    return z;
}