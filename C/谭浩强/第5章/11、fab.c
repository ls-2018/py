#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#define M 1000

void method1()
{
	int k1, k2, k3, k4, k5, k6, k7, k8, k9, k10;
	int i, a, n, s;

	for (a = 2; a <= M; a++)
	{
		n = 0;
		s = a;

		for (i = 1; i < a; i++)
		{
			if (a % i == 0)
			{
				n++;
				s -= i;

				switch (n)
				{
				case 1:
					k1 = i;
					break;

				case 2:
					k2 = i;
					break;

				case 3:
					k3 = i;
					break;

				case 4:
					k4 = i;
					break;

				case 5:
					k5 = i;
					break;

				case 6:
					k6 = i;
					break;

				case 7:
					k7 = i;
					break;

				case 8:
					k8 = i;
					break;

				case 9:
					k9 = i;
					break;

				case 10:
					k10 = i;
					break;
				}
			}

			if (s == 0)
			{
				printf("%d,Its factors are ", a);

				if (n > 1) { printf("%d,%d", k1, k2); }

				if (n > 2)
				{
					printf("%d,%d", k1, k3);
				}

				if (n > 3)
				{
					printf("%d, ", k4);
				}

				if (n > 4)
				{
					printf("%d, ", k4);
				}

				if (n > 5)
				{
					printf("%d, ", k5);
				}

				if (n > 6)
				{
					printf("%d, ", k6);
				}

				if (n > 7)
				{
					printf("%d  ", k7);
				}

				if (n > 8)
				{
					printf("%d  ", k8);
				}

				if (n > 9)
				{
					printf("%d  ", k9);
				}

				if (n > 10)
				{
					printf("%d  ", k10);
				}
			}
		}
	}


}

void method2()
{
	int m, s, i;

	for (m = 2; m < 1000; m++)
	{
		s = 0;

		for (i = 1; i < m; i++)
		{
			if ((m % i) == 0) { s += i; }

			if (s == m)
			{
				printf("%d,its factors are \n", m);

				for (i = 1; i < m; i++)
				{
					if (m % i == 0) { printf("%d\n", i); }
				}

				printf("\n");
			}
		}
	}
}
void main()
{
	method2(); system("pause");
}