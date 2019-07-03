#include<stdio.h> // 数据类型的极限值
#include<limits.h> // int的极限
#include<float.h> // float的极限

void main(){
    //   十进制小数形式
//    printf("%f      ",100.1);   //
//    printf("%f      ",.1);   //
//    printf("%f      ",0.0);   //  默认小数点后会有六位
//    // 指数
//    printf("%f      ",10e4);   //
//    printf("%f      ",10e-4);   //  e可大小写
    printf("%f     %.10f",FLT_MAX,FLT_MIN);   //  e可大小写
//    340282346638528860000000000000000000000.000000     0.0000000000
    // double       8字节
    // float        4 字节
//    sizeof(1.0)      8
//    sizeof(1.0f)      4

}