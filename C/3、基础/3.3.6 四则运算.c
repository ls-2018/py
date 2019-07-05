#include<stdio.h> // 数据类型的极限值
#include<limits.h> // int的极限
#include<float.h> // float的极限

void main(){
// % 只能整型

//C语言为什么要规定先声明变量呢？为什么要指定变量的名字和对应的数据类型呢？
//建立变量符号表
//变量的类型指示系统分配多少内存
//变量的类型指示系统如何解释存储空间中的值
//
//变量的类型确定变量的取值范围
//不同的数据类型有不同的操作
int a =1;
double b=1.2;
a=b;
printf("%d",a);


//short --> int ---> double
//int ---> float ---> double
}