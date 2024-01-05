
def main():

 with open("books/frankenstein.txt") as f:
  file_contents = f.read()
 return file_contents

def wordCount(file_contents):
 words = file_contents.split()
 return len(words)

def countLetters(file_contents):
 lowerContents = file_contents.lower()
 freq = {}
 for i in set(lowerContents):
  freq[i] = lowerContents.count(i)
  print(f"The '{i}' character appears {lowerContents.count(i)} times")
 return freq




file_contents =main() 
print("--- Starting book report for: books/frankenstein.txt ---")
print(f"There were {wordCount(file_contents)} words were found in the document")
print(countLetters(file_contents))
print("--- End Report ---")
