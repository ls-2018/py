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
    // ֻ�п�ָ�룬�����ͷţ���û������
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

void importance()
{
    //int *p = malloc(4 * sizeof(int));
    ////realloc(�ѷ�����ڴ��ַ�����·�����ֽ���)
    //int *x = realloc(p, 8 * sizeof(int));
    ////calloc�����ڴ�飬	������ռ�ݵ��ڴ��ֽ���size,����ĸ���num��   �����Զ���ʼ��λ0
    //getchar();
    int a[3][4] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    printf ("%x\n", a);
    //int *p = a;// p[2][0]����
    int (*p) [4] = a;
    printf ("%x,	%d\n", p, p[2][0]);
    p++;
    printf ("%x,	%x	,%x\n", *p, * (p + 1), &a[2][0]);
    printf ("%d\n", p[0]);
    getchar();
    // realloc �����ڴ治���õ�����£���չ�ڴ棻���ԭ�����ڴ������ʹ�ã���ֱ����չ
    // ����ʹ�ã������·��䣬�����ȿ���ԭ���ڴ�����ݣ�Ȼ�����
}



void  xx(){
 int a[3][4] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    int *p = a;
    p++;		// ��������4���ֽ�
    printf ("%x    %x\n", a, p);
    getchar();

}