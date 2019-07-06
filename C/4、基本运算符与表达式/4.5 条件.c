#include<stdio.h> // 数据类型的极限值
#include<stdlib.h>
#include<math.h>


void main()
{
    int a = 4;
    //a == 0 ? a = 1 : a = 2; // 第一表达式为成立，执行第二表达式，否则第三表达式
    a = 1 ? 8 : 5;
    printf ("%d", a);  //8
    // if __ do __ else do __,会自动进行数据类型转换
    printf ("%d\n", 1 ? 4 : 5); //4
    time_t ts;
    srand ( (unsigned int) time (&ts)); // 生成随机数种子

    for (int i = 1; i < 20; i++)
    {
        int num = rand() % 100 + 1;
        num > 50 ? printf ("win\n") : printf ("lose\n");
    }

    getchar();
}
void main2()
{
    printf ("%d\n", 1 < 2 < 2 < 2); // 从左到右
    //     1<2<2
    //		1<2
    //		1







	//条件运算符的结合方向为 自右向左
	//a > b ? a :( c > d ? c : d);
	//a > b ? a : c > d ? c : d;

	getchar();
}
