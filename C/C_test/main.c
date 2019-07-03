#include <stdio.h>
#include "data.c"
#include "123.h"
// 同一个作用域，变量不能定义两次
void main() {
    int a = 1;

    add();
//    return 0;
}