#include<stdio.h>
#include<stdlib.h>
#include<time.h>
void main()
{
    time_t ts;
    unsigned int num =  time (&ts);
    srand (num);   // 初始化随机种子
    int a[104];

    for (int i = 0; i < 104; i++)
    {
        a[i] = rand() % 104;
    }

    for (int i = 0; i < 104; i++)
    {
        int max = i;

        for (int j = i; j < 104; j++)
        {
            if (a[max] < a[j])
            {
                max = j;// 循环完毕，可能max还是和i相等
            }
        }

        int temp = a[max];
        a[max] = a[i];
        a[i] = temp;
    }

    for (int i = 0; i < 104; i++)
    {
        printf ("%d\n", a[i]);
    }

    getchar();
}