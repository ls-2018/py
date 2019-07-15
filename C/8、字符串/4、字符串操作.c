#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include <string.h>
void demo()
{
    char *p = "hello world";
    char *px = "hello world";
    char *pd = "hello world---------";
    int is_same = strcmp (p, px);
    int is_same2 = strcmp (p, pd);
    printf ("%d\n", is_same);
    printf ("%d\n", is_same2);
    /*
    三种情况，
    0	相等
    +1	第一个字符串比较大
    -1	第一个字符串比较小

    a	97
    A	65
    0	48
    */
}

int mystrcmp (char *p1, char *p2)
{
    int num = 0;

    while (*p1 == *p2 && *p1 != '\0')
    {
        // 结束条件，p1 循环完，或者，有不一样的
        p1++;
        p2++;
    }

    if (*p1 == '\0' && *p2 == '\0')
    {
        return 0;
    }

    return *p1 - *p2;
}

void main2()
{
    demo();
    printf ("%d\n", mystrcmp ("abcj", "abcg"));
    char str[] = "asdBV";
    _strupr (str); // 小写转大写
    _strlwr (str); // 大写转小写
    printf ("%s\n", str);
    getchar();
}

void main3()
{
    // strchr查找字符串s中首次出现字符c的位置
    // 返回首次出现字符c的位置，如果s中不存在则返回NULL
    char str[] = "calcxlect";
    char *p = strchr (str, 'x');

    if (p != NULL)
    {
        printf ("%s\n", p);
    }

    char str1[30] = "yincheng";
    char str2[10] = "xxx";
    // 把str2所指字符串的添加到str1结尾处，覆盖原\0
    // 且二者不能有交集，str1必须有足够的空间，返回str1的指针
    strcat (str1, str2);
    printf ("%s\n", str1);
    strncat (str1, str2, 2);
    printf ("%s\n", str1);
    // 把数字字符串转换成正整数
    int at = atoi ("8848"); //0
    at = atoi ("e8848"); //0，出现非数字字符，都回转化失败
    printf ("%d\n", at); //0
    // 逆转字符串
    printf ("%s\n", str); //0
    _strrev (str);
    printf ("%s\n", str); //0
    getchar();
}
void main4()
{
    char str[100] = " hello ";
    char *p = " hello ";
    printf ("%d\n", strlen (str));
    printf ("%d\n", strlen (p));
    getchar();
}
void main()
{
    //strcat
    char str1[10] = "note";
    char str2[10] = "pad";
    char str[20];
    //1
    //sprintf(str, "%s%s", str1, str2);
    //printf(str);
    //2
    strcpy (str, str1);
    strcat (str, str2);
    printf (str);
    getchar();
}