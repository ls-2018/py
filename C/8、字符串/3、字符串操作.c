#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include <string.h>
void main()
{
    //gets();
    // �ַ�����洢�ַ�������������������ص�
    char str[] = { 'c', 'a', 'l', 'c' };//û�н�����
    // str��һ�������������Ը�ֵ
    char *p;
    p = "ABC"; // ���ԣ��洢����ABC�ĵ�ַ
    puts (p);
    int a[5], *px;
    // a = { 1, 2, 3, 4, 5 };// ��������Ϊa�ǳ�������������
    //px = {1,2,3,4} // ָ�벻�����������ʼ��
    //char demo[100] = "woyuo123$";
    //sscanf(demo, "woyuo%d$", 1);
    char *str1 = "Borland International", *str2 = "nation", *ptr;
    ptr = strstr (str1, str2);
    printf ("The substring is: %s\n", ptr);
	//�ڴ��в���ָ���ַ����ĵ�һ�γ���
    getchar();
}