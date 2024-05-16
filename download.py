
# -------working code-------

import yt_dlp as yt
import os

def download_audio(video_id, start_time, duration, output_dir, filename):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, filename + '.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }

    with yt.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=' + video_id])

def main():
    video_id = 'u_J_mPrFNdE'  # Example video ID
    start_time = '00:00:1'  # Example start time (in seconds)
    duration = '00:00:10'  # Example duration (in seconds)
    output_dir = './output/cowbell'  # Example output directory
    filename = 'u_J_mPrFNdE'  # Example output filename

    download_audio(video_id, start_time, duration, output_dir, filename)

if __name__ == "__main__":
    main()

#https://www.youtube.com/shorts/u_J_mPrFNdE
#-----------testing code----------
# import yt_dlp as yt
# from yt_dlp import YoutubeDL
# import os

# def download_audio(video_id, start_time, end_time, output_dir, filename):
#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'outtmpl': os.path.join(output_dir, filename + '.%(ext)s'),
#         'exec_cmd': f'ffmpeg -ss {start_time} -to {end_time} -i %(extractor)s:%(id)s -vn -acodec pcm_s16le -ar 44100 -ac 2 %(outfile)s.wav',
#     }

#     with yt.YoutubeDL(ydl_opts) as ydl:
#         ydl.download(['https://www.youtube.com/watch?v=' + video_id])

# def main():
#     video_id = '-7YESdyyHVw'  # Example video ID (without time)
#     start_time = '00:00:01'  # Example start time (in HH:MM:SS format)
#     end_time = '00:00:10'  # Example end time (in HH:MM:SS format)
#     output_dir = './output/cowbell'  # Example output directory
#     filename = 'audio_clip2'  # Example output filename

#     download_audio(video_id, start_time, end_time, output_dir, filename)

# if __name__ == "__main__":
#     main()


# yt-dlp --extract-audio --audio-format wav --postprocessor-args "-ss 00:01:00 -to 00:02:00" https://www.youtube.com/watch?v=5aYwU4nj5QA

# ffmpeg -ss 00:00:30 -i $(yt-dlp -f bestaudio -g https://www.youtube.com/watch?v=7YESdyyHVw) -to 00:01:00 -c:a copy output_audio.wav

# yt-dlp -f bestaudio -g "https://www.youtube.com/watch?v=DwYuap44Q6I"

# ffmpeg -ss 00:00:30 -i "https://rr3---sn-q4fl6nsl.googlevideo.com/videoplayback?expire=1715549359&ei=T-BAZobxLuaa2_gPvtKXSA&ip=184.176.34.96&id=o-AHfJr7KWC6DF_MIJ72kKjLM9VtK-GZn_YDr8AQY2nf6s&itag=251&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=Zk&mm=31%2C29&mn=sn-q4fl6nsl%2Csn-q4fzene7&ms=au%2Crdu&mv=m&mvi=3&pl=21&initcwndbps=1168750&bui=AWRWj2SfoOMLpa7eBE_Tmm4McBolF4gNz6dZPnOOzYKWaN9CqIiqK9knsHsQKkSeDUFiy5nbFojqrCia&spc=UWF9f8s0Ir3nrxOj-AwnPed3DI4p2vqhMxY9pQmWRFjwOkXUHdhgbeQ&vprv=1&svpuc=1&mime=audio%2Fwebm&ns=sByEl3otgAbWOrTR8aZMl_cQ&rqh=1&gir=yes&clen=2106027&dur=153.381&lmt=1715430001509715&mt=1715527492&fvip=5&keepalive=yes&c=WEB&sefc=1&txp=6308224&n=LZ9oAybOqGbDkw&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRgIhAJjtxFeWIPFG5Q1bJ2a1HDt5HtnMqAU7FzDhsN-GbPn3AiEAgV-ewhmEWc6dOkPwT0VgTgbUABF4NukWb6GMIrCSGB8%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AHWaYeowRQIhAJ9Tp_OnbzwrcnKNb1tZqrk_dVQXWbnRqdqKnYcMLUlBAiA0MeuWzA2pbTJkuWj7Cb5ArnBIAPI0T5bMTzek_TfXqQ%3D%3D" -to 00:01:00 -c:a copy output_audio.wav

# DwYuap44Q6I

# yt-dlp --format bestaudio --download-sections *00:00:30-00:00:60 https://www.youtube.com/watch?v=DwYuap44Q6I

#yt-dlp -x --download-sections "*00:00:30-00:00:40" -x --audio-quality 320k --audio-format wav https://www.youtube.com/watch?v=DwYuap44Q6I
#yt-dlp -x --audio-quality 320k --audio-format wav -ss 30 -to 40 https://www.youtube.com/watch?v=DwYuap44Q6I