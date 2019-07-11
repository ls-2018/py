#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<memory.h>
void test (int *p)
{
    printf ("%d\n", *p);
}
void main()
{
    int a = 10;
    int *p = &a; // p是左值，p是一个指针变量
    int *const px;// px是一个指针变量，不可以被赋值
    void *p1 = p;//void 类型的指针可以传递地址
    //但是由于指向不明确，所以无法取出内容
    test (p1);
    char str[30] = "123fsasdasga";
    int num[5] = { 1, 2, 3, 4, 5 };
    memset (str, 'A', 5); // 从str的首地址开始，向后的5个字节，进行赋值
    printf ("%s", str);
    void *x = malloc (20); // 开辟内存；20个字节的内存,返回void类型的指针
    // 如果x==NULL,分配内存失败
    free (x); //释放内存
    getchar();
}

void test()
{
    int num;
    scanf_s ("%d", &num);
    int *p = malloc (sizeof (int) * num);

    for (int i = 0; i < num; i++)
    {
        p[i] = i;
        printf ("%d,%x\n", p[i], &p[i]);
    }
}