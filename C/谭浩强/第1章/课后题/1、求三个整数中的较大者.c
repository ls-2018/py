#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
void main()
{
    int a, b, c, _max;
    scanf ("%d%d%d", &a, &b, &c);
    _max = a;

    if (b > _max)
    { _max = b; }

    if (c > _max)
    { _max = c; }

    printf ("max=%d\n", _max);
    system ("pause");
}

