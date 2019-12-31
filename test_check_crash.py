import subprocess
import datetime
path = '/data/jenkins/build/serversdk/Agora_MediaStreamingServer_SDK_for_Linux_FULL.sym/bin/log/%s'%(datetime.datetime.now().strftime("%Y%m%d"))
print(path)
cmd  = 'cd %s find -name "*crash*"|wc -l' % path
cnt = subprocess.getoutput(cmd)
print(cnt)