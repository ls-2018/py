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

    printf ("��ʮ�����ʱ������%f��\n", sn);
    printf ("��ʮ�η���%f��\n", bn);
    system ("pause");
}