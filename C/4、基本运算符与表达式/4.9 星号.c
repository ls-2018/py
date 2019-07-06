#include<stdio.h> // 数据类型的极限值
#include<stdlib.h>
#include<math.h>
#include<limits.h>

void main()
{
    // %[-][0][m][.n][l]	格式字符
    // -	左对齐，邮编填充空格
    // 0(数字)输出的空位用0填充
    // m(>0)输出数据的字段宽度。
    //.n	对字符串，输出n位小数;对字符串,
    printf ("%4d\n", 10);	// 4	字段宽度

    for (int i = 0; i < 10; i++)
    {
        //printf("%*d\n", i, 10);	//*号与i对应，表明宽度为i，输出10
        printf ("%*.*d\n", 2 * i, i, 10);
    }
    //% d	中间>=1空格   对于正数，会添加一个空格作为前戳
	// 对于负数，没有影响
	printf("%d\n", 10);

	printf("%  d", 10);

    getchar();
}
