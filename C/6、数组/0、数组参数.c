#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>

void _change (char a[])
{
    a[0] = 'f';
    printf ("%s, %p   %p	%p	%p	%p	%p\n", a, &a, &a[0], &a[1], &a[2], &a[3], &a[4]);
}
void main()
{
    // ����û�и������ƣ��������Ͷ��У����ǽṹ��������������û�и�������
    char a[5] = "abc";
    printf ("%s, %p   %p	%p	%p	%p	%p\n", a, &a, &a[0], &a[1], &a[2], &a[3], &a[4]);
    _change (a);
    printf ("%s, %p   %p	%p	%p	%p	%p\n", a, &a, &a[0], &a[1], &a[2], &a[3], &a[4]);
    system ("pause");
	// �����鵱����������ʱ���ᷢ�����鱾��Ŀ���������ÿ��Ԫ�ػ��Ǳ���
	// ��������Խ����ʣ����ᱨ�����Ƿ��ʵĵ�ַ�п��ܻᵼ�±���
}