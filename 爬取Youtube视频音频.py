import yt_dlp

def download_youtube_audio(video_url):
    ydl_opts = {
	# 指定格式为最佳音频
        'format': 'bestaudio/best',

	# 配置后处理组件（使用 ffmpeg 提取并转换音频）
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
	# 转换为 mp3 格式 (也可以选 m4a, wav, flac 等)
            'preferredcodec': 'mp3',
	# 音频比特率 (如 192, 256, 320)
            'preferredquality': '192',
        }],
	
	# 输出文件的命名格式 (保存路径/视频标题.扩展名)
        'outtmpl': 'D:/Music/%(title)s.%(ext)s',

	# 强制支持中文等特殊字符文件名
        'restrictfilenames': False,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except Exception:
        pass

if __name__ == "__main__":

	# 替换为你想要下载的 YouTube 视频链接
  	url = ""
  	download_youtube_audio(url)