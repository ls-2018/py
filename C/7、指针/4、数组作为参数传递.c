#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
void test (int a[10])
{
    // ������Ϊ�������ݣ����ݵ��ǵ�ַ����ַ����ָ�� ռ4���ֽ�
    printf ("test = %d\n", sizeof (a));
}
void showa (int *a) // int a[10]
{
    for (int i = 0; i < 10; i++)
    {
        printf ("%d		%d\n", a[i], * (a + i));
    }
}
void showb (int b[][4])
{
    //void showb(int (*p)[4])
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            //printf("%d\n", b[i][j]);				b[i]==*(b+i)
            printf ("%d\n", * (* (b + i) + j));
        }
    }
}

void ser (int (*p) [3], int n)
{
    double res = 0;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            res += p[i][j];
        }
    }

    printf ("%f\n", res / 12);
}

void main()
{
    int a[10] = { 1, 2, 3, 4, 5, 6, 7 };
    int b[3][4] = { 1, 2, 3, 4, 5, 6, 7 };
    printf ("%d\n", sizeof (a));
    // ����ָ��
    test (a);
    showa (a);
    printf ("-----------------\n");
    showb (b);
    ser (b, 3);
    printf ("----%d\n", sizeof (*a)); // a��һ����ָ�룬16���ֽڣ�ÿһ����4��Ԫ��
    int (*u) [4] = a;
    getchar();
}