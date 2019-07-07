#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
void main()
{
	int sign = 1;
	double demo = 2.0, sum = 1.0, term;
	while (demo<=100)
	{
		sign *= -1;
		term = sign / demo;	// ·ÖÄ¸µÝÔö
		//printf("%lf\n", term);
		sum += term;
		demo++;
	}

    printf ("res=%lf\n", sum);
    system ("pause");
}