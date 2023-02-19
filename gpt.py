import os
import openai 

API_KEY = "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"

def chatgpt_api(prompt, api_key = API_KEY): 

    if prompt.strip() is "":
        return ""

    openai.api_key = api_key
    print("You:      " + prompt.strip())

    try:
        """
        response = openai.Completion.create(
            engine = "davinci-codex", #text-curie-001, text-davinci-002, text-davinci-003, davinci-codex
            prompt = prompt, 
            temperature = 0.9,
            max_tokens = 100,
            top_p = 1.0,
            frequency_penalty = 0.0,
            presence_penalty = 0.0
        )"""

        #generated_text = response["choices"][0]["text"].strip()
        
        generated_text = prompt.strip() + "!!~~~~"

        print("chatgpt: " + "\033[91m" + generated_text + "\033[0m")
        return generated_text

    except:
        print("openai no reponse")
        return ""

if __name__ == "__main__":
    generate_text("why sky is blue")