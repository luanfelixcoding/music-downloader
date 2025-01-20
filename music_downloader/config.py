YDL_OPTS = {
    'format': 'bestaudio/best',
    'outtmpl': '~/Desktop/musics/%(title)s.%(ext)s',  # output
    'quiet': True,  # False it will not supress the output
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  # specifying the software to extract the audio
        'preferredcodec': 'mp3',  # type of the audio
        'preferredquality': '192',  # quality of the audio
    }],
}
