clc;
clear all;

nchan=6;
event_num=2000;
fs=16000;

for num=1:event_num

    % Load input files
    for c=1:nchan,
        x(:,c)=wavread(['../2019_KETI_NOISE\SEP/caffe/machine/CH/machine' '_num' int2str(num) '_ch'  int2str(c) '.wav']);
    end

    wavwrite(x,fs,['../2019_KETI_NOISE\SEP/caffe/machine/machine' '_num' int2str(num) '.wav']);


end

    % Load input files
%     for c=1:nchan,
%         x(:,c)=wavread(['../2020_02_24_NOISE/WAV/restroom/wash_basin/Track ' int2str(c) '_001.wav']);
%     end
% 
%     wavwrite(x,fs,['../2020_02_24_NOISE/WAV/restroom/wash_basin/wash_basin.wav']);


disp('wav write done.');
 
fclose('all');


            