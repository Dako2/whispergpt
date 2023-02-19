""" test machine capability for whisper model 
follow the Open-Ai/Whisper Installation: https://github.com/openai/whisper
0. I'm using wsl so maybe install wsl first ??
1. install Python 3.9.9
2. 

Check:
1. inference time
2. memory 
3. gpu

"""

import whisper
import time
import torch

audiofile = "jfk.wav"

for model_name in ["tiny","base", "small"]:
    _ = whisper.load_model(model_name)


print("analyzing ...")

for model_name in ["tiny","base", "small"]:
    
    print("%s ..."%model_name)

    model = whisper.load_model(model_name) #CPU
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audiofile)
    audio = whisper.pad_or_trim(audio)

    t0 = time.time()

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # decode the audio
    options = whisper.DecodingOptions(fp16 = False)
    result = whisper.decode(model, mel, options)

    dt = int((time.time() - t0) * 1000)

    # print the recognized text
    print(model_name, ",", dt, "ms, ", result.text)

"""
pip uninstall torch
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
"""
if torch.cuda.is_available():
    device = "cuda"
    try:
        for model_name in ["tiny","base", "small", "medium"]:
            model = whisper.load_model(model_name, device = device)
            # load audio and pad/trim it to fit 30 seconds
            audio = whisper.load_audio(audiofile)
            audio = whisper.pad_or_trim(audio)

            t0 = time.time()

            # make log-Mel spectrogram and move to the same device as the model
            mel = whisper.log_mel_spectrogram(audio).to(model.device)

            # decode the audio
            options = whisper.DecodingOptions(fp16 = False)
            result = whisper.decode(model, mel, options)

            dt = int((time.time() - t0) * 1000)

            # print the recognized text
            print(dt, "ms, ", result.text)

    except:
        print("somehow GPU not working..")
else:
    print("no gpu detected in this machine")

