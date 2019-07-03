//
// Created by Administrator on 2019/7/3.
//

/*
char    1个字节
short   2个字节
int     4个字节，不同系统，也不同
double  8个字节
 */
#include <stdio.h>
#include<limits.h> // 数据类型的极限值
void main(){
    printf("%d               %d\n",INT_MAX,INT_MIN);
    printf("%d               %d\n",UINT_MAX,0);

    printf("%d\n", sizeof(char));// sizeof 是一个运算符，不是函数
    unsigned int x =1 ;// 无符号
    int y = 2; //有符号

}