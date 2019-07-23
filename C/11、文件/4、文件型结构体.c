#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
void main()
{
    /*
    struct _iobuf {
        char *_ptr;
        int   _cnt;
        char *_base;
        int   _flag;
        int   _file;
        int   _charbuf;
        int   _bufsiz;
        char *_tmpfname;
        };
    typedef struct _iobuf FILE;
    */
    //FILE
    printf ("缓冲区的有效数据是%d\n", stdin->_cnt);
    printf ("缓冲区的指针是%p\n", stdin->_ptr);
    printf ("缓冲区的起始地址是%p\n", stdin->_base);
    printf ("缓冲区的大小是%d\n", stdin->_bufsiz);
    printf ("文件提示符是%d\n", stdin->_file);
    fflush (stdin); // 刷新缓冲区，有效数据清零，指针回到起始地址
    //rewind(stdin);// 文件回到开头，有效数据清零，指针回到起始地址
    stdin->_ptr = stdin->_base;//指针回到起始地址
    stdin->_cnt = 0; // 有效数据清零
    char ch = getchar();
    printf ("缓冲区的有效数据是%d\n", stdin->_cnt);
    printf ("缓冲区的指针是%p\n", stdin->_ptr);
    printf ("缓冲区的起始地址是%p\n", stdin->_base);// 始终不变
    printf ("缓冲区的大小是%d\n", stdin->_bufsiz);
    printf ("文件提示符是%d\n", stdin->_file);
    system ("pause");
}