#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<stdarg.h>
#include<string.h>
double _add (int num, ...) // 可变参数
{
    //num = 8; // 默认是传递过来的第一个参数
    double last = 0.0;
    va_list  argp;// 等价于char *，指针
    va_start (argp, num); // 从这里开始读取参数,读取num个参数,并把地址放在argp

    for (int i = 0; i < num; i++)
    {
        //printf("%d------\n", va_arg(argp, int)); //挨个读取参数
        // 按照参数的位置，解析参数类型
        char str[50];//保存读取的字符串参数
        strcpy (str, va_arg (argp, char *)); //按照字符串的参数读取一个参数，拷贝到str
        printf ("%s\n", str);
    }

    va_end (argp); // 结束读取
    return last;
}
void main()
{
    double res = _add (2, "a", "b");
    printf ("%d\n", res);
    system ("pause");
    int temp = 100;
    // xxxxx(temp,++temp)   //   变量是从右往左开始引用的
    //	---->		传入的两个参数是	101,101
}