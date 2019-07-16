#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct dangdang // dangdang可以省略，
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
// 即无名结构体,	---->	数量要有限的
struct
{
    int num;
} w1, w2;

void main()
{
    struct dangdang d1, d2 ;
    struct dangdang *p = &d1;
    d3.num = 100;
    // *(d1.name) = "abc";//warning : “=”:“char”与“char [4]”的间接级别不同
    sprintf (d2.name, "hello");
    strcpy (d2.name, "hello");
    struct dangdang d5 =
    {
        "123@qq.com",


    };
    system ("pause");
}
