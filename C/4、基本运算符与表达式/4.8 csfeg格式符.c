#include<stdio.h> // 数据类型的极限值
#include<stdlib.h>
#include<math.h>
void c_format()
{
	// %c            %[m]c		限定宽度
	int a = 97;
	char x = 'a';
	// 整数按照%d就是97，按照%c就是求编号为97 的字符
	printf("%d,%c", a, a); // 97  a
	// 字符按照%d,就是字符的编号，%c就是求字符
	printf("%d,%c", x, x); // 97  a
	getchar();
}
void f_format()
{
	// %f            %[-][0][m][.n]f
	/*
	%f	整数部分全部输出，小数部分默认6位（用四舍五入或右边补0满足小数位数）
	%m.nf	输出数据共占m列，小数占n位，右对齐
	%-m.nf	输出数据共占m列,小数占n列，左对齐
	*/

	getchar();
}
void e_format()
{
	// %e            %[-][0][m][.n]e
	// %m.ne	输出数据共占m列，小数占n位，右对齐
	/*
	输出数据共占13位，其中数据部分为1位非0数字，小数点占1位，小数部分为6位
	指数部分e占1位，指数符号占1位，指数为3位。
	若输出数据为负数，还应增加一位整数部分的符号位
	1.230000e+001
	*/

	getchar();
}
void g_format()
{
	// %g

	/*
	 根据数值的大小，自动选择用f,e格式输出实数。输出时选择占宽度较小的一种，
	 且不输出无意义的0
	*/

	getchar();
}
void main()
{
	// %s   输出字符串            %[-][m][.n]s
	/*
	%s	直接输出指定字符串
	%ms	输出字符串占m列，右对齐
	%-ms输出字符串占m列，左对齐
	%m.ns输出字符串前n个字符，占m列，右对齐
	*/
	printf("%s\n", "hello");
	printf("%9s\n", "hello");
	printf("%9.3s\n", "hello");
	printf("========================\n");
	char str[] = "hello china ";// 字符数组保存字符串，[]就是字符的集合，也就是说起到几个字符的作用
	printf("%s", str);
	getchar();
}