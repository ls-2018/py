#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<stdarg.h>
#include<string.h>
double _add (int num, ...) // �ɱ����
{
    //num = 8; // Ĭ���Ǵ��ݹ����ĵ�һ������
    double last = 0.0;
    va_list  argp;// �ȼ���char *��ָ��
    va_start (argp, num); // �����￪ʼ��ȡ����,��ȡnum������,���ѵ�ַ����argp

    for (int i = 0; i < num; i++)
    {
        //printf("%d------\n", va_arg(argp, int)); //������ȡ����
        // ���ղ�����λ�ã�������������
        char str[50];//�����ȡ���ַ�������
        strcpy (str, va_arg (argp, char *)); //�����ַ����Ĳ�����ȡһ��������������str
        printf ("%s\n", str);
    }

    va_end (argp); // ������ȡ
    return last;
}
void main()
{
    double res = _add (2, "a", "b");
    printf ("%d\n", res);
    system ("pause");
    int temp = 100;
    // xxxxx(temp,++temp)   //   �����Ǵ�������ʼ���õ�
    //	---->		���������������	101,101
}