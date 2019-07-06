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
// %d   整数，按有符号十进制打印    int
// %x   无符号十六进制显示（内存地址实际也是一串数字）
// %s   字符串
// %u   按无符号数十进制打印  int
// %c   字符
// %o   无符号数八进制打印

// 只有x,c，e，g可以大小写 ---->输出的也是对应的大小写

//%e  以标准指数形式输出单双精度实数，如果小写的e，指数小写的e，否则就是大写的E

//%g   选用输出宽度缴械的格式输出实数










/*
内存中一律以补码存在

正数： 原反补一样
负数：
    原： 开头为1 ，其余为对应二进制
    反： 开头为1 ，其余位反转
    补： 开头为1 ，其余位加一，进位舍弃


负数补求   原码：
取反，加一

*/

}