 #define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct dangdang
{
    char  email[30];
    char name[50];
    char addr[100];
    int num;
};
struct MyStruct
{
    int bignum;
    char tel[20];
    char phone[20];
    double RMB;
    struct dangdang    my1;
};

void main()
{
    struct dangdang d1, d2 ;
    struct dangdang *p = &d1;
    sprintf (d2.name, "hello");
    system ("pause");
}
