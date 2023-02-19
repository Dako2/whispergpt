import subprocess
import time
import keyboard
from gpt import chatgpt_api

import os
import sys
import queue 
import threading

PATH_TO_WHISPER = os.path.abspath('/whisper.cpp')

process = None
def start_subprocess(command):
    global process
    try:
        # Start the stream.cpp executable in a new process
        print("start whisper")
        process = subprocess.Popen(command, )
        """
        # Wait for the process to finish and capture its output
        output, errors = process.communicate()
        # Print the output
        print(output.decode())
        """
    except KeyboardInterrupt:
        print("Terminating process...")
        process.terminate()

command = ["./%s/stream"%PATH_TO_WHISPER, "-m", "./%s/models/ggml-small.bin"%PATH_TO_WHISPER, "-t", "6", "-l", "zh", "--step", "0", "--length", "30000", "-vth", "0.6"]
start_subprocess(command)

time.sleep(5)

# Keep monitoring the log file for new text
logfile = "log.txt"


class PromptQueue:
    def __init__(self, maxsize=0):
        self.queue = queue.Queue(maxsize=maxsize)
    
    def add_prompt(self, prompt):
        self.queue.put(prompt)
    
    def process_prompt(self):
        prompt0 = ""
        while True:
            prompt = self.queue.get()
            if prompt != prompt0:
                # Perform ChatGPT inference on the prompt
                response = chatgpt_api(prompt)
            print(response)
            
            self.queue.task_done()
            prompt0 = prompt
    
    def start_processing(self):
        processing_thread = threading.Thread(target=self.process_prompt)
        processing_thread.start()

prompt_queue = PromptQueue(3)
prompt_queue.start_processing()

with open(logfile, "r") as f:
    while True:
        # Read new lines from the log file
        new_lines = f.readlines()

        # If there are new lines, print them to the console and generate text
        if new_lines:
            for prompt in new_lines:
                prompt_queue.add_prompt(prompt)

        # Check if the stream.cpp process is still running
        if process.poll() is not None:
            # Process has terminated, stop monitoring the log file
            break

        # Wait for a short time before checking for new log lines
        time.sleep(0.5)


# Process has terminated, print its exit code
print("Process exited with code", process.returncode)



























