#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
void main()
{
    int x = 1;
    x *= 1;
    x *= 2;
    x *= 3;
    x *= 4;
    x *= 5;
    printf ("res=%d\n", x);
    system ("pause");




    int i,t;
	t = 1;
	i = 2;
	while (i<=5)
	{
		t *= i;
		i++;
	}
    printf ("res=%d\n", t);
    system ("pause");
}