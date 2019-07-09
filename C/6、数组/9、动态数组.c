#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
void demo()
{
    // 二维动态数组，
    /*
    1、整体之间是连续的，与静态二维数组一样使用
    2、整体之间不连续，一个指针数组，每一个元素都是指针，存放了另外一个数组的地址
    */
    int a[3][4] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 };
    /*for (int i = 0; i < 12; i++){
    	printf("%d\n", a[i / 4][i % 4]);
    }*/
    //int *p = &a[0][0]; // p就是地址
    //printf("%x\n", p);
    //printf("%x\n", *p);// a[0][0]
    //printf("%x\n", &a[0][0]);
    //for (int *p = &a[0][0]; p < &a[0][0] + 12; p++)
    //	printf("%d\n",*p);
    int *df = a;
    int *dg = &a;
    printf ("%x\n", a);
    printf ("%x\n", &a);
    printf ("%x\n", df);
    printf ("%x\n", dg); // 一样
    int (*p) [4] = a; // 创建一个指针数组，存储二维数组的首地址,步长为a元素的长度
    /*printf("%x\n", p);
    p++;
    printf("%x\n", p);
    //二维数组，一个指向有四个元素的一位数组的指针，指针的步长为四个int的长度。
    */
    getchar();
}


void main()
{
    // 手动输入x,y创建一个动态数组p[x][y]
    // 从0开始初始化，一直初始化到 p[x-1][y-1]这个元素，一直递增
    int x, y;
    scanf ("%d%d", &x, &y);
    //void *p = malloc (sizeof (int) * x * y); // 分配内存，连续的内存
    // y必须是一个已知的常量，才能将这片内存当做一个二维数组来使用
    //	int(*px)[9] = p;
    //	数组长度必须是一个已知量
    // 二级指针可以存储指针数组的地址
    // 动态分配一篇内存，存放指针数组，每一个元素都是一个地址
    // 然后将指针数组的首地址传递给pp保存
    int **pp = (int**) malloc (sizeof (int *) *x);

    for (int i = 0; i < x; i++)
    {
        // 分配内存，有多少列，一位数组；每个指针都指向这样一片内存的地址
        pp[i] = malloc (sizeof (int) * y);
    }

    int num = 0;

    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < y; j++)
        {
            pp[i][j] = num;	// *(*(pp+i)+j)等价
            num++;
            printf ("%4d", pp[i][j]);
        }

        printf ("\n");
    }
    for (int i=0;i<x;i++){
    // 释放内存
    free(pp[i]);
    }    free(pp);
    // printf("%d\n", sizeof(int *));	// 指向int类型数据的指针，
    system ("pause");
}