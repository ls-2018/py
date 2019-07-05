#include<stdio.h> // 数据类型的极限值
#include<stdlib.h>
#include<limits.h>
#include<float.h>
#include<windows.h>
#include<locale.h>

void main()
{
	setlocale(LC_ALL,"chs");//使用简体中文,否则当字符串中含中文，打印不了
    MessageBox (0, "123是", "想", 0); // 使用多字节字符集，不会出现乱码。
	MessageBox(0, L"123是", L"想", 0);// UNICODE格式下,不会出现乱码


	MessageBoxW(0, L"123是", L"想", 0);// 无论多字节还是Unicode，就是Unicode
	MessageBoxA(0, "123是", "想", 0);// 无论多字节还是Unicode，就是多字节




	MessageBox(0, TEXT("123是"), TEXT("想"), 0);
	// 自动适应Unicode， 多字节





	// 项目，属性，常规，字符集， Unicode会出现乱码。
    //char 字符串可以显示汉字，字符不可以，字符连在一起%c%c可以显示汉字
    /*char str[10] = "你好";
    char ch = '我';
    printf ("\n%s", str);
    printf ("\n%c%c", str[0], str[1]); */// 一个汉字2字节
    // 只有在字符串的里的两个字符连续输出 ，才可以输出一个字
    // 字符不行




	wchar_t xc = L'我';//L宽字符或者宽字符串
	wchar_t xzc = L"我";//L宽字符或者宽字符串

    //wprintf (L"\n%wc", xc); //汉字当做一个字符

	//wchar_t xcx[20] = L"as撒大大大多多多多多多";//L宽字符或者宽字符串
	//wprintf(L"\n%s", xcx); //汉字当做一个字符






    getchar();
}
