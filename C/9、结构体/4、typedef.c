#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
typedef int 整数;
// 没有创建新的数据类型，是定义类型，不是定义变量
//
/*
define	预编译是处理、简单字符替换
typedef	编译时处理	、为已有类型命名
*/
void go() {}
void main2()
{
    整数 a = 12;
    printf ("%d\n", a);
    printf ("%d\n", sizeof (a));
    typedef int s[100];
    s	x;// int x[100]

    for (int i = 0; i < 100; i++)
    {
        x[i] = i;
    }

    typedef char *str;
    str s1 = "xxx";
    printf ("%s\n", *s1);
    str s2[5] = { "xxx" };
    //void(*p)();// 函数指针
    //void(*xxxxxxxxx)();// 变量名替换为类型名
    typedef void (*xxxxxxxxx) ();
    xxxxxxxxx go1 = go;
    go1();
    system ("pause");
}

void main(){
	printf("%d\n", sizeof(char));
	printf("%d\n", sizeof(char * ));
	getchar();
}