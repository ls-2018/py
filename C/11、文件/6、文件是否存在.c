#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
//#include<unistd.h>		// linux
void main()
{
    printf ("%d", _access ("e:\123.c", 0));
    // ģʽ0	�ļ��Ƿ����
    // 2		�Ƿ��д
    // 4		�Ƿ�ɶ�
    // 6		�Ƿ�ɶ���д
    /*
    R_OK	��Ȩ��
    W_OK	дȨ��
    X_OK	��дȨ��
    F_OK	�ļ��Ƿ����
    */
    // �Ƿ���0���񷵻�-1
    // windows�������ļ��ж��ǿɶ���д
    system ("pause");
}