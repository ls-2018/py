#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
void readfile (char *path)
{
    FILE *pf = fopen (path, "rb");
    char ch;
    fread (&ch, 1, 1, pf); //��ȡһ��Ԫ��

    while (!feof (pf))
    {
        printf ("%d	", ch); //��ӡASCII��
        fread (&ch, 1, 1, pf); // ��ȡ��һ��Ԫ��,�ɹ����ظ���
        /*
        ��ȡʧ�ܷ���-1��EOF,��ȡ�����Ҳ����-1
        */
        //fwrite (buf, 1, 5, pfa); // д�����飬���������׵�ַ��Ԫ�ش�СΪ1,5��Ԫ�أ��Լ��ļ�ָ��,�᷵�سɹ��ĸ���
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
        printf ("�������ļ���ʧ��");
    }

    else
    {
        fwrite (buf, 1, 5, pfa); // д�����飬���������׵�ַ��Ԫ�ش�СΪ1,5��Ԫ�أ��Լ��ļ�ָ��,�᷵�سɹ��ĸ���
        fclose (pfa);
    }

    pfb = fopen (pathb, "wb");

    if (pfb == NULL)
    {
        printf ("�������ļ���ʧ��");
    }

    else
    {
        fwrite (buf, 1, 5, pfb); // д�����飬���������׵�ַ��Ԫ�ش�СΪ1,5��Ԫ�أ��Լ��ļ�ָ��
        fclose (pfb);
    }

    printf ("\n");
    readfile (patha);//13      10      13      10      13      10      13      10      13      10
    printf ("\n");
    readfile (pathb); //10      10      10      10      10
    /*
    �ı�д��ʱ���Ὣ���з�10��'\n',ASCII������ɻس���13\r,���з�10\n
    ,��˶����ƶ�ȡ��ʱ�򣬻�������������
    ��������д�룬����ı�



    ����linux���ı�������ƶ�дû������
    */
    getchar();
}