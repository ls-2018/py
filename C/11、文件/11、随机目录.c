#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<io.h>
void main()
{
    char path[100] = "e:\\XXXXXX";// 目录名,后面必须是6个X
    char *newname = _mktemp (path);
    printf ("%s	%s\n", newname, path); //e:\a06972       e:\a06972
    system ("pause");
}