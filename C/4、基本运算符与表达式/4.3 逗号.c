#include<stdio.h> // 数据类型的极限值
#include<stdlib.h>
#include<math.h>


void main()
{
    int num = (1, 2, 3, 4, 5);
    printf ("%d\n", num); //打印5,以最后一个为基准
    int d = 5;
    printf ("%d\n", d = 10);
    int a;
    a = (a = 3, 6 * 3);//18
    printf ("%d\n", a);
    a = (a = a = 3, 6 * 3);//18
    printf ("%d\n", a);
    a = (a = 3, a += 2, a + 3);//8
    printf ("%d\n", a);
    a = (3 * 5, a * 4);//32
    printf ("%d\n", a);
    a = ( (a = 3 * 5, a * 4), a + 5);  //20
    printf ("%d\n", a);
    getchar();
}