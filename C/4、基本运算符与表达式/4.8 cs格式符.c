#include<stdio.h> // 数据类型的极限值
#include<stdlib.h>
#include<math.h>
void c_format()
{
    // %c            %[m]c		限定宽度
    int a = 97;
    char x = 'a';
    // 整数按照%d就是97，按照%c就是求编号为97 的字符
    printf ("%d,%c", a, a); // 97  a
    // 字符按照%d,就是字符的编号，%c就是求字符
    printf ("%d,%c", x, x); // 97  a
    getchar();
}


void main()
{
    // %s   输出字符串            %[-][m][.n]s
    /*
    %s	直接输出指定字符串
    %ms	输出字符串占m列，右对齐
    %-ms输出字符串占m列，左对齐
    %m.ns输出字符串前n个字符，占m列，右对齐
    */
    printf ("%s\n", "hello");
    printf ("%9s\n", "hello");
    printf ("%9.3s\n", "hello");
    printf ("========================\n");
    char str[] = "hello china ";// 字符数组保存字符串，[]就是字符的集合，也就是说起到几个字符的作用
    printf ("%s", str);
    getchar();
}