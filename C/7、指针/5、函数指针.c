#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
void msg(int x)
{
    printf ("---------\n");
}

void main()
{
    void (*p) (int x) = msg;
    // ����ָ��
    p();
    getchar();
}