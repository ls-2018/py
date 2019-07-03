//
// Created by Administrator on 2019/7/3.
//
const int x = 10;  // 常量,定义方式1
#define pi   3.14159926// 常量,定义方式2
// define 的本质是替换
#include <stdio.h>

void multadd() {
    int num = 0;
    num += 1;
    printf("%d", num);
}

void change() {
    int a = 10;
    int b = 2;
//    a, b = b, a;

    a = a*b;
    b=a/b;
    a=a/b;


}

void main() {
    int a = 10;
    int b = a; // 内存地址不一样
    printf("%d--%x\n", a, &a);
    // %d   整数
    // %x   内存地址
    // %s   字符串

    printf("%d\n", x);
    printf("%d\n", pi);
    printf("%x - %x\n", &a, &b);


    char namestr[] = "张三";
    printf("%s\n", namestr);
//    void multadd();
    multadd();
//    change();
    float f=1.0;
    double g=1.0;
    printf("%d                     %f",f,g);   // ?有问题
}

