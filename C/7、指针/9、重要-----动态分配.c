#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>


void dt()
{
    int x;
    scanf ("%d", &x);
    int *p = (int *)  malloc (x * sizeof (int));

    /*for (int i = 0; i < x; i++)
    {
        p[i] = i + 1;
        printf ("%d	,	%x\n", p[i], p + i);
    }*/

    for (int *px = p, i = 0; px < p + x; px++, i++)
    {
        *p = i + 1;
        printf ("%d\n", *p);
    }

    free (p);
    p = NULL;// ������̹淶, ���ÿգ��ٴ��ͷ��Լ�p[i]���ر���
}
void main()
{
    dt();
    //void *x = malloc(20); // �����ڴ棻
    // ���x==NULL,�����ڴ�ʧ��
    //free(x); //�ͷ��ڴ�
    getchar();
    getchar();
}