rewind(fp);
int size = ftell(fp);执行成功时，返回当前文件指针到文件头有多少个字节，否则，返回-1



int num = fseek(fp,偏移，起始)

起始点     值   名称
文件开始    0   SEEK_SET
当前位置    1   SEEK_CUR
文件末尾    2   SEEK_END



fseek(fp,0,SEEK_END)
fputs("xxxxxxxxx",pf);
fclose(fp)

windows下，换行解析为/r/n两个字符，不需要结束符
linux下，换行解析为/n一个字符，需要一个结束符