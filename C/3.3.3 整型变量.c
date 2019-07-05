#include<stdio.h> // 数据类型的极限值
#include<limits.h>
#include<float.h> // float的极限
void main(){
printf("%d",sizeof(int));
printf("\n%d",INT_MAX);
printf("\n%u",UINT_MAX);
//INT_MAX
//INT_MIN
//SHRT_MAX
//USHRT_MAX         %d (有符号10进制)   超出范围，使用%u
//SHRT_MIN
//UINT_MAX
//FLT_MAX
//DBL_MAX

//整数用补码存储

//浮点数，用指数存储    1.2e4


/*
short   短整型        2 字节     2^16
long    长整型        4 字节     2^32
int     整型          4 字节     2^32


默认都是有符号的，
可使用unsigned    使其变成无符号数。
*/
// char ,short ,int ,long ,long long,,double,float








//     char  short 字符，无论有无符号，在表达式都会转换为int或者unsigned
// 可以跨平台移植的整数
// int     16位 2个字节         32位 4个字节

//  long    64位 linux 8个字节   windows   32位\64位都是8个
//#include<stdint.h>  //C99编译器



}