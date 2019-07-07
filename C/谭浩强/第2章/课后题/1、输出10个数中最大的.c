#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
void main()
{
    int n = 1, _max;
    int in;
    scanf ("%d", &in);
    _max = in;

    while (n <= 10) // 10´Î
    {
        if (in > _max)
        {
            _max = in;
        }

        n++;
        scanf ("%d", &in);
    }

    printf ("max=%d", _max);
    system ("pause");
}