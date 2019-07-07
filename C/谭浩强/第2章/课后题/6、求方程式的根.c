#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
void main()
{
    double a, b, c, disc, x1, x2, p, q;
    scanf ("%lf%lf%lf", &a, &b, &c);
    disc = b * b - 4 * a * c;
    p = -b / (2.0 * a);
    q = sqrt (disc) / (2.0 * a);
    x1 = p + q;
    x2 = p - q;
    printf ("x1=%7.2f\nx2=%7.2f\n", x1, x2);
    system ("pause");
}