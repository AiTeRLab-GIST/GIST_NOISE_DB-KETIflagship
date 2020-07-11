import os
import numpy as np
import glob
import librosa
import scipy
  
wavs = glob.glob('../2020_02_24_NOISE/WAV_BACK/restroom/wash_basin/*.wav')
 
output_file='../2020_02_24_NOISE/SEP/restroom/wash_basin/CH/'

label_path ='restroom_wash_basin_label.csv'

for wav_fname in wavs:
    
    print(wav_fname)
    y,sr=librosa.load(wav_fname,mono=False,sr=16000)
    
    ch=wav_fname.split('Track ')[-1].split('_')[0]
    print(ch)
        
    f = open(label_path, 'r')
    lines = f.readlines()
            
    for line in lines:
        event=line.split(',')[0]
        num=int(line.split(',')[1])
        start=int(line.split(',')[2])
        end=int(line.split(',')[3])
    
        y_event= np.zeros(160000)
        y_event[8000:8000+end-start]=y[start:end]
        y_event=y_event*32768
        
        output_path= output_file+str(event)+'_num'+str(num)+'_ch'+ch+'.wav'
        print(output_path)
        scipy.io.wavfile.write(output_path, sr ,y_event.astype(np.int16))
        

