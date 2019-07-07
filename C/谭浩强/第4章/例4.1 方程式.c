#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
void main()
{
    double a, b, c, disc, x1, x2, p, q   ;
    scanf ("%lf%lf%lf", &a, &b, &c);
    disc = b * b - 4 * a * c;

    if (disc < 0)
    { printf ("this equation hasn't real roots\n"); }

    else
    {
        p = -b / (a * 2.0);
        q = sqrt (disc) / (a * 2.0);
        x1 = p + q;
        x2 = p - q;
        printf ("real roots\nx1=%7.2f\nx2=%7.2f\n", x1, x2);
    }

    system ("pause");
}