#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>



void main()
{
    /*
    &
    |
    ^	���
    ~	ȡ��
    >>	����
    <<	����
    �����ı�ԭֵ
    */
    unsigned char a = 15;	// 0000 1111
    unsigned char b = ~a;	// 1111 0000	240
    printf ("%d\n", b);
    printf ("%d\n", a);
    printf ("%d\n", a ^ 0); // ����ԭ������
    printf ("%d\n", a ^ 255); // 1111 1111		��ת
    // ������������
    unsigned char ch1 = 20;		// 0001 0100
    unsigned char ch2 = 10;		// 0000 1010
    ch1 = ch1 ^ ch2;
    ch2 = ch2 ^ ch1;
    ch1 = ch2 ^ ch1;
    printf ("%d	%d\n", ch1, ch2);
    // �� unsigned  char ĩβ����
    printf ("%d\n", 11 & ~1);
    // ���73��4��������������%
    printf ("%d\n", 73 - (73 & ~3));	// - �� ~ ��&
    system ("pause");
}
