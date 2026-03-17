import re
clean=lambda t:re.sub('[^a-z ]','',t.lower())
clean_text=clean
