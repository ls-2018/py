"""psutil是一个跨平台库，能够轻松实现获取系统运行的进程和系统利用率它主要应用于系统监控，分析和限制系统资源及进程的管理。
采集系统的基本性能信息包括CPU、内存、磁盘、网络等，可以 完整描述当前系统的运行状态及质量。psutil模块已经封装了这些方法， 用户可以根据自身的应用场景，调用相应的方法来满足需求，非常简单实用。"""
import psutil #导入psutil
mem = psutil.virtual_memory() #使用psutil.virtual_memory方法获取内存完整信息
swap = psutil.swap_memory() #获取swap分区信息
disk = psutil.disk_partitions()  #加载磁盘完整信息
disk_usage = psutil.disk_usage('/')  #获取分区使用情况
IO = psutil.disk_io_counters(perdisk=True)  #获取磁盘io个数
print("\n","内存信息:",mem,"\n","磁盘信息=",disk,"\n","分区使用情况:",disk_usage,"\n","IO:",IO,"\n")
"""
内存信息: svmem(total=12779589632, available=8544985088, percent=33.1, used=4234604544, free=8544985088) 
磁盘信息= [
                    sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed'), 
                    sdiskpart(device='D:\\', mountpoint='D:\\', fstype='NTFS', opts='rw,fixed'), 
                    sdiskpart(device='E:\\', mountpoint='E:\\', fstype='NTFS', opts='rw,fixed'), 
                    sdiskpart(device='F:\\', mountpoint='F:\\', fstype='NTFS', opts='rw,fixed'), 
                    sdiskpart(device='G:\\', mountpoint='G:\\', fstype='NTFS', opts='rw,fixed')
            ] 

分区使用情况: sdiskusage(total=143755665408, used=92014858240, free=51740807168, percent=64.0) 
IO: {
            'PhysicalDrive1': sdiskio(read_count=1685, write_count=8437, read_bytes=31655424, write_bytes=95997952, read_time=36, write_time=30),
            'PhysicalDrive0': sdiskio(read_count=131633, write_count=103383, read_bytes=3538910208, write_bytes=3913503232, read_time=69, write_time=56)
    } 
"""


time=psutil.cpu_times() #使用cpu_times方法获取CPU完整信息，需要显示所有逻辑CPU信息，
time_user=psutil.cpu_times().user  #获取单项数据信息，如用户user的CPU时间比
cpu_count=psutil.cpu_count()  #获取CPU的逻辑个数，默认logical=True4
cpu2=psutil.cpu_count(logical=False)  #获取CPU的物理个数
print("\n","cpu信息:",time,"\n","cpu单项信息=",time_user,"\n","cpu逻辑个数=",cpu_count,"\n","cpu物理个数=",cpu2)
"""
 cpu信息: scputimes(user=4505.625, system=2875.0156250000036, idle=31789.343749999996, interrupt=241.375, dpc=189.109375) 
 cpu单项信息= 4505.625 
 cpu逻辑个数= 4 
 cpu物理个数= 2
"""

# #################################     psutil获取进程信息    ############################################
for proc in psutil.process_iter():  #
    try:
        pinfo = proc.as_dict()
        # pinfo = proc.as_dict(attrs=['pid', 'name'])
    except psutil.NoSuchProcess:
        pass
    else:
        if pinfo['pid']==8900:
            print(pinfo)
"""
{   其中的一些信息
    'exe': 'D:\\Program Files\\Notepad++\\notepad++.exe', 
    'cpu_times': pcputimes(user=0.78125, system=1.21875, children_user=0.0, children_system=0.0), 
    'memory_percent': 0.4823371154708452, 
    'username': 'DESKTOP-JRUNE4A\\Administrator', 
    'status': 'running', 
    'create_time': 1552957404.0, 
    'name': 'notepad++.exe', 
    'ppid': 5176, 
    'num_threads': 6, 
    'environ': None, 
    'cpu_percent': 0.0, 
    'pid': 8900,
    'cwd': 'd:\\Program Files\\Notepad++', 
    'cpu_affinity': [0, 1, 2, 3], 
    'num_handles': 466
}
"""
