#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>

void main()
{
    int a = 10;
    int *p = &a; // p是左值，p是一个指针变量
    int *const px;// px是一个指针变量，不可以被赋值
    void *p1 = p;//void 类型的指针可以传递地址
    //但是由于指向不明确，所以无法取出内容
    getchar();
}