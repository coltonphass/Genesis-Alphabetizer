# Main function (driver)
def main():
    # Load and process text file
    print("Opening the Book of Genesis...")
    fileContent = readFile("genesis.txt")
    
    # Split text into a list of words
    wordList = splitText(fileContent)
    print("Found {} total words".format(len(wordList)))
    
    # Clean and deduplicate words
    uniqueWords = processWords(wordList)
    
    # Save and display results
    saveFile("genesis_words.txt", uniqueWords)
    print("\nComplete! Found {} unique words.".format(len(uniqueWords)))
    showSample(uniqueWords, 10)


# Helper functions

# Read the file content
def readFile(filePath):
    with open(filePath, "r") as file:
        return file.read()

# Split text into a list of words
def splitText(text):
    return text.split()

# Clean words and remove duplicates
def processWords(words):
    uniqueWords = []
    for word in words:
        cleanedWord = toUpper(word)
        if cleanedWord and cleanedWord not in uniqueWords:
            uniqueWords.append(cleanedWord)
    uniqueWords.sort()
    return uniqueWords

# Convert word to uppercase alphabetic characters only
def toUpper(word):
    result = ""
    for char in word:
        if char.isalpha():
            result += char.upper()
    return result

# Write words to a file
def saveFile(filePath, words):
    with open(filePath, "w") as file:
        for word in words:
            file.write(word + "\n")

# Display a sample of words
def showSample(words, count):
    print("\nHere are the first {} words to verify:".format(count))
    for i in range(min(count, len(words))):
        print(words[i])

# Start
main()
