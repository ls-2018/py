#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<windows.h>

void main()
{
    int a = 2, flag = 0;

    if ( (a % 3) != 0)
    { flag = -1; }

    if ( (a % 5) != 0)
    { flag = -1; }

    if (flag == 0)
    { printf ("ok"); }

    else
    { printf ("not"); }

    system ("pause");
}