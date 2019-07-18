#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>

struct info
{
    char name[50];
    long long phone;
};
union school
{
    char name[50];
    int num;
};
struct stu
{
    union school school;
    struct info info;
};
void main()
{
    struct stu *p;
    p = (struct stu *) malloc (sizeof (struct  stu)); // ·ÖÅäÄÚ´æ
    p->info.phone = 1232323123;
    strcpy (p->info.name, "xxx");
    printf ("%d\n", sizeof (char));
    printf ("%d\n", sizeof (char *));
    getchar();
}