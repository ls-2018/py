#include<stdio.h> // 数据类型的极限值
#include<stdlib.h>
#include<math.h>


void main()
{
    int a = 10;
    int b = 6;
    printf ("%d\n", a-- + b);
    printf ("%d\n", a);
    printf ("%d\n", b);
    a -= 1.5;
    printf ("%d\n", a);
    a = b = 5;// a=(b=5);从右到左开始执行
    a = 12;
    a += a -= a * a;// a=a+(a=a-a*a)
    printf ("%d\n", a);
    getchar();
}