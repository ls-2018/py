#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include <string.h>
void main()
{
    //gets();
    // 字符数组存储字符串，具有所有数组的特点
    char str[] = { 'c', 'a', 'l', 'c' };//没有结束符
    // str是一个常量，不可以赋值
    char *p;
    p = "ABC"; // 可以，存储的是ABC的地址
    puts (p);
    int a[5], *px;
    // a = { 1, 2, 3, 4, 5 };// 不可以因为a是常量（数组名）
    //px = {1,2,3,4} // 指针不可以用数组初始化
    //char demo[100] = "woyuo123$";
    //sscanf(demo, "woyuo%d$", 1);
    char *str1 = "Borland International", *str2 = "nation", *ptr;
    ptr = strstr (str1, str2);
    printf ("The substring is: %s\n", ptr);
	//在串中查找指定字符串的第一次出现
    getchar();
}