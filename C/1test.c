#include <stdlib.h>
#include<windows.h>   // 投文件写在上面，遇到了问题。

void main() {
    system("ipconfig");// 单双引号的问题
//    system('pause');
//    system('D:\Destop\book\C\a.exe');
    MessageBox(0,"----","+++++++++",0);
    ShellExecute(0,"open","www.baidu.com",0,0,1); // 啥意思？   windows系统下的一个函数
    // open print    ,最后一个数字控制最小化(隐藏)，最大化，
    //                                     6             1
}