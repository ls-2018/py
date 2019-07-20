#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct data
{
    unsigned int day : 5;	// 限定这个变量用5个二进制位	0-31
    unsigned int month : 4;
    unsigned int year : 14;
} demo;
struct data2
{
    unsigned char day : 1;
    unsigned char day2 : 2;
    /*
    1000 1100			如果两个字符都小于4位，会填充一个字节，通过位操作
    */
    unsigned int num : 10;
    /*
    1000 1100 0000 0000 0000 0000 0000 0000
    1111 1111 1100 0000 0000 0000 0000 0000
    */
} demo2;

void main()
{
    printf ("%d\n", sizeof (struct data)); // 4个字节，32个二进制位
    /*
    cpu按照字节来寻址，所以至少一个字节是寻址的最小单位
    1111 1000
    1111 0000
    1111 1111
    1111 1100
    位字段成员不可以大于存储单元的长度，也不能为0
	不可以取位域的地址
	*/
    demo.day = 3;
    printf ("%d\n", demo.day);
    system ("pause");
}
