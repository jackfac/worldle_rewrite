
def clean_words(words):
  temp_words = []
  for word in words:
    temp = word.strip("\n")
    temp_words.append(temp)
  return temp_words

def read_file(filename):
  with open(filename,"r") as f:
    words = f.readlines()
  return words