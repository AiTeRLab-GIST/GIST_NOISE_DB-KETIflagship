import os
import numpy as np
import glob
import librosa
import scipy

print('mjm')
  
wavs = glob.glob('../2019_KETI_NOISE/sep_backup/HOME/*_ch1_fan.wav')
 
output_file='../2019_KETI_NOISE/SEP/home/fan_test/'

wavs.sort()

time_len=160000
y_len=0
cnt =1
firtst_flag=0

y_sum=[]
y_PP=[]
y_p=[]
y_sum=np.array(y_sum)
y_p=np.array(y_p)
y_PP=np.array(y_PP)

for wav_fname in wavs:
    
    y,sr=librosa.load(wav_fname,mono=False,sr=16000)
    y_len=int(len(y)) 
    
    if(y_len >=time_len):
        for i in range(int(y_len/time_len)):
            y_PP=y[1+i*time_len:time_len+i*time_len]
            output_path= output_file+'fan'+'_num'+str(cnt)+'_ch1.wav'
            y_PP=y_PP*32768
            print(output_path)
            scipy.io.wavfile.write(output_path, sr ,y_PP.astype(np.int16))
            cnt=cnt+1

        

    
    
    
    
    
    
    
                                

