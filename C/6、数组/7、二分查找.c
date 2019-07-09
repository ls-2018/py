#include<stdio.h>
#include<stdlib.h>
#include<time.h>
void main()
{
    time_t ts;
    unsigned int num = time (&ts);
    srand (num); // 初始化随机种子
    int a[1024];

    for (int i = 0; i < 1024; i++)
    {
        a[i] = i;
    }
	a[333] = 334;
    int key = 333;
    int low = 0;
    int high = 1023;
    int mid, flag = 0;

    while (low < high)
    {
        mid = (low + high) / 2;

        if (a[mid] < key)
        {
            low = mid + 1;
        }

        else
            if (a[mid] > key)
            {
                high = mid - 1;
            }

            else
                if (a[mid] == key)
                {
                    flag = mid;
                    break;
                }
    }

    if (flag)
    {
        printf ("%d\n", a[flag]);
    }

    else
    {
        printf ("lose");
    }

    getchar();
}