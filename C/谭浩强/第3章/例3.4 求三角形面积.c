#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
void main()
{
    double a, b, c, s, area;
    a = 3.67;
    b = 5.43;
    c = 6.21;
    s = (a + b + c) / 2;
    area = sqrt (s * (s - a) * (s - b) * (s - c));
    printf ("%lf\n", area);
    system ("pause");
}