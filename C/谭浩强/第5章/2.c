#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define SUM 100000
void main()
{
    int i, j, n = 0;

    for (i = 1; i <= 4; i++)
        for (j = 1; j <= 5; j++, n++)
        {
            if (n % 5 == 0)
            { printf ("\n"); }

            printf ("%d\t", i * j);
        }

    system ("pause");
}