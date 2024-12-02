import sys

import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_KEY"])
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

pseudocode = ""
with open(sys.argv[1]) as f:
   pseudocode = f.read() 


prompt = "Translate the following pseudocode into "+sys.argv[2]+", make your output NOT BE A CODE BLOCK and make sure to not make any syntax errors: \n"+pseudocode
response = model.generate_content(prompt)

# add more here later
langs = {
        "python" : ".py",
        "java"   : ".java",
        "c"      : ".c",
        "c++"    : ".cpp",
        "lua"    : ".lua",
        "javascript": ".js"
        }

suffix = langs[sys.argv[2].lower()]
filename = "code" + suffix

with open(filename, 'w') as f:
    f.write(response.text)

