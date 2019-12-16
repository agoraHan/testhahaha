import subprocess
import time
for i in range(2):
    cmd_run = "./build_and_run.sh &"
    subprocess.getoutput(cmd_run)
    time.sleep(10)
    cmd = "pidof java"
    pid_list = []
    list = subprocess.getoutput(cmd)
    print(list)
    for i in list.split(" "):
        if i in pid_list:
            pid_list.pop(i)
        else:
            pid_list.append(i)

    print(pid_list)

    for kill_pid in pid_list:
        cmd_kill = "kill %s" % kill_pid
        subprocess.getoutput(cmd_kill)
        print("kill all java process")

    cmd_crash = 'find -name "*crash*" |wc -l'
    crash_count = subprocess.getoutput(cmd_crash)
    assert crash_count == 0

