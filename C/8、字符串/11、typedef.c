#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
typedef int ����;
// û�д����µ��������ͣ��Ƕ������ͣ����Ƕ������
//
/*
define	Ԥ�����Ǵ������ַ��滻
typedef	����ʱ����	��Ϊ������������
*/
void go() {}
void main2()
{
    ���� a = 12;
    printf ("%d\n", a);
    printf ("%d\n", sizeof (a));
    typedef int s[100];
    s	x;// int x[100]

    for (int i = 0; i < 100; i++)
    {
        x[i] = i;
    }

    typedef char *str;
    str s1 = "xxx";
    printf ("%s\n", *s1);
    str s2[5] = { "xxx" };
    //void(*p)();// ����ָ��
    //void(*xxxxxxxxx)();// �������滻Ϊ������
    typedef void (*xxxxxxxxx) ();
    xxxxxxxxx go1 = go;
    go1();
    system ("pause");
}

void main(){
	printf("%d\n", sizeof(char));
	printf("%d\n", sizeof(char * ));
	getchar();
}