#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>


void main()
{
    time_t ts; // ����ʱ�����
    unsigned int randdata = time (&ts); // ��ȡʱ�䣬ת��Ϊһ���޷�������
    printf ("%d\n", randdata); //�������������
    printf ("%d\n", rand());
    printf ("%d\n", rand());
    printf ("%d\n", rand());
    printf ("%d\n", rand());
    system ("pause");
}