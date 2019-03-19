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