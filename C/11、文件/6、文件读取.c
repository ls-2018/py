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
        // ��ʽһ
        /*char *ch = (char *) malloc (fp->_file);
        fread (ch, sizeof (char), fp->_file, fp);
        printf ("s", ch);*/
        // ��ʽ��
        char ch = fgetc (fp);

        //while (!feof(fp))
        while (ch != -1) // EOF��-1�������ļ�����
        {
            printf ("%c", ch);
            ch = fgetc (fp);
        }

        fclose (fp);
    }

    system ("pause");
}