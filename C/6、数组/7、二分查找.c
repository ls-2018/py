#include<stdio.h>
#include<stdlib.h>
#include<time.h>
void main()
{
    time_t ts;
    unsigned int num =  time (&ts);
    srand (num);   // 初始化随机种子
    int a[1024];

    for (int i = 0; i < 1024; i++)
    {
        //a[i] = rand() % 1024;
        a[i] = i;
    }

    a[333] = 334;
    int target = 333;
    int shang = 0;
    int xia = 1023;
    int zhong;
    printf ("%x", a);
    int flag = 0;

    while (shang <= xia)
    {
        zhong = (shang + xia) / 2;
        printf ("shang = %d	zhong = %d	xia = %d\n", shang, zhong, xia);

        if (a[zhong] == target)
        {
            flag = 1;
            break;
        }

        if (a[zhong] < target)
        {
            shang = zhong + 1;
        }

        if (a[zhong] > target)
        { xia = zhong - 1; }
    }

    if (flag)
    {
        printf ("找到了");
    }

    else
    {
        printf ("没找到");
    }

    getchar();
}