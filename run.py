from __future__ import unicode_literals
import yt_dlp
from youtubesearchpython import VideosSearch

ydl_opts = {
  'format': 'bestaudio/best',
  'outtmpl': 'music/%(title)s.%(ext)s',
  'postprocessors': [{
      'key': 'FFmpegExtractAudio',
      'preferredcodec': 'mp3',
      'preferredquality': '192',
  }],
  'extract_audio': True,
}

def search_song(song_name):
  videosSearch = VideosSearch(song_name, limit = 1)
  return videosSearch.result()['result'][0]['link']

def download_song(song_name):
  song_url = search_song(song_name)
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      ydl.download([song_url])

if __name__ == "__main__":
  while True:
      song_name = input("What song do you want to download? ")
      if song_name.lower() == 'exit':
          break
      download_song(song_name)
