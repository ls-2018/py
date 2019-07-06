#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
void main()
{
    // switch
    int x  ;
    scanf ("%d", &x);
    printf ("%d\n", x);

    switch (x)	// 整型、字符型
    {
        case 1:
            printf ("-\n");
            break; // 必须有break

        case 2:
            printf ("-8\n");
            break;

        default:
            printf ("-+\n");
            break;
    }
     system ("pause");
}
