#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
void main()
{
    char i, j, k;

    for (i = 'x'; i <= 'z'; i++)
        for (j = 'x'; j <= 'z'; j++)
            if (i != j)
                for (k = 'x'; k <= 'z'; k++)
                    if (i != k && j != k)
                        if (i != 'x' && k != 'x' && k != 'z')
                        { printf ("A--%c\nB--%c\nC--%c\n", i, j, k); }

    system ("pause");
}