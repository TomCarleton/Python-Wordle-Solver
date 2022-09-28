# Assign score weight values
greenVal = 10
yellowVal = 5
dupePen = 2
commonBonus = 2

with open('wordlewords.txt') as f:
			wordleWordList = list(f)

with open('words.txt') as g:
			acceptedWordList = list(g)

class Word:
    def __init__(self, string):
        self.word = string
        self.score = 0

        for wordleWord in wordleWordList:
            for i in [0,1,2,3,4]:
                # Checking for green tiles, i.e. perfect letter match
                if self.word[i] == wordleWord[i]:
                    self.score += (greenVal - yellowVal)
                # Checking for yellow tiles, i.e. letter matches anywhere
                for j in [0,1,2,3,4]:
                    if self.word[i] == wordleWord[j]:
                        self.score += yellowVal

        self.score = self.score / len(wordleWordList)

        # Gives a score penalty for repeating letters
        for i in [0,1,2,3,4]:   
            jList = [0,1,2,3,4]
            jList.remove(i)
            for j in jList:
                if self.word[i] == self.word[j]:
                    self.score -= (dupePen / 2)

        # Gives a score bonus if word is common
        if self.word in wordleWordList:
            self.score += commonBonus

        #print(self.word + " - " + str(self.score))


# Put all words and associated scores into a list
unsortedList = list()
for tryWord in acceptedWordList:
    word1 = Word(tryWord)
    unsortedList.append(word1)

# Sort the unsorted list based on word score
sortedList = list()
while len(unsortedList) != 0:
    bestScore = -1
    bestIndex = 0
    currentIndex = 0
    for sortWord in unsortedList:
        if sortWord.score > bestScore:
            bestScore = sortWord.score
            bestIndex = currentIndex
        currentIndex += 1
    sortedList.append(unsortedList[bestIndex])
    unsortedList.pop(bestIndex)

# Export sorted word list to sortedwords.txt
with open('sortedwords.txt', 'w') as h:
    for writeWord in sortedList:
        h.write(writeWord.word)