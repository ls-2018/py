#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
/*
	��ͬ���Ǽ�����ͬ���͵ı�����ռһ���ڴ棬�໥���ǣ�
���κ�ʱ��ֻ��һ����Ա���ڣ�
��ͬ�������������ڴ棬����=���Ա��ռ�ֽ���
*/
union info
{
    char addr[100];
    int num;
} d2, *d3, d4[5]; //���Ͷ��岻�����ڴ�

union info d5, *d6, d7[5];
union
{
    char addr[100];
    int num;
} d8;

void main()
{
    union info d1;
    strcpy (d1.addr, "world");
    printf ("%d\n", sizeof (d1)); // ����Ա������ռ���ڴ��С
    printf ("%d	%s\n", d1.num, d1.addr);
    system ("pause");
}
