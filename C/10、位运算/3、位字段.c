#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct data
{
    unsigned int day : 5;	// �޶����������5��������λ	0-31
    unsigned int month : 4;
    unsigned int year : 14;
} demo;
struct data2
{
    unsigned char day : 1;
    unsigned char day2 : 2;
    /*
    1000 1100			��������ַ���С��4λ�������һ���ֽڣ�ͨ��λ����
    */
    unsigned int num : 10;
    /*
    1000 1100 0000 0000 0000 0000 0000 0000
    1111 1111 1100 0000 0000 0000 0000 0000
    */
} demo2;

void main()
{
    printf ("%d\n", sizeof (struct data)); // 4���ֽڣ�32��������λ
    /*
    cpu�����ֽ���Ѱַ����������һ���ֽ���Ѱַ����С��λ
    1111 1000
    1111 0000
    1111 1111
    1111 1100
    λ�ֶγ�Ա�����Դ��ڴ洢��Ԫ�ĳ��ȣ�Ҳ����Ϊ0
	������ȡλ��ĵ�ַ
	*/
    demo.day = 3;
    printf ("%d\n", demo.day);
    system ("pause");
}
