# _*_coding:utf-8_*_

def LinuxSysInfo():
    from plugins.linux import sysinfo
    return sysinfo.collect()

def WindowsSysInfo():
    from plugins.windows import sysinfo as win_sysinfo
    return win_sysinfo.collect()
