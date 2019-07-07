#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
void main()
{
    int num = 123, i = 0;
    AAA:    //语句的标号，不影响代码执行
        if (num)
        {
            num /= 10;
            i++;
            // goto AAA;		//跳转
        }

    // for while do while  goto
    printf ("%d\n", num);
    printf ("%d\n", i);
    system ("pause");
}
