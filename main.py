import random
from utils import clean_words, read_file

def green(words):
    out = "\033[30;102m"
    out += words
    out += "\033[0m"
    return out

def orange(words):
    out = "\033[30;103m"
    out += words
    out += "\033[0m"
    return out

def white(words):
    out = "\033[30;107m"
    out += words
    out += "\033[0m"
    return out

def strip_cleaned_words(words, length_of_word):
  dummy_words = []
  for ele in words:
    if len(ele) == length_of_word:
        ele = ele.lower()
        dummy_words.append(ele)
  return dummy_words

def read_words(length_of_word=5):
  print("importing the word list")
  raw_words = read_file('words')
  cleaned_words = clean_words(raw_words)
  striped_words = strip_cleaned_words(cleaned_words, length_of_word)
  return striped_words

# def read_words(length_of_word=5):
#   print("importing the word list")
#   striped_words = []
#   with open("words","r") as f:
#     words = f.readlines()
#     for word in words:
#       temp = word.strip("\n")
#       if len(temp) == length_of_word:
#         temp = temp.lower()
#         striped_words.append(temp)
#   return striped_words

def main():
    words = read_words()
  
    # words = ["water", "worry"]
    spec = random.randint(0,len(words)-1)
    actual = words[spec]
    # actual = "water"
    end = False
    guess_count = 0
    max_guess = 6

    while not end:
      guess_count += 1
      if guess_count <= max_guess:
        print(f"Enter your guess:\n ({guess_count} / {max_guess}):")
        guess = input()
        guess = guess.lower()
        if guess in words:
          if len(guess) == len(words[0]):
            if guess == actual:
              print("You guessed right!")
              print(orange(guess))
              break

            output = ""
            for i, char in enumerate(guess):
              if char in actual:
                if char == actual[i]:
                  output += orange(char)
                else:
                  output += green(char)
              else:
                output += white(char)
            print(output)
          else:
            print("Enter a new word you cunt")
            guess_count -= 1
        else:
          print("Bad word you cunt")
          guess_count -= 1
    else:
        print(f"unlucky you didn't get it, the word was {actual}")
        end = True


if __name__ == "__main__":
  print("test")
  main()
