#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
void main()
{
    char buf[] = "��ð�";
    FILE *pfa;
    char patha[40] = "e:\\a.c";
    pfa = fopen (patha, "wb");

    if (pfa == NULL)
    {
        printf ("�������ļ���ʧ��");
    }

    else
    {
        //fwrite(buf, 1, 5, pfa); ���ֽ�д��
        fputs (buf, pfa);
        fflush (pfa); // ǿ��д���ļ�
        //fclose (pfa); // ���رգ�Ĭ�ϳ���ر�ʱ��д��
    }

    getchar();
}