#include<stdio.h>
#include<stdlib.h>

void main()
{
    /*
    数组作为参数的时候，改变的是原来的数组
    数组当做参数的时候，传递的是指针，就是指针的大小，32位4个字节；如果作为非参数，就是整个数组
    数组数据拷贝非常浪费内存
    C语言的编译器，数组当做参数的时候，传递的是指针
    除了数组以外，都是副本机制，新建一个变量赋值
    */
    int a = 100;
    int *p = &a;
    int * *g = &p;

	printf("%x,%x\n", a, &a);
	printf("%x,%x\n", p, &p);	// a的地址，a的值
	printf("%x,%x\n", g, &g);	// g的值，g的地址
	printf("%x,%x\n", *g, **g);// a 的地址，a的值



    getchar();
}