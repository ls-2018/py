#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct dangdang // dangdang����ʡ�ԣ�
{
    char  email[30];
    char name[50];
    char addr[100];
    int num;
    int bignum;
    char tel[20];
    char phone[20];
    double RMB;
} d3, d4 =
{
    "123@qq.com",


};
// �������ṹ��,	---->	����Ҫ���޵�
struct
{
    int num;
} w1, w2;

void main()
{
    struct dangdang d1, d2 ;
    struct dangdang *p = &d1;
    d3.num = 100;
    // *(d1.name) = "abc";//warning : ��=��:��char���롰char [4]���ļ�Ӽ���ͬ
    sprintf (d2.name, "hello");
    strcpy (d2.name, "hello");
    struct dangdang d5 =
    {
        "123@qq.com",


    };
    system ("pause");
}
