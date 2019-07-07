#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
void main()
{
    int n = 1900;

    while (n <= 2000)
    {
        if (n % 4 == 0 && n % 100 != 0 || n % 100 == 0 && n % 400 == 0)
        { printf ("%d\n", n); }

        n++;
    }

    system ("pause");
}