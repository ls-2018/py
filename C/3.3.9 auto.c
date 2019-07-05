#include<stdio.h> // 数据类型的极限值
#include<stdlib.h>
// auto用于软件开发工程规范，让代码清晰易懂
// 如果只是为了让程序可以跑起来，可以不加
void go(auto int num){
	auto int data = num;
	printf("\n%x,%d", &num, num);
	printf("\n%x,%d", &data, data);

	static int n = 100;
	// 静态变量，一直存在，值没有变化，地址也没有变化
	// 自动变量，函数调用的时候，就存在，函数结束的时候就终止
	// 地址都是同一地址，但是内容却反复变化
}
// 此文件必须是.c后缀，让VS2013运行的时候
//1.新版C++定义auto不能和任何类型进行组合；
//2.auto x = 14; 表示把x自动转换成整型，归结为 auto 变量名 = 值（可以是基本数据类型）:auto根据后面的值自动把该变量转换成相应的类型。
//3.大多数以普通声明方式声明的变量都是auto变量, 他们不需要明确指定auto关键字，默认就是auto；
//4.auto变量在离开作用域是会被程序自动释放，不会发生内存溢出。


void main(){
	go(11);
	system("pause");
}
