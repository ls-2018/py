#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
void test (int a[10])
{
    // 数组作为函数传递，传递的是地址，地址就是指针 占4个字节
    printf ("test = %d\n", sizeof (a));
}
void showa (int *a) // int a[10]
{
    for (int i = 0; i < 10; i++)
    {
        printf ("%d		%d\n", a[i], * (a + i));
    }
}
void showb (int b[][4])
{
    //void showb(int (*p)[4])
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            //printf("%d\n", b[i][j]);				b[i]==*(b+i)
            printf ("%d\n", * (* (b + i) + j));
        }
    }
}
void main()
{
    int a[10] = { 1, 2, 3, 4, 5, 6, 7 };
    int b[3][4] = { 1, 2, 3, 4, 5, 6, 7 };
    printf ("%d\n", sizeof (a));
    // 函数指针
    test (a);
    showa (a);
    printf ("-----------------\n");
    showb (b);
    getchar();
}