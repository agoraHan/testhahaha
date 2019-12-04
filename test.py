import ffmpeg
import subprocess

def get_video_info(test_dir):
    cmd = 'find %s -name "*merge_av.mp4"' % test_dir
    lists = subprocess.getoutput(cmd)
    video_url = lists.split('\n')[0]
    # print(video_url)
    info = ffmpeg.probe(video_url)
    for stream in info['streams']:
        if stream['codec_type'] == 'video':
           video_stream = stream
           print(video_stream)
    height = video_stream['height']
    width = video_stream['width']
    frame_rate = int(video_stream["r_frame_rate"].split('/')[0]) / int(video_stream["r_frame_rate"].split('/')[1])
    return int(width),int(height),int(frame_rate)

def get_audio_info(test_dir):
    cmd = 'find %s -name "*.aac"' % test_dir
    lists = subprocess.getoutput(cmd)
    audio_url = lists.split('\n')[0]
    audio_size = int(subprocess.getoutput("du -k %s" % audio_url).split("\t")[0])
    print(audio_size)
    cmd1 = 'ffmpeg -i %s -f null -' % audio_url
    time_info = subprocess.getoutput(cmd1).split("time=")[1].split(" bitrate=N/A ")[0].split(".")[0]
    audio_time = int(time_info.split(":")[0])*3600 + int(time_info.split(":")[1])*60 + int(time_info.split(":")[2])

    info = ffmpeg.probe(audio_url)
    for stream in info['streams']:
        if stream['codec_type'] == 'audio':
            audio_stream = stream

    audio_sample_rate = audio_stream['sample_rate']
    audio_channels  = audio_stream['channels']
    audio_bitrate = audio_size*8/audio_time
    return int(audio_sample_rate),int(audio_channels),int(audio_bitrate)

if __name__=='__main__':
    test_dir = "/data/jenkins/workspace/Recording_AutoTest_Test/testcases/native_com_low/test_linux_3748_com_00_c++/file_mode_com/20191204/wylive_1575447557534_081921_163841251"
    video_info = get_video_info(test_dir)
    print((video_info))
    audio_info = get_audio_info(test_dir)
    print(audio_info)