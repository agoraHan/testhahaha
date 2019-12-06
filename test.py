import ffmpeg
import subprocess

def check_video_info(video_path,uid):
    cmd = 'find %s -name "%s*_av.mp4"' % (video_path,uid)
    lists = subprocess.getoutput(cmd)
    video_url = lists.split('\n')[0]
    # print(video_url)
    info = ffmpeg.probe(video_url)
    for stream in info['streams']:
        if stream['codec_type'] == 'video':
            video_stream = stream

    height = video_stream['height']
    width = video_stream['width']
    frame_rate = int(video_stream["r_frame_rate"].split('/')[0]) / int(video_stream["r_frame_rate"].split('/')[1])
    return  int(width),int(height), int(frame_rate)

def check_audio_info(audio_path,uid):
    cmd = 'find %s -name "%s*.aac"' % (audio_path,uid)
    lists = subprocess.getoutput(cmd)
    audio_url = lists.split('\n')[0]
    audio_size = int(subprocess.getoutput("du -k %s" % audio_url).split("\t")[0])
    time_info = subprocess.getoutput('ffmpeg -i %s -f null -' % audio_url).split("time=")[1].split(" bitrate=N/A ")[0].split(".")[0]
    audio_time = int(time_info.split(":")[0])*3600 + int(time_info.split(":")[1])*60 + int(time_info.split(":")[2])
    info = ffmpeg.probe(audio_url)
    for stream in info['streams']:
        if stream['codec_type'] == 'audio':
            audio_stream = stream
    audio_sample_rate = audio_stream['sample_rate']
    audio_channels  = audio_stream['channels']
    '''
    音频码率上下20kb/s属于正常范围
    计算方法：ffmpeg -i <file_name> -f null - 来获取duration（例如time=00:00:30.22）；
    audio size通过du -k命令来获取，
    audio size 除以duration计算准确的平均码率
    （例：audio size :622298、time=00:00:30.22 码率=622298*8/1024/30=162Kb/s）
    '''
    audio_bitrate = audio_size*8/audio_time
    # print("audio_sample_rate %s"% audio_sample_rate,"audio_channels %s"%audio_channels,"audio_bitrate %s" %audio_bitrate)
    return int(audio_sample_rate),int(audio_channels),int(audio_bitrate)

if __name__=='__main__':
    test_dir = "/root/Downloads/test_info/wylive_1575461902923_121822_975547145"
    video_info = check_video_info(test_dir,12345)
    print((video_info))
    audio_info = check_audio_info(test_dir,12345)
    print(audio_info)