#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>

void main()
{
    int a = 10;
    int *p = &a; // p����ֵ��p��һ��ָ�����
    int *const px;// px��һ��ָ������������Ա���ֵ
    void *p1 = p;//void ���͵�ָ����Դ��ݵ�ַ
    //��������ָ����ȷ�������޷�ȡ������
    getchar();
}