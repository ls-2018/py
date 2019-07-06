#include<stdio.h> // 数据类型的极限值
#include<stdlib.h>
#include<math.h>
#include<limits.h>

void main()
{
    printf ("%o,%#o\n", 8, 8);
    printf ("%x,%#x\n", 8, 8);
    printf ("%x,%#X\n", 8, 8);
    printf ("%.0f,%f\n", 1.1, 1.1);
    printf ("%#.0f,%f\n", 1.1, 1.1); // # 确保一定保留小数点
	printf("%#.0e,%e\n", 1.1, 1.1);
    getchar();
}
