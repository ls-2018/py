#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<memory.h>
#include<string.h>
void main()
{
    char str[][100] = { "hello", "world"};

    for (int i = 0; i < 2; i++)
    {
        puts (str[i]);
    }

    char demo[30];
    strcpy (demo, str[1]);
    strcpy (str[1], str[0]);
    strcpy (str[0], demo);

    for (int i = 0; i < 2; i++)
    {
        puts (str[i]);
    }

    getchar();
}