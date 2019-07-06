#include<stdio.h> // 数据类型的极限值
#include<stdlib.h>
#include<math.h>
#include<limits.h>
typedef unsigned long long UUL;
void type_def()
{
    UUL  uul = 123;  //  简化书写
    // 没有创建新饿数据类型，只是为已经有的数据类型起一个别名
}
void diff_int()
{
    //输出不同类型的整数
    signed short sh1, sh2;
    sh1 = 19;
    sh2 = -19;
    unsigned short ush;
    ush = 256;
    // 有无符号短整数，都占据两个字节，16位
    printf ("%d,%d\n", sizeof (signed short), sizeof (unsigned short));
    // %hd对应有符号短整数
    printf ("%hd\n", sh1);
    printf ("%hd\n", sh2);
    // %hu对应无符号短整数
    printf ("%hu\n", ush);
    printf ("%hd,%hd\n", SHRT_MAX, SHRT_MIN);
    printf ("%hu,%hu\n", USHRT_MAX, 0);
    printf ("%hd,%hd\n", SHRT_MAX + 1, SHRT_MIN - 1);
    printf ("%hu,%hu\n", USHRT_MAX + 1, 0);
    //printf ("%u,%u\n", USHRT_MAX, 0);
    //printf ("%d,%d\n", USHRT_MAX, 0);
    printf ("%lld,%llu", 111, 111); // long long ,unsigned long long
}

void main1()
{
    int num1 = 10;
    int num2 = 010;
    int num3 = 0x10;
    printf ("%d,%d,%d\n", num1, num2, num3);
    printf ("%i,%#o,%#x\n", num1, num2, num3);
    // %#o 按照八进制输出，带0	没有# 不带0
    // %#x按照十六进制输出，带0x,没有#  不带0x


    printf("%d,%f",1.1,10);//  printf 第一个不正确，及时后边匹配也会失败。
}

void main()
{
    // %[-][0][m][.n][l]	格式字符
    // -	左对齐，邮编填充空格
    // 0(数字)输出的空位用0填充
    // m(>0)输出数据的字段宽度。
    //.n	对字符串，输出n位小数;对字符串,
    //表示截取的字符个数,
    //如果实际位数少于n，则补以0或n
    // l(字母)输出长整型整数
    printf ("%-06.4f\n", 12.0);
    printf ("=======================\n");
    // %d			int          %i与%d等价
    printf ("%10d\n", 10);
    printf ("%3d\n", 10);	// m 正常输出，或不空格
    printf ("%010d\n", 10);	// 带0 补以0(左侧）
    printf ("%010ld\n", 10);
    //diff_int();
    printf ("=======================\n");
    // %x  16	%o  8	%u  10			按照这种格式输出
    getchar();
}
