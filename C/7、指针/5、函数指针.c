#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
void msg()
{
    printf ("---------\n");
}

void main()
{
    void (*p) () = msg;
    // º¯ÊýÖ¸Õë
    p();
    getchar();
}