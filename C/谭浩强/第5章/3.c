#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define SUM 100000
void main()
{
    int sign = 1;
    double pi = 0.0, n = 1.0, term = 1.0;

    while (fabs (term) >= 1e-6)
    {
        pi += term;
        n += 2;
        sign *= -1;
        term = sign / n;
    }

    pi = pi * 4;
    printf ("pi=%10.8f\n", pi);
    system ("pause");
}