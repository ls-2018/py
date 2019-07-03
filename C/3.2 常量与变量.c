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
// 赋值的本质就是二进制的拷贝
    int a = 10;
    int b = a; // 内存地址不一样
    printf("%d--%x\n", a, &a);
    // %d   整数，按有符号十进制打印
    // %x   十六进制显示（内存地址实际也是一串数字）
    // %s   字符串
    // %u   按无符号数十进制打印

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

