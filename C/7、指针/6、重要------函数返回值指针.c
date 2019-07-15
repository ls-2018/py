#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>

char * mystrcpy (char * dest, char * source)
{
    char *last = NULL;// 最后结果

    if (dest == NULL || source == NULL)
    {
        return last;
    }

    last = dest;

    //while ((*dest++ = *source++) != '\0');
    while (*source != '\0')
    {
        /*
        *dest = *source;
        dest++;
        source++;
        */
        *dest++ = *source++; // a=b整体表达式的值，就是b的值
    }
}


void main()
{
    char str[40] = {0};
    printf ("%s\n", mystrcpy (str, "hello world!"));
    getchar();
}