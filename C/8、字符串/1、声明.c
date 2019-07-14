#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#define getname(x) #x
#include<time.h>
void main()
{
    time_t ts;
    srand ( (unsigned int) time (&ts));
    int num = rand() % 10;
    //字符串和\0来存储字符串
    char *str1 = "hello";	// 字符常量，可以用字符串进行初始化；{}可以省略
    //char str[5] = { 'c', 'a', 'l', 'c', '\0' }; // 字符数组可以修改
    char str[5] = "calc";
    printf ("%x	,%x \n", sizeof (str), sizeof ("calc"));	// 5	,5
    char str2[10][10] =
    {
        {"world!"},
    };
    getchar();
}