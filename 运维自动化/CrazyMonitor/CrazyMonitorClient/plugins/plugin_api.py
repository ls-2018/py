# _*_coding:utf-8_*_

# #################Linux###################

def LinuxSysInfo():
    from .linux import sysinfo
    return sysinfo.collect()


def get_linux_cpu():
    from .linux import cpu
    return cpu.monitor()


def host_alive_check():
    from .linux import host_alive
    return host_alive.monitor()


def GetMacCPU():
    from .linux import cpu_mac
    return cpu_mac.monitor()


def GetNetworkStatus():
    from .linux import network
    return network.monitor()


def get_memory_info():
    from .linux import memory
    return memory.monitor()


def get_linux_load():
    from .linux import load
    return load.monitor()


# #################windows###################
def WindowsSysInfo():
    from .windows import sysinfo as win_sysinfo
    return win_sysinfo.collect()


def get_module(path):
    import importlib
    # 'notify.email.Email',
    module_path, class_name = path.rsplit('.', maxsplit=1)
    # 根据字符串导入模块
    module = importlib.import_module(module_path)
    # 根据类名称去模块中获取类
    func = getattr(module, 'monitor')
    return func()
