//
// Created by Administrator on 2019/7/3.
//
const int x = 10;  // 常量,定义方式1
#define pi   3.14159926// 常量,定义方式2      没有内存地址

#define xxxxxxxx 10
ma(){
int a[xxxxxxxx];
printf("");
}









// define 的本质是替换
#include <stdio.h>
#include <stdlib.h>
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
    // %d   整数，按有符号十进制打印         对应int
    // %x   十六进制显示（内存地址实际也是一串数字）
    // %s   字符串
    // %u   按无符号数十进制打印              对应unsigned int
    // %o   按无符号数八进制打印

    printf("%d\n", x);
    printf("%d\n", pi);
    printf("%x - %x\n", &a, &b);
    char c='c';


//    void multadd();
    multadd();
//    change();
    float f=1.0;
    double g=1.0;
    printf("%d                     %f\n",f,g);   // ?有问题




    int num = 65543;
    char stu[32]; // 字符数组，用于显示的字符串
    _itoa(num,stu,2);// 第一个要转换的数据，第二个是字符串、字符数组   第三个是要转换的进制数
    printf("%s\n",stu);   //65543的二进制 10000000000000111









}

