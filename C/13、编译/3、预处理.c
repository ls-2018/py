#if a == 1
    printf ("----");
#else
    printf ("=========");
#endif

----------------------------------------------------------------------------------------------


#ifdef NODEBUG
#define myassert(x)// 没有代码检测提示
#else
#define myassert(x)	\
	if(!(x))\
{  \
    printf ("myassert(%s)宏开始检测。。。\n", #x);\
    printf ("当前函数名为%s,文件名为%s,代码行号为%d\n", __FUNCTION__, __FILE__, __LINE__);\
}
#endif