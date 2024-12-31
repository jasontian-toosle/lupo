import shutil, os, glob, subprocess
import time
from datetime import datetime



# start=15
# end=19

# merge your multiple ts files to one ts file.
cwd = os.getcwd()
TS_DIR = 'ts_files'
list_of_files = filter( os.path.isfile, glob.glob(cwd + '/'+TS_DIR + '/' + '*') )
list_of_files = sorted( list_of_files, key = os.path.getmtime)
with open('merged.ts', 'wb') as merged:
    for ts_file in list_of_files:
        with open(ts_file, 'rb') as mergefile:
            print(mergefile.name)
            shutil.copyfileobj(mergefile, merged)

            # merge with index
            # file_number = mergefile.name[mergefile.name.find('media')+6: mergefile.name.find('.ts')]
            # print(file_number)
            # if (int(file_number) >= start and int(file_number) <= end):
                # print(mergefile.name)
                # shutil.copyfileobj(mergefile, merged)

# convert ts to mp4
infile = cwd + '/'+ 'merged.ts'
outfile = cwd + '/'+ 'merged.mp4'

subprocess.run(['ffmpeg', '-i', infile, outfile])
# input = ffmpeg.input(infile)
# audio = input.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
# video = input.video.hflip()
# out = ffmpeg.output(audio, video, 'out.mp4')