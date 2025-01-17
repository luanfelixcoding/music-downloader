YDL_OPTS = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  # specifying the software to extract the audio
        'preferredcodec': 'mp3',  # type of the audio
        'preferredquality': '192',  # quality of the audio
    }],
    # musics/%(title)s [%(id)s].%(ext)s
    'outtmpl': '~/Desktop/musics/%(title)s.%(ext)s',  # output
    'quiet': True,  # False it will not supress the output
}
