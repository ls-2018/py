#include<stdio.h>
#include<stdlib.h>
#include<assert.h>// 静态断言的投文件

void  main()
{
    double db1 = 1, db2 = 0;
    printf ("db1=%f,db2=%f", db1, db2);
    assert (db2 != 0); //成立是正常
    system ("pause");
}
