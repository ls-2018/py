rewind(fp);
int size = ftell(fp);执行成功时，返回当前文件指针到文件头有多少个字节，否则，返回-1



int num = fseek(fp,偏移，起始)

起始点     值   名称
文件开始    0   SEEK_SET
文件末尾    2   SEEK_END
当前位置    1   SEEK_CUR