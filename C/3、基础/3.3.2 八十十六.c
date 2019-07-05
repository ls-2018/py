

#include<stdio.h> // 数据类型的极限值
void main(){
    printf("%d      ",10);      // 10
    printf("%d       ",-1);     //-1
    printf("%d       ",010);    //八进制数以0开头，也有正负号，    打印8
    printf("%d       ",-010);   //八进制数以0开头，也有正负号，    打印-8
    printf("%d       ",0x10);   //16进制数以0开头，也有正负号，    打印16



    printf("%d       ",10l);   //l代表long类型，32位机器上int与long等价。
    printf("%d       ",-10l);   //


    printf("%d       ",10u);   // 无符号整数常量12
//    printf("%d       ",-10u);   // 无符号整数常量12，前面不可以加负号，会出错。


}