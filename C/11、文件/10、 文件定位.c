rewind(fp);
int size = ftell(fp);ִ�гɹ�ʱ�����ص�ǰ�ļ�ָ�뵽�ļ�ͷ�ж��ٸ��ֽڣ����򣬷���-1



int num = fseek(fp,ƫ�ƣ���ʼ)

��ʼ��     ֵ   ����
�ļ���ʼ    0   SEEK_SET
��ǰλ��    1   SEEK_CUR
�ļ�ĩβ    2   SEEK_END



fseek(fp,0,SEEK_END)
fputs("xxxxxxxxx",pf);
fclose(fp)

windows�£����н���Ϊ/r/n�����ַ�������Ҫ������
linux�£����н���Ϊ/nһ���ַ�����Ҫһ��������