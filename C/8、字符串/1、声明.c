#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#define getname(x) #x//  �Զ���x ���� ��x��
#include<time.h>
void main()
{
    time_t ts;
    srand ( (unsigned int) time (&ts));
    int num = rand() % 10;
    //�ַ�����\0���洢�ַ���
    char *str1 = "hello";	//str1�洢�ڴ��ַ �ַ��������������ַ������г�ʼ����{}����ʡ��
    //char str[5] = { 'c', 'a', 'l', 'c', '\0' }; // �ַ���������޸�
    char str[5] = "calc";
    printf ("%x	,%x \n", sizeof (str), sizeof ("calc"));	// 5	,5
    char str2[10][10] =
    {
        {"world!"},
    };
    int count = 0;
    char *x = "hello world!";

    while (*x)
    {
        printf ("%c\n", *x);
        count++;
        x++;
    }

    getchar();
}