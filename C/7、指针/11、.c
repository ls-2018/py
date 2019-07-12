#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>


void main()
{
    int a = 34;
    int b = 4;
    int *c = &a;
    int *d = &b;

    if (*c < *d)
    {
        int *f = NULL;
        f = c;
        c = d;
        d = f;
    }

    printf ("%d		%d\n", *c, *d);
    getchar();
}