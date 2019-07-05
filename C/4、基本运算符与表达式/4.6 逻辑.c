#include<stdio.h> // 数据类型的极限值
#include<stdlib.h>
#include<math.h>


void main()
{
    //逻辑   与或非
    /*
    逻辑运算符		名称	其他语言中对应的运算符	举例	运算
    	&&			逻辑与		and					x&&y	x与y
    	||			逻辑或		or					x||y	x或y
    	！			逻辑非		not					!x		非x


    */
    printf ("%d\n", 0 && 0);
    printf ("%d\n", 1 && 0);
    printf ("%d\n", 0 && 1);
    printf ("%d\n", 1 && 1);
    3 > 2 && 2 > 1 ? printf ("--\n") : printf ("=====\n");
    printf ("%d\n", 0 || 0);
    printf ("%d\n", 1 || 0);
    printf ("%d\n", 0 || 1);
    printf ("%d\n", 1 || 1);
    printf ("====================\n");
    printf ("%d\n", !1);
    printf ("%d\n", !0);
    /*
    运算的优先级（由高到低）
    ！	->	算数运算符	->	关系运算符	->	&&	->	||	->	赋值运算符
    		+-*\/				><>=<=
    */
    // 短路效应
    int a = 8;
    1 || ++a;	//a不会自增
    0 && ++a;//a不会自增
    getchar();
}
