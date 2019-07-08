#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#define N 10
#define M 10

void main()
{
    /* int a[3][4] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};

     for (int i = 0; i < 12; i++)
     {
         a[i  / 4][i % 4] = i;
     }*/
    int a[][2] = { { 1, 2 } };
    int b[2][2] = { { 1, 2 } };
    /*
    a[i]+j	与	&a[i][j]	等价
    a[i][j]	与	*(&a[i][j])	等价


    */
    system ("pause");
}
void run(){

int num[N][N];
    /*for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            num[i][j] = N * i + j + 1;
        }
    	printf("\n");
    }*/
    int nu = 0;

    for (int i = 0; i < N * N; i++)
    {
        num[i / N][i % N] = ++nu;
        printf ("%5d", num[i / N][i % N]);

        if ( (i + 1) % N == 0)
        {
            printf ("\n");
        }
    }

    system ("pause");

}