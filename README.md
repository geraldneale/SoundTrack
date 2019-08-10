# SoundTrack
Summary:
A group of Jupyter Notebooks that plays your music on a weekly schedule and shuffles song in between to fit the gaps. Written in Python3 and SQLite. It runs on Linux and plays to connected browser. Really cool Raspberry Pi (3 or higher) project.

Helpful Hints:
1. Use youtube-dl command line tool to populate shuffle folder(https://ytdl-org.github.io/youtube-dl/index.html)
  My config file looks like this:
  #Lines starting with # are comments
  #Always extract audio
  -x
  #use highest quality
  --audio-quality 0
  #mp3 only
  --audio-format mp3
  #remove spaces and special characters in file name
  --restrict-filenames
  #--get-filename -o '%(title)s.%(ext)s'
  -o '%(title)s.%(ext)s'
  
  For example(only use this tool on legally distributable content like Steadman and Creative Commons songs): 
  youtube-dl https://www.youtube.com/watch?v=ctCsZiQE_rQ
  [youtube] ctCsZiQE_rQ: Downloading webpage
  [youtube] ctCsZiQE_rQ: Downloading video info webpage
  [download] Destination: 4_Steadman_-_Good_To_Go.webm
  [download] 100% of 3.77MiB in 00:00
  [ffmpeg] Destination: 4_Steadman_-_Good_To_Go.mp3
  Deleting original file 4_Steadman_-_Good_To_Go.webm (pass -k to keep)

Todo (20190806):
1. Upload database creation scripts.
2. Get working over a smart phone browser(IPython.display.Audio autoplay non-functioning).
3. Get working in a Tesla browser through group nightly prayer to Tesla's update team to allow HTML 5 sound of any kind.

Special thanks to:

David Laganella - Master composer, virtuoso, author and professor.
  (https://en.wikipedia.org/wiki/David_Laganella)
  
Jackie Neale - Artist.(https://jackiephoto.photoshelter.com/index)  

Tim Seyfarth Garner - Musician, songwriter and producer.

Timmy Garner - Friend.

Concept:
Soundtrack is my ultimate mix tape for today. 

In 1985, for a friend, I might have created a 90 minute cassette tape as follows; to start the first 45 minute side I'd play a song that my audience and I share enthusiasm for, followed by 2-3 selections of songs that I thought my audience doesn't know yet but would like just as much as the first, the rest of the side would be stuff I'm listening to in a curated manner (ascending tempo to a climax at the latest the 40th minute and a slow song to end the side). A little blank space after the last song is acceptable on the first side. The second 45 minute side of a mix tape cassette would start with a slammer, then songs I like currently with the same rise and fall of tempo and intensity as the first side. The final song inevitably ends with some blank space left and that's where I put my signature 30 second sample of David Brubeck, Mozart, Beethoven, Puccini, etc something classic, intensely sweet, and just as you might want another bite the end of the cassete tape would go POP!     

It's now 2019. We can connect to music from anywhere with an internet connection. We can tell precise time to the second.
