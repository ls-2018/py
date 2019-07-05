#include<stdio.h> // 数据类型的极限值
#include<stdlib.h>
#include<math.h>


void main()
{
    printf ("%d\n", abs (-1));
    // 运算符不能相邻，+-号有些不同(代表正负)。
    printf ("%d\n", 10 + -1);
    /*
    34个运算符	32个关键字	9个逻辑控制		共75个

    算数运算符：+	-	*	/	%	++	--
    关系运算符：>	<	==	>=	<=	!=
    逻辑运算符：!	&&	||
    位  运算符：<<	>>	~	|	^	&
    赋值运算符：=
    条件运算符：？	：
    逗号运算符：，
    指针运算符：*	&
    求字节数运算符：sizeof
    强制类型转换运算符：
    分量运算符：->
    下表运算符：[]

    */
    //		/除号，当两侧为整数，结果为整除；有一方为小数，就是除法
    //		%	取余数
    // 自增、自减
    int num = 10;
    int c = num++;  // 先将num赋值给c,   然后num执行自增操作
    printf ("%d\n", c); // c=10
    printf ("%d\n", num); // num =11
    printf ("-----------------------\n");
    num = 10;
    int d = ++num;
    printf ("%d\n", d); // d=10
    printf ("%d\n", num); // num =11
    getchar();
}