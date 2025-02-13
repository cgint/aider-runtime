from aider.coders import Coder
from aider.models import Model
from aider.io import InputOutput
import os
import sys

action = "Add or adapt all method comments so they reflect the intent for users of the function. Mention parametes but only if it really adds to the understanding."
fnames = ["watcher_google_ads.py"]
# Check if all files exist
for fname in fnames:
    if not os.path.isfile(fname):
        print(f"File {fname} does not exist.")
        sys.exit(1)


model_name = "gpt-4o" # "gemini/gemini-1.5-pro-latest"
model = Model(model_name)

# Create a coder object
coder = Coder.create(main_model=model, fnames=fnames, io=InputOutput(yes=True))

# This will execute one instruction on those files and then return
coder.run(action)