#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>

void main()
{
    char a[30] = { "hello " };
    char b[] = { "world" };
    printf ("%s\n", strcat (a, b)); // 将b接到a后面，结果在a中。函数返回a的地址，
    // a要指定足够大的空间，连接时只保留b后面的\0
    // 经过试验，b不能指定大小
    // /////////////////////////////////////////////////////
    char str1[10], str2[] = "china";
    strcpy (str1, str2);
    // strcpy(str1, "xxxx");
    // 不合法操作	str1="asd";str1=str2;
    strncpy (str1, str2, 2); // 将str2中的前2个字符，复制到str1中
    // /////////////////////////////////////////////////////
    strcmp ("a", "b"); //比较两个 字符串 在ASCII数的大小,返回0，正整数，负整数

    if (strcmp ("ca", "b") > 0)
    { printf ("yes\n"); }

    // /////////////////////////////////////////////////////
    printf ("%d\n", strlen (str1)); //字符数组有效值得长度，不包括\0
    // /////////////////////////////////////////////////////
    //char f = "Hello";
    //_strlwr(f);
    //printf ("%s\n",f );// 字符串转小写
    // /////////////////////////////////////////////////////
    //printf ("%s\n", _strupr ("Hello")); // 字符串转小写
    getchar();
}