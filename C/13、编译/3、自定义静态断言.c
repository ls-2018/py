//#define NODEBUG //�رվ�̬����
#include<stdio.h>
#include<stdlib.h>
#include<assert.h>// ��̬���Ե�Ͷ�ļ�

#ifdef NODEBUG
#define myassert(x)// û�д�������ʾ
#else
#define myassert(x)	\
	if(!(x))\
{  \
    printf ("myassert(%s)�꿪ʼ��⡣����\n", #x);\
    printf ("��ǰ������Ϊ%s,�ļ���Ϊ%s,�����к�Ϊ%d\n", __FUNCTION__, __FILE__, __LINE__);\
}
#endif


void  main()
{
    double db1 = 1, db2 = 0;
    printf ("db1=%f,db2=%f", db1, db2);
    myassert (db2 != 0); //����������
    system ("pause");
}
