#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
void main()
{
    float p, r, n;
    r = 0.07;
    n = 10;
    p = pow (1 + r, n);
    printf ("%f\n", p);
    system ("pause");
}