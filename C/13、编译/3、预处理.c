#if a == 1
    printf ("----");
#else
    printf ("=========");
#endif

----------------------------------------------------------------------------------------------


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