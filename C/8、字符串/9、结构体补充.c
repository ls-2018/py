#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
/*
�ṹ�����ռ�ݵ��ڴ浥Ԫ�ĸ���Ӧ�����ڵ������ڲ��������ݳ�Առ���ڴ浥Ԫ���ĺ�

1���ṹ������Ĵ�С�ܹ�����      ���������ͳ�Ա    �Ĵ�С������
2���ṹ���ڸ���Ա����ڽṹ���׵�ַ��ƫ���� ���ǳ�Ա��С���������������Ҫ�������ڳ�Ա֮���������ֽ�
3���ֽڶ��������׼��������������͵ĸ����ν����������ָ��
char��short\int\float ]double �����������������͡����ݿ��  ����ָ��sizeof�Ĵ�С��ע��ṹ�塢��ͬ�������Ȳ��ʻ�����������

*/
//struct sd
//{
//    short s1;	  //8
//    double as;    //  8
//    char s[19]; //  24
//};
//struct sd
//{
//    short s1;	  //  2
//    char as;      //  1
//    char s[19];   //  19
//};
//struct sd
//{
//	short s1;	  //  4
//	int as;      //   4
//	char s[19];   //  20
//};
struct sd
{
	char s1;	  //  0-7
	double as;      //   8-15
	char s[19];   //  16-39
};

void main()
{
    struct sd s1;
    printf ("%d\n", sizeof (struct sd));
    printf ("%x	%x	%x	%x\n", &s1, &s1.s1, &s1.as, &s1.s);
    system ("pause");
}
