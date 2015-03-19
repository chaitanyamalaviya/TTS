

FID = fopen('ch1.wrd', 'r');
if FID == -1, error('Cannot open file'), end
%Data = textscan(FID, '%s', 'delimiter', '\n', 'whitespace', '');
%CStr = Data{1};

C = textscan(FID,'%s %s %s');
fclose(FID);
%disp(C(endpos));

inputstr = 'THE';


for i = 1 : 5260
    if  strcmp(C{3}{i},inputstr)==1
        startpos = C{1}{i};
        endpos = C{2}{i};
    end
end

startpos = round(str2double(startpos)*Fs);
endpos = round(str2double(endpos)*Fs);
%Play the segment
[y, Fs] = audioread('ch1.wav');
[y3, Fs] = audioread('ch1.wav', [startpos,endpos]);
sound(y3, Fs);