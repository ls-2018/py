#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include <string.h>
void demo()
{
    char *p = "hello world";
    char *px = "hello world";
    char *pd = "hello world---------";
    int is_same = strcmp (p, px);
    int is_same2 = strcmp (p, pd);
    printf ("%d\n", is_same);
    printf ("%d\n", is_same2);
    /*
    ���������
    0	���
    +1	��һ���ַ����Ƚϴ�
    -1	��һ���ַ����Ƚ�С

    a	97
    A	65
    0	48
    */
}

int mystrcmp (char *p1, char *p2)
{
    int num = 0;

    while (*p1 == *p2 && *p1 != '\0')
    {
        // ����������p1 ѭ���꣬���ߣ��в�һ����
        p1++;
        p2++;
    }

    if (*p1 == '\0' && *p2 == '\0')
    {
        return 0;
    }

    return *p1 - *p2;
}

void main2()
{
    demo();
    printf ("%d\n", mystrcmp ("abcj", "abcg"));
    char str[] = "asdBV";
    _strupr (str); // Сдת��д
    _strlwr (str); // ��дתСд
    printf ("%s\n", str);
    getchar();
}

void main3()
{
    // strchr�����ַ���s���״γ����ַ�c��λ��
    // �����״γ����ַ�c��λ�ã����s�в������򷵻�NULL
    char str[] = "calcxlect";
    char *p = strchr (str, 'x');

    if (p != NULL)
    {
        printf ("%s\n", p);
    }

    char str1[30] = "yincheng";
    char str2[10] = "xxx";
    // ��str2��ָ�ַ�������ӵ�str1��β��������ԭ\0
    // �Ҷ��߲����н�����str1�������㹻�Ŀռ䣬����str1��ָ��
    strcat (str1, str2);
    printf ("%s\n", str1);
    strncat (str1, str2, 2);
    printf ("%s\n", str1);
    // �������ַ���ת����������
    int at = atoi ("8848"); //0
    at = atoi ("e8848"); //0�����ַ������ַ�������ת��ʧ��
    printf ("%d\n", at); //0
    // ��ת�ַ���
    printf ("%s\n", str); //0
    _strrev (str);
    printf ("%s\n", str); //0
    getchar();
}
void main4()
{
    char str[100] = " hello ";
    char *p = " hello ";
    printf ("%d\n", strlen (str));
    printf ("%d\n", strlen (p));
    getchar();
}
void main()
{
    //strcat
    char str1[10] = "note";
    char str2[10] = "pad";
    char str[20];
    //1
    //sprintf(str, "%s%s", str1, str2);
    //printf(str);
    //2
    strcpy (str, str1);
    strcat (str, str2);
    printf (str);
    getchar();
}