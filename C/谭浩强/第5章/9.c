#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
void main()
{
    int a, n, i = 1, sn = 0, tn = 0;
    printf ("a,n=:");
    scanf ("%d,%d", &a, &n);

    while (i <= n)
    {
        tn += a;
        sn += tn;
        a *= 10;
        i++;
    }

    printf ("a+aa+aaa+...=%d\n", sn);
    system ("pause");
}