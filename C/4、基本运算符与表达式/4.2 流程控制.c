#include<stdio.h> // 数据类型的极限值
#include<stdlib.h>
#include<math.h>


void main()
{
    for (int i = 2; i < 5; i++)
    {
        printf ("%d\n", i); // 2 3 4
    }

    printf ("-----------------------\n"); // 2 3 4
    int i = 2;

    while (i < 5)
    {
        printf ("%d\n", i); // 2 3 4
        i++;
    }

    printf ("-----------------------\n");
    printf ("%d\n", i); // 5
    printf ("-----------------------\n");
    i = 2;

    while (i++ < 5) // 先判断i大小，在自增
    {
        printf ("%d\n", i); // 3 4 5
    }

    printf ("-----------------------\n");
    i = 2;

    while (++i < 5) // 先自增，在判断大小，
    {
        printf ("%d\n", i); //	3	4
    }

    for (;;)
    {
        switch (i)
        {
            case 1:
                return 1;
            case 2:
                i = i +2 ;
                break;
            default:
                return 0;
        }
    }

    getchar();
}
