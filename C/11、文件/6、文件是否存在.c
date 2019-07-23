#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
//#include<unistd.h>		// linux
void main()
{
    printf ("%d", _access ("e:\123.c", 0));
    // 模式0	文件是否存在
    // 2		是否可写
    // 4		是否可读
    // 6		是否可读可写
    /*
    R_OK	读权限
    W_OK	写权限
    X_OK	读写权限
    F_OK	文件是否存在
    */
    // 是返回0，否返回-1
    // windows下所有文件夹都是可读可写
    system ("pause");
}