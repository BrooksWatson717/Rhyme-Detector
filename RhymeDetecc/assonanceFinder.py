import lyricScrub
import nltk
from nltk.tokenize import word_tokenize, WhitespaceTokenizer, wordpunct_tokenize
from nltk.corpus import cmudict

wordList = {}
keyList = []
assonanceList = []
vowels = ["AA0", "AE0", "AH0", "AO0", "AW0", "AY0", "EH0", "EY0", "IH0", "IY0", "OW0", "OY0", "UH0", "UW0", "AA1", "AE1", "AH1", "AO1",
          "AW1", "AY1", "EH1", "EY1", "IH1", "IY1", "OW1", "OY1", "UH0", "UW0", "AA2", "AE2", "AH2", "AO2", "AW2", "AY2", "EH2", "EY2", "IH2", "IY2",
          "OW2", "OY2", "UH2", "UW2", "ER1"]
vowelDict = {}

Done = False


# Highlights the words that have the same vowel sound
def highlighter(lyrics):
    start = '<p>'
    end = '</span>'
    global Done
    global Lyrics
    for i in range(0, len(lyrics)):
        if lyrics[i] in vowelDict['AO1']:
            lyrics[i] = '<span style="background-color: #ccffcc;">' + lyrics[i] + end
        if lyrics[i] in vowelDict['AH1'] or lyrics[i] in vowelDict['AH2']:
            lyrics[i] = lyrics[i] = '<span style="background-color: #f2a0a0;">' + lyrics[i] + end
        if lyrics[i] in vowelDict['EY1'] or lyrics[i] in vowelDict['EY2']:
            lyrics[i] = lyrics[i] = '<span style="background-color: #ffff99;">' + lyrics[i] + end
        if lyrics[i] in vowelDict['AY1'] or lyrics[i] in vowelDict['AY2']:
            lyrics[i] = lyrics[i] = '<span style="background-color: #cc99ff;">' + lyrics[i] + end
        if lyrics[i] in vowelDict['AE1'] or lyrics[i] in vowelDict['AE2']:
            lyrics[i] = lyrics[i] = '<span style="background-color: #99ccff;">' + lyrics[i] + end
        if lyrics[i] in vowelDict['IY1'] or lyrics[i] in vowelDict['IY2'] or lyrics[i] in vowelDict['IY0']:
            lyrics[i] = lyrics[i] = '<span style="background-color: #ffcc99;">' + lyrics[i] + end
        if lyrics[i] in vowelDict['ER1']:
            lyrics[i] = lyrics[i] = '<span style="background-color: #ed95d3;">' + lyrics[i] + end
        if lyrics[i] in vowelDict['EH1'] or lyrics[i] in vowelDict['EH2']:
            lyrics[i] = lyrics[i] = '<span style="background-color: #89e8e6;">' + lyrics[i] + end
        if lyrics[i] in vowelDict['OY1'] or lyrics[i] in vowelDict['OY2']:
            lyrics[i] = lyrics[i] = '<span style="background-color: #95ff80;">' + lyrics[i] + end
        if lyrics[i] in vowelDict['OW0'] or lyrics[i] in vowelDict['OW1'] or lyrics[i] in vowelDict['OW1']:
            lyrics[i] = lyrics[i] = '<span style="background-color: #cfb480;">' + lyrics[i] + end
    for i in range(0, len(lyrics) - 1):
        if lyrics[i] == '<br/>':
            lyrics[i + 1] = lyrics[i + 1].capitalize()
        if lyrics[i] == 'i':
            lyrics[i] = lyrics[i].capitalize()
    Lyrics = ' '.join(lyrics)
    Done = True


# Stores words into a list grouped by vowel sound
def vowel_Finder(songs):
    list = songs
    for i in range(0, len(vowels)):
        vowelDict[vowels[i]] = []
    j = 0
    for i in range(0, len(vowels)):
        for k in range(0, len(keyList)):
            if vowels[i] in wordList[keyList[k]]:
                if keyList[k] not in vowelDict.values():
                    vowelDict[vowels[i]].append(keyList[k])
        i += 1
    highlighter(list)


# SPLITS SONG INTO VERSES
def get_Lyric_Sounds(verseNumber):
    number_of_verse = str(verseNumber)
    superSong = ''.join(lyricScrub.LYRICS)
    # Allows lines to be reprinted as new lines when necessary
    mytext = " <br/> ".join(superSong.split("\n"))
    mytext2 = " ".join(mytext.split("-"))  # Splits hyphenated words
    songLyrics = WhitespaceTokenizer().tokenize(mytext2)
    for i in range(0, len(songLyrics)):
        # Makes the search in the next for-loop faster and more accurate
        songLyrics[i] = songLyrics[i].lower()
        songLyrics[i] = songLyrics[i].replace(",", "")

    # Fetches the pronunication of each word and stores it in a dictionary
    for (word, pron) in cmudict.entries():
        if word in songLyrics:
            if word != 'the' and word != "and":
                wordList[word] = pron

    # Create a list of words in the verse
    for key in wordList:
        if len(wordList[key]) > 1:
            keyList.append(key)
    vowel_Finder(songLyrics)
