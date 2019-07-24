#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
//#include<unistd.h>		// linux
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
        // 方式一
        /*char *ch = (char *) malloc (fp->_file);
        fread (ch, sizeof (char), fp->_file, fp);
        printf ("s", ch);*/
        // 方式二
        char ch = fgetc (fp);

        //while (!feof(fp))
        while (ch != -1) // EOF即-1，代表文件结束
        {
            printf ("%c", ch);
            ch = fgetc (fp);
        }

        fclose (fp);
    }

    system ("pause");
}