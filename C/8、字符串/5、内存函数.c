#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<memory.h>
void main5()
{
    char str[100] = "hello";
    puts (str);
    memset (str, 'A', 10);
    puts (str);
    char dest[20] = {0};
    //memcpy(dest, str, 5);// ��str��ʼ������5���ַ���dest
    //memccpy (dest, str, '0', 7);
    // �޶�����Ϊ7���ֽڣ���str��ǰ7���ַ�������dest
    // �����ǰ������ 0  ����
    // ���û������	����7���ַ�
    //puts(dest);
	char  temp[] = "abcd";
	char *xx = temp;
	printf("%c\n", *xx);			//a
	char a = *xx++;
	printf("%c	%x	%c", a, xx, *xx);	//a   xxx   b
    getchar();
}