#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
/*
	结构体变量占据的内存单元的个数应当大于等于其内部所有数据成员占据内存单元数的和

1、结构体变量的大小能够被其他     最宽基本类型成员    的大小所整除
2、结构体内个成员相对于结构体首地址的偏移量 都是成员大小的整数倍，如果需要编译器在成员之间加上填充字节
3、字节对齐第三条准则体积最宽基本类型的概念，所谓基本类型是指像
    char、short\int\float ]double 这样的内置数据类型。数据宽度  就是指其sizeof的大小。注入结构体、共同体和数组等不适基本数据类型

*/
struct sd{
    short s1;
    char as;
    char s[19];
};

void main()
{
printf("%d\n",sizeof(struct sd));
    system ("pause");
}
