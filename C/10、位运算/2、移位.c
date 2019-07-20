#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>

void main()
{
    unsigned  char a = 8;
    printf ("%d\n", a >> 1);
    printf ("%d\n", a);// 移位不会改变操作数
    // 左移需要考虑 溢出问题
    /*
    注意事项：
    只能作用于	char	short	int	long	long long
    字符型，整数型

    实数是指数方式表示的，不适用于位运算

    */
    unsigned char ch = 12;// 1个字节
    unsigned int num = 123;// 4个字节
    printf ("%d\n", ch & num); // 会自动进行数据类型转换，向大类型转换
    //  负数
    ch = -12;// 1个字节		在计算机中以补码的形式存在
    // 10001100		--> 11110011       11110100
    num = -123;// 4个字节
    // 11111011          10000100      10000101
    // 10000011
    printf ("%d\n", ch & num);
    printf ("%d\n", -2 << 2);
    /*
    左边移动的时候，右边填充0
    右边移动的时候，如果是无符号数据，左边填充0
    				如果是有符号的数据，整数按照符号位填充0，负数按照符号位1填充1
    */
    system ("pause");
}
