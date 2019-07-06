#include<stdio.h> // 数据类型的极限值
#include<stdlib.h>
#include<windows.h>
void main()
{
    for (;;)
    {
        ShellExecuteA (0, "open", "https://www.baidu.com/baidu?ie=utf-8&tn=56060048_4_pg&ch=10&ssl_s=1&ssl_c=ssl1_16bc69f836c&word=LUFEIXUECHENG&h_search_ext=%7B%22count%22%3A5%2C%22list%22%3A%5B%7B%22txt%22%3A%22%5Cu5f20%5Cu671d%5Cu9633%5Cu518d%5Cu8c085G%5Cu5371%5Cu5bb3%22%2C%22cid%22%3A%2246606222%22%2C%22sellv%22%3Anull%2C%22sell%22%3Afalse%7D%2C%7B%22txt%22%3A%22%5Cu5218%5Cu70e8%5Cu5b89%5Cu5a1c%5Cu7ed3%5Cu5a5a%5Cu5341%5Cu5468%5Cu5e74%22%2C%22cid%22%3A%2246594522%22%2C%22sellv%22%3Anull%2C%22sell%22%3Afalse%7D%2C%7B%22txt%22%3A%22%5Cu4e2d%5Cu56fd%5Cu518d%5Cu6dfb%5Cu4e00%5Cu5904%5Cu4e16%5Cu9057%22%2C%22cid%22%3A%2228673341%22%2C%22sellv%22%3Anull%2C%22sell%22%3Afalse%7D%2C%7B%22txt%22%3A%22%5Cu9648%5Cu5609%5Cu4e0a%5Cu5411%5Cu8a00%5Cu627f%5Cu65ed%5Cu9053%5Cu6b49%22%2C%22cid%22%3A%2228673347%22%2C%22sellv%22%3Anull%2C%22sell%22%3Afalse%7D%2C%7B%22txt%22%3A%22%5Cu5927%5Cu5b66%5Cu751f%5Cu8df3%5Cu4e0b10%5Cu697c%22%2C%22cid%22%3A%2228673343%22%2C%22sellv%22%3Anull%2C%22sell%22%3Afalse%7D%2C%7B%22txt%22%3A%22%5Cu505c%5Cu673a%5Cu65ad%5Cu7f51%5Cu80fd%5Cu5145%5Cu8bdd%5Cu8d39%22%2C%22cid%22%3A%2228673350%22%2C%22sellv%22%3Anull%2C%22sell%22%3Afalse%7D%2C%7B%22txt%22%3A%22%5Cu9648%5Cu598d%5Cu5e0c%5Cu4e3a%5Cu9648%5Cu6653%5Cu5e86%5Cu751f%22%2C%22cid%22%3A%2228673345%22%2C%22sellv%22%3Anull%2C%22sell%22%3Afalse%7D%2C%7B%22txt%22%3A%22%5Cu4f5c%5Cu5bb6%5Cu674e%5Cu5fc3%5Cu7530%5Cu53bb%5Cu4e16%22%2C%22cid%22%3A%2228673346%22%2C%22sellv%22%3Anull%2C%22sell%22%3Afalse%7D%2C%7B%22txt%22%3A%22%5Cu9a6c%5Cu56fd%5Cu660e%5Cu9ec4%5Cu5fc3%5Cu9896%5Cu5206%5Cu624b%22%2C%22cid%22%3A%2228673342%22%2C%22sellv%22%3Anull%2C%22sell%22%3Afalse%7D%2C%7B%22txt%22%3A%22%5Cu6210%5Cu90fd%5Cu5783%5Cu573e%5Cu5206%5Cu7c7b%22%2C%22cid%22%3A%2228673348%22%2C%22sellv%22%3Anull%2C%22sell%22%3Afalse%7D%5D%7D", 0, 0, 3);
        Sleep (10 * 1000);
        SetCursorPos (150, 290);
        mouse_event (MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);
        mouse_event (MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);
        system ("taskkill /f /im chrome.exe");
    }

    system ("pause");
}
