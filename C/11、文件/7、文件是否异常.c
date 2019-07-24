#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
void main()
{
    FILE *fp = fopen ("E:\\123.c", "r+");

    if (fp == NULL)
    {
        printf ("lose");
    }

    else
    {
        printf ("win\n");

        if (ferror (fp) == 0)
        {
            printf ("Õý³£\n");
        }

        fclose (fp);
    }

    system ("pause");
}