#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
void demo()
{
    // ��ά��̬���飬
    /*
    1������֮���������ģ��뾲̬��ά����һ��ʹ��
    2������֮�䲻������һ��ָ�����飬ÿһ��Ԫ�ض���ָ�룬���������һ������ĵ�ַ
    */
    int a[3][4] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 };
    /*for (int i = 0; i < 12; i++){
    	printf("%d\n", a[i / 4][i % 4]);
    }*/
    //int *p = &a[0][0]; // p���ǵ�ַ
    //printf("%x\n", p);
    //printf("%x\n", *p);// a[0][0]
    //printf("%x\n", &a[0][0]);
    //for (int *p = &a[0][0]; p < &a[0][0] + 12; p++)
    //	printf("%d\n",*p);
    int *df = a;
    int *dg = &a;
    printf ("%x\n", a);
    printf ("%x\n", &a);
    printf ("%x\n", df);
    printf ("%x\n", dg); // һ��
    int (*p) [4] = a; // ����һ��ָ�����飬�洢��ά������׵�ַ,����ΪaԪ�صĳ���
    /*printf("%x\n", p);
    p++;
    printf("%x\n", p);
    //��ά���飬һ��ָ�����ĸ�Ԫ�ص�һλ�����ָ�룬ָ��Ĳ���Ϊ�ĸ�int�ĳ��ȡ�
    */
    getchar();
}


void main()
{
    // �ֶ�����x,y����һ����̬����p[x][y]
    // ��0��ʼ��ʼ����һֱ��ʼ���� p[x-1][y-1]���Ԫ�أ�һֱ����
    int x, y;
    scanf ("%d%d", &x, &y);
    //void *p = malloc (sizeof (int) * x * y); // �����ڴ棬�������ڴ�
    // y������һ����֪�ĳ��������ܽ���Ƭ�ڴ浱��һ����ά������ʹ��
    //	int(*px)[9] = p;
    //	���鳤�ȱ�����һ����֪��
    // ����ָ����Դ洢ָ������ĵ�ַ
    // ��̬����һƪ�ڴ棬���ָ�����飬ÿһ��Ԫ�ض���һ����ַ
    // Ȼ��ָ��������׵�ַ���ݸ�pp����
    int **pp = (int**) malloc (sizeof (int *) *x);

    for (int i = 0; i < x; i++)
    {
        // �����ڴ棬�ж����У�һλ���飻ÿ��ָ�붼ָ������һƬ�ڴ�ĵ�ַ
        pp[i] = malloc (sizeof (int) * y);
    }

    int num = 0;

    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < y; j++)
        {
            pp[i][j] = num;	// *(*(pp+i)+j)�ȼ�
            num++;
            printf ("%4d", pp[i][j]);
        }

        printf ("\n");
    }
    for (int i=0;i<x;i++){
    // �ͷ��ڴ�
    free(pp[i]);
    }    free(pp);
    // printf("%d\n", sizeof(int *));	// ָ��int�������ݵ�ָ�룬
    system ("pause");
}