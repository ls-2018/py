#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
void main()
{
    int n = 100;

    while (n <= 200)
    {
        int i = 2;

        while (i < n)
        {
            if (n % i == 0)
            { break; }

            else
            {
                i++;
            }
        }

        if (i == n)
        { printf ("%d\n", n); }

        n++;
    }

    system ("pause");
}