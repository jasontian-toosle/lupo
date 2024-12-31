import requests, shutil, m3u8, os, glob, subprocess
import time
from datetime import datetime
import logging

def strip_end(text, suffix):
    if not text.endswith(suffix):
        return text
    return text[:len(text)-len(suffix)]

def download_file(url, local_filename):
    print(local_filename)
    r = requests.get(url, stream=True)
    with open(f"ts_files/{local_filename}", 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    return local_filename



#https://s3-e1.dnvodcdn.me/ppot/_definst_/mp4:s11/jvod/lxj-zsrjyhs-02-014013849x8nz.mp4/chunklist.m3u8?dnvodendtime=1682906019&dnvodhash=GLylpFDalL5PxOAQpejPHX-sV3BzPqbUEvcjT-H13ws=&dnvodCustomParameter=571973_2601%3a646%3a9b80%3a7050%3ad1d9%3a263f%3a404c%3a4b16.US_1&lb=2e021d34c5168d1c64386eca2c78dd08&us=1&vv=59ea06c9343c784611031dbd3678f11f&pub=CJOuCZSoEJOnDoumDZbVLLDVCZOmCJesD3OwEM8uC3etC3KmEcGnP3awCZOpPZeqC3HZEZHYCJPVD30uOcOrE65XOcGsD6GmDpauE3DaOJanCJ8oD64uDc5VD3WrDJSnP3WrDZKtPcCmDM9aPZ0mOMOpEM4vDJauOs1

# get list of ts files
m3u8_url = 'https://s3-e1.dnvodcdn.me/ppot/_definst_/mp4:s3/ivod/lxj-pfzl-01-02E56FFAA5flg.mp4/chunklist.m3u8?dnvodendtime=1684745792&dnvodhash=PhiN-d1_Sp13odjj7Y7Kpc_jQl2De8TILQWPnu45v24=&dnvodCustomParameter=0_2601%3a646%3a9b80%3a7050%3a808b%3ab495%3a4ae2%3a9edf.US_1&lb=874c1fd9e91439753a42b8cb48c248ad&us=1&vv=a565d98a17b3929180a7a631391e349d&pub=CJOuD3KsEJCvCIuqC3LVLLDVCZOmCJesD3OwEM8uC3etC3KmEZWmE68wOZGvDJeqOMKoEZbbP6PVOMCsE3LYOJWoDJKoD3XZDc9ZCZOoCJ8uOZDcEJ9aCpDVPcGvC3baCZWpDp4oP65YOJ0qOJWmOJTYCMCvDMHbOp2'
r = requests.get(m3u8_url)
m3u8_master = m3u8.loads(r.text)

# get prefix url
m3u8_file = m3u8_url.split('/')[-1]
url = strip_end(m3u8_url, m3u8_file)
url_copy = url
print(url_copy)

# create ts folder
if not os.path.exists('ts_files'):
    print('ts_file folder is not found, creating the folder.')
    os.makedirs('ts_files')

# print statement can be deleted, they were placed prior to debugging purposes.
for seg in m3u8_master.data['segments']:
    append_url = seg['uri']
    local_filename = append_url.split('?')[0]
    url += append_url
    print(f'downloading {seg["uri"]}')
    download_file(url, local_filename)
    url = url_copy


# merge files
cwd = os.getcwd()
TS_DIR = 'ts_files'
list_of_files = filter( os.path.isfile, glob.glob(cwd + '/'+TS_DIR + '/' + '*') )
list_of_files = sorted( list_of_files, key = os.path.getmtime)

# merge every 45 ts files to one ts file. each one around 10 mins
size = 45
count = 0
index = 0
start = 0
end = len(list_of_files)
while start < end:
    part_done = False
    with open('merged_{}.ts'.format(index), 'wb') as merged:
        while not part_done:
            if start >= end:
                break
            ts_file = list_of_files[start]
            with open(ts_file, 'rb') as mergefile:
                print(mergefile)
                shutil.copyfileobj(mergefile, merged)
            count += 1
            start += 1
            if count > size:
                count = 0
                index += 1
                part_done = True


for i in range(index+1):
    infile = cwd + '/'+ 'merged_{}.ts'.format(i)
    outfile = cwd + '/'+ 'merged_{}.mp4'.format(i)
    subprocess.run(['ffmpeg', '-i', infile, outfile])


# merge all files to one single merged.ts
# with open('merged.ts', 'wb') as merged:
#     for ts_file in list_of_files:
#         with open(ts_file, 'rb') as mergefile:
#             print(mergefile)
#             shutil.copyfileobj(mergefile, merged)


# convert ts to mp4
# infile = cwd + '/'+ 'merged.ts'
# outfile = cwd + '/'+ 'merged.mp4'
# subprocess.run(['ffmpeg', '-i', infile, outfile])
# input = ffmpeg.input(infile)
# audio = input.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
# video = input.video.hflip()
# out = ffmpeg.output(audio, video, 'out.mp4')