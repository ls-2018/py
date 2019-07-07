#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define SUM 100000
void main()
{
    float amount, aver, total;
    int i;

    for (i = 1, total = 0; i <= 1000; i++)
    {
        printf ("please enter amount ");
        scanf ("%f", &amount);
        total = total + amount;

        if (total >= SUM) { break; }
    }

    aver = total / i;
    printf ("num=%d\nnaver=%10.2f\n", i, aver);
    system ("pause");
}