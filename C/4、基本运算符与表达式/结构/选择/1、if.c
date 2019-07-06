#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
void main()
{
    int a = 10;

    if (a > 10)
    {
        printf ("---\n");
    }

    else
    {
        if (a < 10)
        {
            printf ("-++\n");
        }

        else
        {
            printf ("=====\n");
        }
    }



    //char ch = getchar();
    ////(ch >= 'A' && ch <= 'Z') ? ch = ch + 32 : ch;
    ////printf("%c", ch);// 打印字符   大-->小
    //(ch >= 'A' && ch <= 'Z') ? ch = ch + 32 : ((ch >= 'a' && ch <= 'z') ? ch = ch - 32 : ch);
    //printf("%c", ch);
    //int   b=4, c = 2;
    //printf("%d\n", b);
    //printf("%d\n", c);
    //scanf_s("%d\n", &b); printf("%d\n", b); getchar();
    system ("pause");
}
