#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
void main2()
{
    puts ("xx");
    int a = fputs ("xxxxx", stdout); // д��ʧ�ܻ᷵��-1
    //
    putchar ('A');
    fputc ('a', stdout);
    //
    int a;
    scanf ("%d\n", &a);
    fscanf (stdin, "%d\n", a);
    //
    printf ("%s--", a);
    fprintf (stdout, "%d", a);
    //
    char str[50];
    gets (str);
    char g = fgetc (stdin);
    fgets (str, sizeof (str) - 1, stdin);
    fputs (str, stdout);
    system ("pause");
}
void main()
{
    int w = _getw (stdin); //�Ӽ��̻�ȡ����4���ֽ�
    _putw (w, stdout);	// ��int���ͣ�������������
    _putw (97, stdout); // �������һ���ַ������Ǻ����Ļᵱ�����ַ�����
    // һ��������ĸ��ַ�
    system ("pause");
}