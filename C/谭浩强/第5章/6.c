#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<math.h>


void main()
{
    char c  ;

    while ( (c = getchar()) != '\n')
    {
        if ( (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
        {
            if (c >= 'W' && c <= 'Z' || c >= 'w' && c <= 'z') { c = c - 22; }

            else
            { c = c + 4; }
        }
    }

    system ("pause");
}