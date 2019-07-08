#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>


void main()
{
    double sn = 100, bn = sn / 2;
    int n;

    for (n = 2; n <= 10; n++)
    {
        sn += 2 * bn;
        bn /= 2;
    }

    printf ("第十次落地时共经过%f米\n", sn);
    printf ("第十次反弹%f米\n", bn);
    system ("pause");
}