# whispergpt
whisper.cpp + chatgpt api => ASR chatbot

whisper.cpp installation procedure:
https://github.com/ggerganov/whisper.cpp
It integrates vad (voice activation detection) + streaming ASR in C++ and operates well in Macbook 
(no clear solution found on how to compile in Windows) 

there seems to be no existing github solution for ChatGPT + Streaming ASR service

Whisper seems to be a nice solution for ASR> though might be some instability existing and resource heavy 

ChatGPT API hasn't been open yet but expected to be soon
https://github.com/openai/openai-python

The goal of this project is to provide a quick and dirty solution for ASR + Chatgpt bot that is readily available to integrate into a GAME engine
