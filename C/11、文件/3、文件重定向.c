#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
void main()
{
    char str[100] = { 0 };
    /*scanf ("%s", str);
    printf ("str=%s\n", str);*/
    FILE *f = fopen ("e:\\123.c", "w");
    fscanf (stdin, "%s", str);
    fprintf (f, "str=%s\n", str);
    getchar();
}