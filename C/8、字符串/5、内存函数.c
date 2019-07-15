#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<memory.h>
void main5()
{
    char str[100] = "hello";
    puts (str);
    memset (str, 'A', 10);
    puts (str);
    char dest[20] = {0};
    //memcpy(dest, str, 5);// 从str开始，拷贝5个字符到dest
    //memccpy (dest, str, '0', 7);
    // 限定长度为7个字节，将str的前7个字符拷贝到dest
    // 如果提前遇到了 0  结束
    // 如果没遇到，	拷贝7个字符
    //puts(dest);

    getchar();
}