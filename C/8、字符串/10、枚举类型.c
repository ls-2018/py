#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
// 枚举类型的一半形式，限定作用范围在这个范围内
// 如果没有一个赋初始值，就会从0循环到最后一个，每次加1
// 如果第一个赋初值，后面就会按照每次加一的规则，确保每个枚举常量都不同
// 除非自己赋值，否则计算机赋值会让每个枚举常量都不同
//

enum  level
{
    司令, 军长 = 2, 市长,  营长 = 44, 连长, 排长, 班长, 士兵
};

void main()
{
    enum  level demo1 = 司令;
    printf ("%d\n", demo1);
    enum  level demo2 = 军长;
    printf ("%d\n", demo2);
    enum  level demo3 = 市长;
    printf ("%d\n", demo3);
    enum  level demo4 = 营长;
    printf ("%d\n", demo4);
    enum  level demo5 = 连长;
	printf("%d\n", demo5);
	printf("%d\n", sizeof(demo5));
	for (enum level l1=司令;l1<=士兵;l1++){
	    printf("|%d\n",l1)
	}
    system ("pause");
}
