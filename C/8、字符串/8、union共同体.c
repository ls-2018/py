#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
union info
{
    char addr[100];
    int num;
};  //���Ͷ��岻�����ڴ�



void main()
{
    union info d1;
    printf("%d\n",sizeof(d1));
    system ("pause");
}
