#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>


void dt()
{
    int x;
    scanf ("%d", &x);
    int *p = (int *)  malloc (x * sizeof (int));

    /*for (int i = 0; i < x; i++)
    {
        p[i] = i + 1;
        printf ("%d	,	%x\n", p[i], p + i);
    }*/

    for (int *px = p, i = 0; px < p + x; px++, i++)
    {
        *p = i + 1;
        printf ("%d\n", *p);
    }

    free (p);
    p = NULL;// 软件工程规范, 不置空，再次释放以及p[i]都回报错
    // 只有空指针，反复释放，都没有问题
}
void main()
{
    dt();
    //void *x = malloc(20); // 开辟内存；
    // 如果x==NULL,分配内存失败
    //free(x); //释放内存
    getchar();
    getchar();
}

void importance()
{
    //int *p = malloc(4 * sizeof(int));
    ////realloc(已分配的内存地址，重新分配的字节数)
    //int *x = realloc(p, 8 * sizeof(int));
    ////calloc申请内存块，	（对象占据的内存字节数size,对象的个数num）   ，会自动初始化位0
    //getchar();
    int a[3][4] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    printf ("%x\n", a);
    //int *p = a;// p[2][0]出错
    int (*p) [4] = a;
    printf ("%x,	%d\n", p, p[2][0]);
    p++;
    printf ("%x,	%x	,%x\n", *p, * (p + 1), &a[2][0]);
    printf ("%d\n", p[0]);
    getchar();
    // realloc 就是内存不够用的情况下，扩展内存；如果原来的内存后部无人使用，就直接扩展
    // 有人使用，就重新分配，并且先拷贝原来内存的内容，然后回收
}



void  xx(){
 int a[3][4] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    int *p = a;
    p++;		// 往后走了4个字节
    printf ("%x    %x\n", a, p);
    getchar();

}