#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<windows.h>
void main()
{
    int num = 123, i = 0;
    AAA:    //���ı�ţ���Ӱ�����ִ��
        if (num)
        {
            num /= 10;
            i++;
            // goto AAA;		//��ת
        }

    // for while do while  goto
    printf ("%d\n", num);
    printf ("%d\n", i);
    system ("pause");
}
