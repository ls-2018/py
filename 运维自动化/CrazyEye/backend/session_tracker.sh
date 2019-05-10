

session_id=$1
session_tag=$2



#echo "pwd : $PWD"

for i in $(seq 1 30)
do
    has_process=`ps -ef |grep ssh|grep -v sshpass|grep $session_tag |awk '{ print $2 }'`
    if [ "$has_process" = "" ]
    then
        sleep 1
    else
        #echo "-->$has_process"
        today=`date  "+%Y_%m_%d"`
        today_audit_dir="logs/audit/$today"
        echo "today_audit_dir: $today_audit_dir"
        if [ -d $today_audit_dir ]
        then
            echo " ----start tracking log---- "
        else
            echo "dir not exist"
            echo " today dir: $today_audit_dir"
            sudo mkdir $today_audit_dir
        fi;
        #ps -ef |awk '{ print $2 }'  |grep $has_process > "logs/audit/$today/session_$1.log"
        sudo strace  -fp $has_process -t -o  "logs/audit/$today/session_$1.log"
        break;
    fi;

done;
