#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
void readfile (char *path)
{
    FILE *pf = fopen (path, "rb");
    char ch;
    fread (&ch, 1, 1, pf); //读取一个元素

    while (!feof (pf))
    {
        printf ("%d	", ch); //打印ASCII码
        fread (&ch, 1, 1, pf); // 读取下一个元素,成功返回个数
        /*
        读取失败返回-1，EOF,读取到最后也返回-1
        */
        //fwrite (buf, 1, 5, pfa); // 写入数组，传入数组首地址，元素大小为1,5个元素，以及文件指针,会返回成功的个数
        //char ch = fgetc(p);
        //putchar(ch);
    }

    fclose (pf);
}
void main()
{
    //FILE *pf = stdout;
    //fputs("hello ", pf);
    char buf[5] = { 10, 10, 10, 10, 10};
    FILE *pfa;
    FILE *pfb;
    char patha[40] = "e:\\a.c";
    char pathb[40] = "e:\\b.c";
    pfa = fopen (patha, "w");

    if (pfa == NULL)
    {
        printf ("二进制文件打开失败");
    }

    else
    {
        fwrite (buf, 1, 5, pfa); // 写入数组，传入数组首地址，元素大小为1,5个元素，以及文件指针,会返回成功的个数
        fclose (pfa);
    }

    pfb = fopen (pathb, "wb");

    if (pfb == NULL)
    {
        printf ("二进制文件打开失败");
    }

    else
    {
        fwrite (buf, 1, 5, pfb); // 写入数组，传入数组首地址，元素大小为1,5个元素，以及文件指针
        fclose (pfb);
    }

    printf ("\n");
    readfile (patha);//13      10      13      10      13      10      13      10      13      10
    printf ("\n");
    readfile (pathb); //10      10      10      10      10
    /*
    文本写入时，会将换行符10即'\n',ASCII码解析成回车符13\r,换行符10\n
    ,因此二进制读取的时候，会出现这种情况。
    而二进制写入，不会改变



    而在linux，文本与二进制读写没有区别
    */
    getchar();
}