# This function returns the total number of tweets
def totalNumberOfTweets(s):
  line_num = 0
  for line in s:
    line_num += 1
  print("Number of Tweets:", line_num);
  print()

# This function will return the tweet with the most number of words
def tweetWithMostWords(s):
  longest_tweet_wordCount = 0
  string_sentence = ""
  for words in s:
    count = len(words.split())
    if (longest_tweet_wordCount < count):
      longest_tweet_wordCount = count;
      string_sentence = words
  print("Tweet with max number of words:", string_sentence)

# Function makes all the words lowercase
def cleanedup(s):
  cleantext = []
  for word in s:
    cleantext.append(word.lower())
  return cleantext

def hashtagTextFinder(s):
  read_file = s.read().split(' ')
  hashtag_words=[] # list to store hashtag contained words
  occurrences = [] # list which contains occurence of words having hashtag
  new_s = cleanedup(read_file)

  #Reads content containging a '#' and adds it to the list
  for line in new_s:
    if line.startswith('#'):
      hashtag_words.append(line)

  #used to get occurrences of words
  for i in range(len(hashtag_words)): 
    words = hashtag_words[i]
    occurrences.append(words)

  while True:
    # Request user input
    word = input('Enter hashtag: ')
    # Prints number of occurrences of entered word
    if word in occurrences:
      print('Mentioned',occurrences.count(word),'times')
      print()
    else:
      print('Not mentioned.')
      print()

# Driver Code
with open('elon-musk.txt', 'r') as file:
  totalNumberOfTweets(file)

with open('elon-musk.txt', 'r') as file:
  tweetWithMostWords(file)

with open('elon-musk.txt', 'r') as file:
  hashtagTextFinder(file)
