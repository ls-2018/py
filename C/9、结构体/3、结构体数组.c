 #define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct ours
{
    char addr[100];
    int num;
} o3[2] = { {"sha", 11}, {"zhang", 3} },//������,
o4[2] = {  "sha", 11,  "zhang", 3 };  // ���������ṹ�壬���������ַ�ʽ



void main()
{
    struct ours o1 = {"china", 100};
    struct ours o2[100];	// ����һ
    sprintf (o1.addr, "hello");
    printf ("%x\n", o3);
    printf ("%x\n", &o3[0]);
    printf ("%x\n", &o3[1]);
    system ("pause");
}
