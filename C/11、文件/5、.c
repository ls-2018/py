#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
void main2()
{
    puts ("xx");
    int a = fputs ("xxxxx", stdout); // 写入失败会返回-1
    //
    putchar ('A');
    fputc ('a', stdout);
    //
    int a;
    scanf ("%d\n", &a);
    fscanf (stdin, "%d\n", a);
    //
    printf ("%s--", a);
    fprintf (stdout, "%d", a);
    //
    char str[50];
    gets (str);
    char g = fgetc (stdin);
    fgets (str, sizeof (str) - 1, stdin);
    fputs (str, stdout);
    system ("pause");
}
void main()
{
    int w = _getw (stdin); //从键盘获取输入4个字节
    _putw (w, stdout);	// 用int类型，容纳两个汉字
    _putw (97, stdout); // 可以输出一个字符，但是后续的会当做空字符处理
    // 一口气输出四个字符
    system ("pause");
}