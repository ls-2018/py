//#define NODEBUG //关闭静态断言
#include<stdio.h>
#include<stdlib.h>
#include<assert.h>// 静态断言的投文件

#ifdef NODEBUG
#define myassert(x)// 没有代码检测提示
#else
#define myassert(x)	\
	if(!(x))\
{  \
    printf ("myassert(%s)宏开始检测。。。\n", #x);\
    printf ("当前函数名为%s,文件名为%s,代码行号为%d\n", __FUNCTION__, __FILE__, __LINE__);\
}
#endif


void  main()
{
    double db1 = 1, db2 = 0;
    printf ("db1=%f,db2=%f", db1, db2);
    myassert (db2 != 0); //成立是正常
    system ("pause");
}
