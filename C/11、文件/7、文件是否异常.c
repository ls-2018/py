#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
void main()
{
    FILE *fp = fopen ("E:\\123.c", "r");

    if (fp == NULL)
    {
        printf ("lose");
    }

    else
    {
        printf ("win\n");
        fputs ("xxx", fp);

        if (ferror (fp) == 0)
        {
            printf ("正常\n");
        }

        else
        {
            printf ("异常\n");
			perror("输出的错误是");//输出的错误是: Bad file descriptor
        }

        fclose (fp);// 关闭空指针，会报错
    }

    system ("pause");
}