#define   _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<io.h>
void main()
{
	FILE *pf2 = fopen("D:\\Destop\\123.txt", "w");
	fputs("��ð�123", pf2);
	fclose(pf2);
    FILE *pf = fopen ("D:\\Destop\\123.txt", "r");

    if (pf == NULL)
    {
        perror ("����ԭ��");
    }

    else
    {
        int ich;// ��ȡ�ַ�
        int nume = 0;// ��Ƕ��ٸ�Ӣ���ַ�
        int num0 = 0;// ����
        int numc = 0;// ˫�ֽ��ַ�

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
                        int iwh = fgetc (pf); // ������ǰ��һ���ַ�,fgetc����int����

                        /*
                        GBK���ֵı��뷶Χ
                        ��һ���ֽ���81-A0,�ڶ����ֽ���40-7E����80-FE
                        ��һ���ֽ���B0-D6,�ڶ����ֽ���40-7E����80-FE
                        ��һ���ֽ���D8-F7,�ڶ����ֽ���40-7E����80-FE
                        ��һ���ֽ���AA-AF,�ڶ����ֽ���40-7E����80-A0
                        ��һ���ֽ���F8-FE,�ڶ����ֽ���40-7E����80-A0
                        ��һ���ֽ�=D7,	  �ڶ����ֽ���40-7E����80-F9
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