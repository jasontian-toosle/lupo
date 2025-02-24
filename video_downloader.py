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
    r = requests.get(url, stream=True, headers=headers)
    with open(f"ts_files/{local_filename}", 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    return local_filename
     
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}


s1='https://s6-e1.pipecdn.vip/ppot/_definst_/mp4:s15/kvod/dhp-wdzsj-01-03B2E9786dz0z.mp4/chunklist.m3u8?vendtime=1737360701&vhash=PrDZKroP08ZntlWdW-x2OXo3dBQJkah0vGDdLJJTn8M=&vCustomParameter=571973_2601.646.a081.7a20.6c9b.b15c.eeab.cac2_US_1_0&lb=907d804cdc4a4c9d32b2c73109ba9c61&us=1&vv=37ba80351eeae341918668abe2e6e63a&pub=CJSpDp4uCZ8qC2unDp9VLLDVCZOmCJesD3OwOJ0uCJetOJ8mEZPZEM8wOZ4rOpfbPM5YEcDXOp9VE3TXOMKsCMOmDMCvD30pCZaoP3WoCJKuDJasE6HbOp9VD3OrCM5bP3DZEMGrDsGuCMGqPJKnOJ0mCZOnP64oD63'
s2='https://s6-e1.pipecdn.vip/ppot/_definst_/mp4:s6/gvod/dhp-wdzsj-02-01970DC3Azug1.mp4/chunklist.m3u8?vendtime=1737360764&vhash=E1l5YSO4ddSqho9kqeLFrS30f0Ah8KLrnuSEUqCywOA=&vCustomParameter=571973_2601.646.a081.7a20.6c9b.b15c.eeab.cac2_US_1_0&lb=4668a305922411a774b63d8a4e3372b5&us=1&vv=b6ef39502fb08e46a43f3354836b72cc&pub=CJSpDp4uCZ8qC2unDp9VLLDVCZOmCJesD3OwOJ0uCJetOJ8mEZPZEM8wOZ4rOpfbPM5YEcDXOp9VE3TXOMKsCMOmDMCvD30pCZaoP3WoCJKuDJasE6HbOp9VD3OrCM5bP3DZEMGrDsGuCMGqPJKnOJ0mCZOnP64oD63'
s3='https://s3-e1.pipecdn.vip/ppot/_definst_/mp4:s11/jvod/dhp-wdzsj-03-03B3E3FD30p9q.mp4/chunklist.m3u8?vendtime=1737360781&vhash=tfRdU2WKHzQlCR73LLZ_gwpG74_VeQ0vgj5I1ZnZT1Q=&vCustomParameter=571973_2601.646.a081.7a20.6c9b.b15c.eeab.cac2_US_1_0&lb=808b2eaf7e1fb0edc495be54a500c893&us=1&vv=bf36a9865913053c1478026b67589a3d&pub=CJSpDp4uCZ8qC2unDp9VLLDVCZOmCJesD3OwOJ0uCJetOJ8mEZPZEM8wOZ4rOpfbPM5YEcDXOp9VE3TXOMKsCMOmDMCvD30pCZaoP3WoCJKuDJasE6HbOp9VD3OrCM5bP3DZEMGrDsGuCMGqPJKnOJ0mCZOnP64oD63'
s4='https://s6-e1.pipecdn.vip/ppot/_definst_/mp4:s6/live/dhp-wdzsj-04-00A840322g6fk.mp4/chunklist.m3u8?vendtime=1737360796&vhash=1Jnx3ON69Iuh8WdUX9_W_zLGwLct9aJ60CiYoTsYhFs=&vCustomParameter=571973_2601.646.a081.7a20.6c9b.b15c.eeab.cac2_US_1_0&lb=125f795baa08a725b864d15bd5eb33c7&us=1&vv=840e65831214630bd1f1db8e0e026630&pub=CJSpDp4uCZ8qC2unDp9VLLDVCZOmCJesD3OwOJ0uCJetOJ8mEZPZEM8wOZ4rOpfbPM5YEcDXOp9VE3TXOMKsCMOmDMCvD30pCZaoP3WoCJKuDJasE6HbOp9VD3OrCM5bP3DZEMGrDsGuCMGqPJKnOJ0mCZOnP64oD63'
s5='https://s6-e1.pipecdn.vip/ppot/_definst_/mp4:s15/gvod/dhp-wdzsj-5[720P]-0087C3B81ne3j.mp4/chunklist.m3u8?vendtime=1737360809&vhash=ueb0NZwyB10n5RtrBFhNA0Y6oPkEOHSiQMNZXfDu69s=&vCustomParameter=571973_2601.646.a081.7a20.6c9b.b15c.eeab.cac2_US_1_0&lb=0fd8b3997e393cc40755356b583425df&us=1&vv=1ddb26e90a7ec65fda96f2bd92ecc65a&pub=CJSpDp4uCZ8qC2unDp9VLLDVCZOmCJesD3OwOJ0uCJetOJ8mEZPZEM8wOZ4rOpfbPM5YEcDXOp9VE3TXOMKsCMOmDMCvD30pCZaoP3WoCJKuDJasE6HbOp9VD3OrCM5bP3DZEMGrDsGuCMGqPJKnOJ0mCZOnP64oD63'
s6='https://s6-e1.pipecdn.vip/ppot/_definst_/mp4:s15/ivod/dhp-wdzsj-06-034F0829Fxv1d.mp4/chunklist.m3u8?vendtime=1737360824&vhash=jx9-mzlgLLE6yOPtS4kYPFMghKzoBh3vVDs-3oMldsA=&vCustomParameter=571973_2601.646.a081.7a20.6c9b.b15c.eeab.cac2_US_1_0&lb=84de963dd3ded5398bf1df843081676d&us=1&vv=ea68bbe0ccc235c925ba1ec68d466816&pub=CJSpDp4uCZ8qC2unDp9VLLDVCZOmCJesD3OwOJ0uCJetOJ8mEZPZEM8wOZ4rOpfbPM5YEcDXOp9VE3TXOMKsCMOmDMCvD30pCZaoP3WoCJKuDJasE6HbOp9VD3OrCM5bP3DZEMGrDsGuCMGqPJKnOJ0mCZOnP64oD63'
s7='https://s10-e1.pipecdn.vip/ppot/_definst_/mp4:s13/live/dhp-wdzsj-07-01FA4D56Aye4c.mp4/chunklist.m3u8?vendtime=1737360841&vhash=Tupp9h7DOHte3VBhPlbihdRm3HU-UtMS5CNPiZrNbCA=&vCustomParameter=571973_2601.646.a081.7a20.6c9b.b15c.eeab.cac2_US_1_0&lb=5c1ded532c618c4d513b2cb2cea5638f&us=1&vv=b610dae2171e0fbfd7e3878cc59fbc29&pub=CJSpDp4uCZ8qC2unDp9VLLDVCZOmCJesD3OwOJ0uCJetOJ8mEZPZEM8wOZ4rOpfbPM5YEcDXOp9VE3TXOMKsCMOmDMCvD30pCZaoP3WoCJKuDJasE6HbOp9VD3OrCM5bP3DZEMGrDsGuCMGqPJKnOJ0mCZOnP64oD63'
s75='https://s5-e1.pipecdn.vip/ppot/_definst_/mp4:s14/dvod/dhp-wdzsj-75-01CFF80CB.mp4/chunklist.m3u8?vendtime=1737360920&vhash=1tW9zkAsZtfqoGuNCoCc-n0j2fj95VuU0hkpCmBuWlQ=&vCustomParameter=571973_2601.646.a081.7a20.6c9b.b15c.eeab.cac2_US_0_0&lb=e37e5ced3983cf8906b211671b4b9937'
s8='https://s10-e1.pipecdn.vip/ppot/_definst_/mp4:s13/hvod/dhp-wdzsj-08-00D0F038Evocv.mp4/chunklist.m3u8?vendtime=1737360935&vhash=qEiSlbmx7jnG7lJnOt7j3GJaLOlFkq6_id8TB_vhtmA=&vCustomParameter=571973_2601.646.a081.7a20.6c9b.b15c.eeab.cac2_US_0_0&lb='
s9='https://s6-e1.pipecdn.vip/ppot/_definst_/mp4:s15/jvod/dhp-wdzsj-09-031981C1Byhsm.mp4/chunklist.m3u8?vendtime=1737360946&vhash=NA5Vfwe-KTSzFcImcaNDdUkgNV6CRJbqK1jAnt7u4u4=&vCustomParameter=571973_2601.646.a081.7a20.6c9b.b15c.eeab.cac2_US_0_0&lb=e393ad4271a567c2da6819ff05da021f'
s10='https://s10-e1.pipecdn.vip/ppot/_definst_/mp4:s13/vod/dhp-wdzsj-10-036EE6CD9a1su.mp4/chunklist.m3u8?vendtime=1737360956&vhash=OgcyL-0UBpKRCUa4mG8ZuuSBNAad9PnMbg7sOGRcN0k=&vCustomParameter=571973_2601.646.a081.7a20.6c9b.b15c.eeab.cac2_US_0_0&lb=5ed1d63fc19af37819404ddac287f43a'
s11='https://s6-e1.pipecdn.vip/ppot/_definst_/mp4:s15/jvod/dhp-wdzsj-11-02DEAC918.mp4/chunklist.m3u8?vendtime=1737360965&vhash=vb93EmKynpgh0p5XTPeuxZr5Otvk2dShNTyQNpthSd8=&vCustomParameter=571973_2601.646.a081.7a20.6c9b.b15c.eeab.cac2_US_0_0&lb=a3ed58b2bdac0fe313b3793113e7e96f'
s12='https://s5-e1.pipecdn.vip/ppot/_definst_/mp4:s14/ivod/dhp-wdzsj-12-0105020F5.mp4/chunklist.m3u8?vendtime=1737360974&vhash=uRBkMMN-WrKweQtcO9wGDupAihxi7N7ZGw7RMqIx9d8=&vCustomParameter=571973_2601.646.a081.7a20.6c9b.b15c.eeab.cac2_US_0_0&lb=df40978064323c0c98dedf8337d9e052'

# get list of ts files
m3u8_url = s12
r = requests.get(m3u8_url, headers=headers)
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


# # merge files
cwd = os.getcwd()
TS_DIR = 'ts_files'
list_of_files = filter( os.path.isfile, glob.glob(cwd + '/'+TS_DIR + '/' + '*') )
list_of_files = sorted( list_of_files, key = os.path.getmtime)

# merge every 45 ts files to one ts file. each one around 10 mins
# size = 45
# count = 0
# index = 0
# start = 0
# end = len(list_of_files)
# while start < end:
#     part_done = False
#     with open('merged_{}.ts'.format(index), 'wb') as merged:
#         while not part_done:
#             if start >= end:
#                 break
#             ts_file = list_of_files[start]
#             with open(ts_file, 'rb') as mergefile:
#                 print(mergefile)
#                 shutil.copyfileobj(mergefile, merged)
#             count += 1
#             start += 1
#             if count > size:
#                 count = 0
#                 index += 1
#                 part_done = True


# for i in range(index+1):
#     infile = cwd + '/'+ 'merged_{}.ts'.format(i)
#     outfile = cwd + '/'+ 'merged_{}.mp4'.format(i)
#     subprocess.run(['ffmpeg', '-i', infile, outfile])


# merge all files to one single merged.ts
with open('merged.ts', 'wb') as merged:
    for ts_file in list_of_files:
        with open(ts_file, 'rb') as mergefile:
            print(mergefile)
            shutil.copyfileobj(mergefile, merged)


# convert ts to mp4 in OS
# infile = cwd + '/'+ 'merged.ts'
# outfile = cwd + '/'+ 'merged.mp4'
# subprocess.run(['ffmpeg', '-i', infile, outfile])
# input = ffmpeg.input(infile)
# audio = input.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
# video = input.video.hflip()
# out = ffmpeg.output(audio, video, 'out.mp4')


# convert ts to mp4 in Windows
# infile = cwd + '\\'+ 'merged.ts'
# outfile = cwd + '\\'+ 'merged.mp4'
# if os.path.exists(infile):
#     print("File exists.")
# else:
#     print("File does not exist.")

# command = ["ffmpeg", "-version"]
# try:
#     result = subprocess.run(command, capture_output=True, text=True, check=True)
#     print("FFmpeg version info:")
#     print(result.stdout)
# except FileNotFoundError:
#     print("FFmpeg is not installed or not in PATH.")
# except subprocess.CalledProcessError as e:
#     print("An error occurred:")
#     print(e.stderr)

# subprocess.run(['ffmpeg', '-i', infile, outfile])
# input = ffmpeg.input(infile)
# audio = input.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
# video = input.video.hflip()
# out = ffmpeg.output(audio, video, 'out.mp4')

print('done')

