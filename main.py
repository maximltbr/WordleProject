with open("solutionsupdated.txt") as f:
    solutions = eval(f.read())
with open("wordsupdated.txt") as f:
    words = eval(f.read())
with open("total.txt") as f:
    totalwords = eval(f.read())
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

end = 0
while end == 0:
    userguess = []
    verify = 0
    verify2 = 0
    while verify2 == 0:
        guess1 = input("What was your guess? ")
        guess1 = guess1.lower()
        while verify == 0:
            if len(guess1) == 5:
                for letter in guess1:
                    userguess.append(letter)
                verify += 1
            else:
                print("Incorrect amount of letters")
        if userguess in totalwords:
            verify2 += 1
        else:
            print("Not possible")
    result = []
    verify = 0
    while verify == 0:
        result1 = input("Results? (g = green, y = yellow, b = black) ")
        result1 = result1.lower()
        if len(result1) == 5:
            for letter in result1:
                result.append(letter)
            verify += 1
        else:
            print("fail.")
    count = 0
    dummy = 0
    newsolution = []
    yellowletters = []
    blackletters = []
    greenletters = []
    wordresult = [result, userguess]
    counter = 0
    while counter < 5:
        if wordresult[0][counter] == "y":
            yellowletters.append(wordresult[1][counter])
            counter += 1
        elif wordresult[0][counter] == "b":
            blackletters.append(wordresult[1][counter])
            counter += 1
        elif wordresult[0][counter] == "g":
            greenletters.append(wordresult[1][counter])
            counter += 1
    counter = 0
    while counter < 5:
        newfilter = []
        if userguess[counter] in blackletters:
            for word in solutions:
                if userguess[counter] not in word:
                    newfilter.append(word)
        if userguess[counter] in greenletters:
            for word in solutions:
                if word[counter] == userguess[counter]:
                    newfilter.append(word)
        if userguess[counter] in yellowletters:
            for word in solutions:
                if userguess[counter] != word[counter] and userguess[counter] in word:
                    newfilter.append(word)
        solutions = newfilter
        counter += 1

    if len(solutions) == 1:
        final = ''.join(solutions[0])
        print("The solution is", final)
        end = 1
    else:
        alphabetscores = []
        for letter in alphabet:
            score = 0
            for word in solutions:
                if letter in word:
                    score += 1
            alphabetscores.append(score)
        updatedscores = dict(zip(alphabet, alphabetscores))
        print(updatedscores)
        highest = 0
        suggestions = []
        for word in solutions:
            wordscore = 0
            lettersused = []
            for letter in word:
                if letter not in lettersused:
                    lettersused.append(letter)
            for letter in lettersused:
                wordscore += updatedscores[letter]
            if wordscore >= highest:
                highest = wordscore
                suggestions.append(word)
        print("Try", suggestions[-1])








