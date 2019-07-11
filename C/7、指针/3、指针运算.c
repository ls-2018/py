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
    int ff[5] = { 0 };
    printf ("%d,%d\n", ff, &ff);//18283320,18283320
	int *g = &ff;// 指向元素
	int(*pa)[5] = &ff;// 指向数组的指针
	printf("%d,%d,%d\n", sizeof(g), sizeof(*g), sizeof(*(&g)));  // 4,4,4
	printf("%d,%d,%d\n", sizeof(ff), sizeof(*ff), sizeof(*(&ff)));//20,4,20// 指向数组的指针
    getchar();
    /*
    若有定义int(*p)[3];则定义了一个名为p的指针变量，表示p是一个指针变量，它可以指向每行有三个整数（即int型）元素的二维数组.p是指向一维数组的指针变量。
    这句话的理解是首先(*p)[3]是一个指向一维数组的指针变量，意思就是p这个指针是指向一个含有3个元素的数组的，那么p指针每一次加1就相当于把p中存的地址加6（
                                                                        前提是int类型占2个字节，在VC中是占4个字节）。
    举个例子：int a[3][3]; int( *p)[3]; p =a; //p=a的意思是把数组a的首地址存放到p中那么p[1]就是a[1][0]的地址，p[1][0]就等于a[1][0]，而p[1][2]就等于a[1][2].

    */
}