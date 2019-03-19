from fabric.api import run

def host_type():
        run("uname -s")
# fab -f 5、fabric命令.py  -H 193.112.27.150 -u root host_type