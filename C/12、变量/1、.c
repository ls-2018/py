#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<process.h>

/*
自动分配就是在栈上，系统自动回收清理
函数调用的时候，从定义的地方开始创建
函数结束的时候，系统自动进行回收
*/
/*
静态分配，生命周期就是整个程序执行周期
内存一直不会回收，直到程序结束才会回收
*/
/*
动态分配，malloc
在堆上，不会自动回收清理，直到调用free()
*/

/*
static int num = 100 ;  // 作用域在本个c文件内，外部无法使用
int data = 1001;// 结合extern可以跨文件使用，跨文件的作用域
*/

/*
extern 变量又称全局变量，放在静态存储区，所为全局，是说该变量可以在程序的任意位置使用，其作用域是整个程序代码范围内，
可以跨文件引用。
和auto变量不同的是	extern 有定义个声明之分
int num = 10;全局变量，会自动解析为	extern int num = 10;
*/
/*
{
	static int num = 10;//静态局部变量
	static int num;// static局部变量，没有生命，只有定义
}


static 静态全局变量;只作用于当前C文件；有定义与声明的区别；如果只有声明，又恰好有引用，会被初始化位0
	静态局部变量，没有定义与声明的区别，都是定义
	初始化时不接受变量
extern 全局变量;可以作用于所有的C文件


int b = ?(常量、常量表达式3+2、define常量、sizeof、枚举常量）
const是伪常量，编译器级别。define是寄存器级别的

*/
/*
用static声明一个变量的作用是：
	1、对局部变量用static声明，把它分配在静态存储区，该变量在整个程序执行期间不释放，其所分配的空间始终存在
	2、对全局变量用static声明，则该变量的作用域只限于本文件模块（即被声明的文件中）

静态全局变量与全局变量的区别：
	1、静态会自动初始化，不会其他文件引用
	2、全局没定义不会初始化，可以被其他文件引用。




	*/





//extern int num;	// 不定义，不会分配内存
extern int num = 10;// 定义，分配内存
int num;// 不定义，也会分配内存
//int num = 10;// 分配内存
int func2()
{
    auto int a = 12;
    // 函数内除了extern声明()  ,全部都是定义
    printf ("%d\n", num);
    printf ("%p\n", &a);
    return a;
}


void main ()
{
    int b = func2();
    func2();
    _beginthread (func2, 0, NULL);// 开一个线程，栈的大小，参数
    system ("pause");
}