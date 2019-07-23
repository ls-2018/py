#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
void main()
{
    char buf[] = "你好啊";
    FILE *pfa;
    char patha[40] = "e:\\a.c";
    pfa = fopen (patha, "wb");

    if (pfa == NULL)
    {
        printf ("二进制文件打开失败");
    }

    else
    {
        //fwrite(buf, 1, 5, pfa); 按字节写入
        fputs (buf, pfa);
        fflush (pfa); // 强制写入文件
        //fclose (pfa); // 不关闭，默认程序关闭时，写入
    }

    getchar();
}