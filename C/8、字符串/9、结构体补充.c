#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
/*
	�ṹ�����ռ�ݵ��ڴ浥Ԫ�ĸ���Ӧ�����ڵ������ڲ��������ݳ�Առ���ڴ浥Ԫ���ĺ�

1���ṹ������Ĵ�С�ܹ�������     ���������ͳ�Ա    �Ĵ�С������
2���ṹ���ڸ���Ա����ڽṹ���׵�ַ��ƫ���� ���ǳ�Ա��С���������������Ҫ�������ڳ�Ա֮���������ֽ�
3���ֽڶ��������׼��������������͵ĸ����ν����������ָ��
    char��short\int\float ]double �����������������͡����ݿ��  ����ָ��sizeof�Ĵ�С��ע��ṹ�塢��ͬ�������Ȳ��ʻ�����������

*/
struct sd{
    short s1;
    char as;
    char s[19];
};

void main()
{
printf("%d\n",sizeof(struct sd));
    system ("pause");
}
