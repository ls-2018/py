#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
void main()
{
    int num = 5;

    while (num)
    {
        //当型
        malloc (10*10*100);
        num--;
        printf ("%d\n", num);
    }

    printf ("%d\n", num);

    do
    {
        num++;
        printf ("%d\n", num);
        //直到型，先运行一次，在判断是否满足条件
    }
    while (num < 5);

    //while (1)// 必须加程序块
    //{
    //}
    printf ("%d\n", num);



    printf ("%d\n", num);
    system ("pause");
}
