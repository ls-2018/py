#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<memory.h>
void test (int *p)
{
    printf ("%d\n", *p);
}
void main()
{
    int a = 10;
    int *p = &a; // p����ֵ��p��һ��ָ�����
    int *const px;// px��һ��ָ������������Ա���ֵ
    void *p1 = p;//void ���͵�ָ����Դ��ݵ�ַ
    //��������ָ����ȷ�������޷�ȡ������
    test (p1);
    char str[30] = "123fsasdasga";
    int num[5] = { 1, 2, 3, 4, 5 };
    memset (str, 'A', 5); // ��str���׵�ַ��ʼ������5���ֽڣ����и�ֵ
    printf ("%s", str);
    void *x = malloc (20); // �����ڴ棻20���ֽڵ��ڴ�,����void���͵�ָ��
    // ���x==NULL,�����ڴ�ʧ��
    free (x); //�ͷ��ڴ�
    getchar();
}

void test()
{
    int num;
    scanf_s ("%d", &num);
    int *p = malloc (sizeof (int) * num);

    for (int i = 0; i < num; i++)
    {
        p[i] = i;
        printf ("%d,%x\n", p[i], &p[i]);
    }
}