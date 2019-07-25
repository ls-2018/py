#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<io.h>
void main()
{
	FILE *pf2 = fopen("D:\\Destop\\123.txt", "w");
	fputs("你好啊123", pf2);
	fclose(pf2);
    FILE *pf = fopen ("D:\\Destop\\123.txt", "r");

    if (pf == NULL)
    {
        perror ("错误原因");
    }

    else
    {
        int ich;// 获取字符
        int nume = 0;// 标记多少个英文字符
        int num0 = 0;// 数字
        int numc = 0;// 双字节字符

        //while (!feof (pf))
        while ( (ich = fgetc (pf) != EOF))
        {
            if ( (ich >= 'A' && ich <= 'Z') || (ich <= 'z' && ich >= 'a'))
            {
                nume++;
            }

            else
                if (ich >= '0' && ich <= '9')
                {
                    num0++;
                }

                else
                    if (ich > 128)
                    {
                        int iwh = fgetc (pf); // 继续向前读一个字符,fgetc返回int类型

                        /*
                        GBK汉字的编码范围
                        第一个字节在81-A0,第二个字节在40-7E或者80-FE
                        第一个字节在B0-D6,第二个字节在40-7E或者80-FE
                        第一个字节在D8-F7,第二个字节在40-7E或者80-FE
                        第一个字节在AA-AF,第二个字节在40-7E或者80-A0
                        第一个字节在F8-FE,第二个字节在40-7E或者80-A0
                        第一个字节=D7,	  第二个字节在40-7E或者80-F9
                        */
                        if ( (ich >= 0x81 && ich <= 0xA0) && ( (iwh >= 0x40 && iwh <= 0x7E) || (iwh <= 0xFE && iwh >= 0x80)))
                        {
                            numc++;
                        }
						else if ((ich >= 0xB0 && ich <= 0xD6) && ((iwh >= 0x40 && iwh <= 0x7E) || (iwh <= 0xFE && iwh >= 0x80)))
						{
							numc++;
						}
						else if((ich >= 0xD8 && ich <= 0xF7) && ((iwh >= 0x40 && iwh <= 0x7E) || (iwh <= 0xFE && iwh >= 0x80)))
						{
							numc++;
						}
						else if((ich >= 0xAA && ich <= 0xAF) && ((iwh >= 0x40 && iwh <= 0x7E) || (iwh <= 0xA0 && iwh >= 0x80)))
						{
							numc++;
						}
						else if((ich >= 0xF8 && ich <= 0xFE) && ((iwh >= 0x40 && iwh <= 0x7E) || (iwh <= 0xA0 && iwh >= 0x80)))
						{
							numc++;
						}
						else if((ich == 0xD7) && ((iwh >= 0x40 && iwh <= 0x7E) || (iwh <= 0xF9 && iwh >= 0x80)))
						{
							numc++;
						}
                    }
        }

        printf ("%d	%d	%d", nume, num0, numc);
        fclose (pf);
    }

    system ("pause");
}