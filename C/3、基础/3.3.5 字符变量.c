#include<stdio.h> // 数据类型的极限值
#include<limits.h> // int的极限
#include<float.h> // float的极限

void main(){
 putchar('a');
 putchar(100);
 putchar('\100');
 putchar('\x10');

    printf("%d",'1'); // 求字符的编号
    printf("%c",'1'); // 显示该字符
    printf("%d",1); // 显示整数1
    printf("%c",1); // 求编号为1 字符


// char 是 1 字节
 char a = '1';
 char b = 1;
 int c = 1;
// a 与b的区别，b在末尾有隐藏的   \0，  会占一个长度


// a与c的区别

/*在内存中，a以ascii存在，占一个字节

而c占2个、4个或8个字节*/

char ch ='A';
printf("%c,%d",ch,ch);   //A,65
ch=ch+1;
printf("%c,%d",ch,ch);   //B 66






for (int i=0;i<100;i++){
    putchar(i);
}

char str[2]="cd";
printf("\n%s",str);
printf(str);
sprintf(str,"\nasdsad%d",10);
printf(str);

//sprintf(str,"%%d");
// str是一个字符数组，有40个字符，  % 被当做一个单独字符处理，
//% 打印为空， % ，i 连在一起，0 ， 没有初始化的数据
//打印的时候会有bug,显示有问题，不影响程序执行
}