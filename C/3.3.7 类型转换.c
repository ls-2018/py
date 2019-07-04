#include<stdio.h> // 数据类型的极限值
//#include<limits.h> // int的极限
//#include<float.h> // float的极限

void main(){

   double a = 2.3111111111111111;
   printf("%.100f\n",a);  //强制类型转换，不会改变被转换变量的值
   printf("%d\n",(int)(1+a));  //强制类型转换，不会改变被转换变量的值
   getchar();
   char x = 'x';
   printf("%d\n",x);
   printf("%c\n",x);
   printf("%s\n","xxxx");
   printf("%d\n",sizeof(char));
}