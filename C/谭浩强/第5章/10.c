#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
void main()
{
    int g, b, s;

    for (int n = 100; n < 1000; n++)
    {
        b = n / 100;
        g = n % 10;
        s = (n - b * 100 - g) / 10;

        if (n == b * b * b + g * g * g + s * s * s)
        {
            printf ("%d\n", n);
        }
    }

    system ("pause");
}