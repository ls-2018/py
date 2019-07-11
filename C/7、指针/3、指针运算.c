#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>

void main()
{
    int a[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    int *p = a;
    printf ("%d\n", p); //即a的地址
    /*printf ("%d\n", p++);
    printf ("%d\n", p);
    printf ("%d\n", *p);*/
    //*p++;// ++的优先级 比 *高；地址先往后移动一位，再取值
    //等价于	*（p++)
    /*
    p++   ，++p,	与p+=1   都是p的地址往后移动一个元素的大小字节
    *p+1
    */
    int b = *p;
    //printf ("%d\n", b);
    //b = *p++;// 将*p的值付给b;然后p的地址往后移动一位
    printf ("====%d\n", b);
    printf ("%d，%d\n", p, *p);
    b = * (p++);	// 与*p++一样，等同与没有括号
    printf ("---%d\n", b);
    printf ("%d，%d\n", p, *p);
    /*b = * (++p);
    printf ("]]]]%d\n", b);
    printf ("%d，%d\n", p, *p);
    b = *++p;
    printf(";;;;;;%d\n", b);
    printf ("%d，%d\n", p, *p);*/
    /*
    总结：
    	作为右值，++在左，先移动地址，将新的值赋给左值
    			  ++在右，不移动地址，将旧的值赋给左值
    			  --同理



    */
    getchar();
}