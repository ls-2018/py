#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>

void main()
{
    int a[10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    int *p = a;
    printf ("%d\n", p); //��a�ĵ�ַ
    /*printf ("%d\n", p++);
    printf ("%d\n", p);
    printf ("%d\n", *p);*/
    //*p++;// ++�����ȼ� �� *�ߣ���ַ�������ƶ�һλ����ȡֵ
    //�ȼ���	*��p++)
    /*
    p++   ��++p,	��p+=1   ����p�ĵ�ַ�����ƶ�һ��Ԫ�صĴ�С�ֽ�
    *p+1
    */
    int b = *p;
    //printf ("%d\n", b);
    //b = *p++;// ��*p��ֵ����b;Ȼ��p�ĵ�ַ�����ƶ�һλ
    printf ("====%d\n", b);
    printf ("%d��%d\n", p, *p);
    b = * (p++);	// ��*p++һ������ͬ��û������
    printf ("---%d\n", b);
    printf ("%d��%d\n", p, *p);
    /*b = * (++p);
    printf ("]]]]%d\n", b);
    printf ("%d��%d\n", p, *p);
    b = *++p;
    printf(";;;;;;%d\n", b);
    printf ("%d��%d\n", p, *p);*/
    /*
    �ܽ᣺
    	��Ϊ��ֵ��++�������ƶ���ַ�����µ�ֵ������ֵ
    			  ++���ң����ƶ���ַ�����ɵ�ֵ������ֵ
    			  --ͬ��



    */
    int ff[5] = { 0 };
    printf ("%d,%d\n", ff, &ff);//18283320,18283320
	int *g = &ff;// ָ��Ԫ��
	int(*pa)[5] = &ff;// ָ�������ָ��
	printf("%d,%d,%d\n", sizeof(g), sizeof(*g), sizeof(*(&g)));  // 4,4,4
	printf("%d,%d,%d\n", sizeof(ff), sizeof(*ff), sizeof(*(&ff)));//20,4,20// ָ�������ָ��
    getchar();
}