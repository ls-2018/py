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
    printf ("����������Ч������%d\n", stdin->_cnt);
    printf ("��������ָ����%p\n", stdin->_ptr);
    printf ("����������ʼ��ַ��%p\n", stdin->_base);
    printf ("�������Ĵ�С��%d\n", stdin->_bufsiz);
    printf ("�ļ���ʾ����%d\n", stdin->_file);
    fflush (stdin); // ˢ�»���������Ч�������㣬ָ��ص���ʼ��ַ
    //rewind(stdin);// �ļ��ص���ͷ����Ч�������㣬ָ��ص���ʼ��ַ
    stdin->_ptr = stdin->_base;//ָ��ص���ʼ��ַ
    stdin->_cnt = 0; // ��Ч��������
    char ch = getchar();
    printf ("����������Ч������%d\n", stdin->_cnt);
    printf ("��������ָ����%p\n", stdin->_ptr);
    printf ("����������ʼ��ַ��%p\n", stdin->_base);// ʼ�ղ���
    printf ("�������Ĵ�С��%d\n", stdin->_bufsiz);
    printf ("�ļ���ʾ����%d\n", stdin->_file);
    system ("pause");
}