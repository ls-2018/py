#include<stdio.h>

/*求两数之较大者*/

void main() {
    int max(int x, int y);
    int a, b, c;
    scanf("%d %d", &a, &b); //输入变量a和b的值,输入时-间隔为空格
    c = max(a, b);
    printf("max is %d\n", c);
    scanf("%d %d", &a, &b);
}

int max(int x, int y) {
    int z;
    if (x > y) {
        z = x;
    } else {
        z = y;
    }
    return (z);
}