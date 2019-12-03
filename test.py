import ffmpeg
import subprocess

def get_video_info(test_dir):
    cmd = 'find %s -name "*.mp4"' % test_dir
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
    return int(width),int(height),int(frame_rate)

def get_audio_info(test_dir):
    cmd = 'find %s -name "*.aac"' % test_dir
    lists = subprocess.getoutput(cmd)
    audio_url = lists.split('\n')[0]
    # print(audio_url)
    info = ffmpeg.probe(audio_url)
    for stream in info['streams']:
        if stream['codec_type'] == 'audio':
            audio_stream = stream
    audio_sample_rate = audio_stream['sample_rate']
    audio_channels  = audio_stream['channels']
    return int(audio_sample_rate),int(audio_channels)

if __name__=='__main__':
    test_dir = "/media/root/data/workspace/Recording_AutoTest_Test/testcases/native_com_low/test_3833_com_720P_c++/file_mode_com/20191203/wylive_1575378037347_130037_409071433"
    video_info = get_video_info(test_dir)
    print(video_info)
    audio_info = get_audio_info(test_dir)
    print(audio_info)