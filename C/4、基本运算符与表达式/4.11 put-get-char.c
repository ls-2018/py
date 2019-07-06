//#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h> // 数据类型的极限值
#include<stdlib.h>

void main()
{
    //putchar (65);
    //putchar ('a');
    //putchar ('\n');
    //puts ("xxx"); // 会在末尾自动插入换行
    //char str[100] = { 0 }; // 全部初始化为字符  ‘\0’
    //gets_s (str,100);
    //puts (str);
    // 单精度实数输入
    // %f   %e  %E  %g  %G
    // 双精度实数输入,(已定义的变量类型是double)
    // %lf  %le     %lE     %lg     %lG
    //getchar();	//会把回车也当做一个字符，空格，tab
    //扫描集合
    //scanf ("%[xyz]", &str); //只能读取xyz,遇到一个不匹配的就终止
    //scanf ("%[^xyz\n]", &str);
    //scanf ("%[a-z]", &str);
    //scanf ("%[A-Z]", &str);
    //puts (str);
    char ch = getchar();
    //(ch >= 'A' && ch <= 'Z') ? ch = ch + 32 : ch;
    //printf("%c", ch);// 打印字符   大-->小
    (ch >= 'A' && ch <= 'Z') ? ch = ch + 32 : ( (ch >= 'a' && ch <= 'z') ? ch = ch - 32 : ch);
    printf ("%c", ch);




    //	int a = 2, b = 1, c = 4, d = 3;
    //	printf("%d", a > b ? a : (c > d ? c : d)); //自左向右
    //a > b ? a : c > d ? c : d;
    int a, b;
    scanf ("%d%n", &a, &b);		// %n 用来统计输入了多少个字符
    printf ("%d%d", a, b);
        float f1 = 1000000000000000.0;
    printf ("%e,%f", f1, f1);
    printf ("\n%a,%A", f1, f1);



    int dd;
    char dddd[40] = "num = 99";
    sscanf(dddd,"num = %d",&dd); // 从字符串中挖值
    spintf(dddd,"-----------%d",dd);// 补充模板，填入dddd
    system ("pause");
}











    system ("pause");
}
