#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
// ö�����͵�һ����ʽ���޶����÷�Χ�������Χ��
// ���û��һ������ʼֵ���ͻ��0ѭ�������һ����ÿ�μ�1
// �����һ������ֵ������ͻᰴ��ÿ�μ�һ�Ĺ���ȷ��ÿ��ö�ٳ�������ͬ
// �����Լ���ֵ������������ֵ����ÿ��ö�ٳ�������ͬ
//

enum  level
{
    ˾��, ���� = 2, �г�,  Ӫ�� = 44, ����, �ų�, �೤, ʿ��
};

void main()
{
    enum  level demo1 = ˾��;
    printf ("%d\n", demo1);
    enum  level demo2 = ����;
    printf ("%d\n", demo2);
    enum  level demo3 = �г�;
    printf ("%d\n", demo3);
    enum  level demo4 = Ӫ��;
    printf ("%d\n", demo4);
    enum  level demo5 = ����;
	printf("%d\n", demo5);
	printf("%d\n", sizeof(demo5));
	for (enum level l1=˾��;l1<=ʿ��;l1++){
	    printf("|%d\n",l1)
	}
    system ("pause");
}
