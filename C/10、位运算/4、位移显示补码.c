#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>


void main()
{
    int num;
    scanf ("%d", &num);
    int data = 1 << 31;

    for (int i = 0; i <= 31; i++)
    {
        printf ("%c", (num & (data >> i)) ? '1' : '0');

        if ( ( (i + 1) % 4) == 0)
        {
            printf (" ");
        }
    }

    {
        /*	int *pint;
        	pint = (int *)malloc(sizeof(struct bits) * 4);
        	scanf("%d",pint)*/
    }
    // 低位在前，高位在后

    system ("pause");
}
