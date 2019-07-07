#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<math.h>


void main()
{
    int n, i;
    printf ("please enter a interger number ,n=£¿");
    scanf ("%d", &n);

    for (i = 2; i < n; i++)
        if (n % i == 0) { break; }

    if (i < n) { printf ("%d is not a prime number\n", n); }

    else
    {
        printf ("%d is a prime number\n", n);
    }

    system ("pause");
}