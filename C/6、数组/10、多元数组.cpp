#include<iostream>
#include<map>
#include<stdio.h>
void main()
{
    int int1 = 10;
    double double1 = 99.8;
    char ch = 'a';
    char *str = "hellow";
    std::tuple<int, double, char, char*>mytuple (int1, double1, ch, str);
    auto data0 = std::get<0> (mytuple);
    auto data1 = std::get<1> (mytuple);
    auto data2 = std::get<2> (mytuple);
    auto data3 = std::get<3> (mytuple);
    std::cout << "data0" << data0;
    getchar();
}