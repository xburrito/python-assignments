count = 1

with open('win95coolest.txt') as text:
  for line in text:
    word_count = len(line.split())
    char_count = len(line)-(line.count(" ")+1)

    if (word_count == 0):
      avg_words = 0
    else:
      avg_words = (char_count / word_count)

    print(count, word_count, avg_words, line)
    count += 1
