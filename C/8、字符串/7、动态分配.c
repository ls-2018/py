#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct ours
{
    char addr[100];
    int num;
} o3[2] = { {"sha", 11}, {"zhang", 3} },//方法二,
o4[2] = {  "sha", 11,  "zhang", 3 };  // 但是无名结构体，不能用这种方式



void main()
{
    //struct ours o1 = {"china", 100};
    //struct ours o2[100];	// 方法一
    //sprintf (o1.addr, "hello");
    //printf ("%x\n", o3);
    //printf ("%x\n", &o3[0]);
    //printf ("%x\n", &o3[1]);
    //struct ours dd[1024*1024*100]; 处理大数据，必须在堆里
    // 动态分配内存
    struct ours *p = (struct ours *) malloc (sizeof (struct ours) * 1024);

    for (int i = 0; i < 1024; i++)
    {
        sprintf (p->addr, "hello");
        p->num = i;
        printf ("%s	%d\n", p->addr, p->num);
    }
	for (struct ours *pi = p; pi < p + 1024; pi++)
	{
		sprintf(pi->addr, "hello");
		pi->num = 18;
		printf("%s	%d\n", pi->addr, pi->num);
	}
    system ("pause");
}
