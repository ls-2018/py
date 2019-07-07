#include<stdio.h> // 数据类型的极限值
//#include<stdbool.h> // 支持c语言的bool型变量


void main(){
	_Bool bl;
	//bool bl;
	bl = 0;
	printf("%d\n", bl);
	printf("%d\n", sizeof(bl));
	// 成立为1，占一个字节
	// 不成立为0，占一个字节

}