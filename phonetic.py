def prepText(paragraph: str):
    """
    Function Description:
        Processes a paragraph of text to remove punctuation, convert all words to lowercase, and return a list of cleaned words.
    Parameter(s): 
        paragraph (str): The input paragraph as a string.
    Return:   
        wordList (list): A list of cleaned words extracted from the paragraph.
    """
    wordList = []
    
    paragraph = paragraph.strip().lower().split() 
    
    for word in paragraph:
        finalWord = ""
        for char in word:
            if (ord(char) >= 97 and ord(char) <= 122):
                finalWord += char
        wordList.append(finalWord)
    
    return wordList


def createDict(wordList: list):
    """
    Function Description:
        Creates a dictionary where each key is a letter (a-z), and the value is a list of words from the input that start with the corresponding letter.
    Parameter(s): 
        wordList (list): A list of cleaned words to be categorized by their starting letters.
    Return:   
        wordDict (dict): A dictionary where keys are letters and values are lists of words starting with those letters.
    """
    
    wordDict = {}
    
    for num in range(97, 123):
        wordDict[chr(num)] = []  
    
    for word in wordList:
        wordDict[word[0]].append(word)
        
    return wordDict

def main():
    """
    Function Description:
        Reads a paragraph, processes it to clean the text and extract words, then creates and displays a dictionary grouping words by their starting letters.
    Parameter(s): 
        None (Uses user input or predefined paragraph as input).
    Return:   
        None (Outputs the phonetic dictionary to the console).
    """
    
    wordList = prepText(paragraph)
    wordDict = createDict(wordList)
    
    print("\nThe Phonetic Dictionary:\n")
    for words in wordDict:
        print(f"{words}: {wordDict[words]}")

main()
