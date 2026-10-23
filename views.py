import os
import re

content=[]
tagRecurrence=[]
fileRecurrence=[]
pathToTop10=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'MainFiles')

def main():
    global content
    global tagRecurrence
    global fileRecurrence
    global pathToTop10
    
    content = []
    tagRecurrence = []
    fileRecurrence = []
    
    pathToTop10=os.path.join(pathToTop10,"top10.html")
        
    initializeHTML()
    readLogFile()
    processContent()
    addToHTML()
    
    
def initializeHTML():
    global pathToTop10
    startingIndex = None 
    endingIndex  = None 
    found = 0
    with open(os.path.join(pathToTop10), 'r', encoding='utf-8') as top10File:
        lines = top10File.readlines()
    
    for lineNumber, line in enumerate(lines, 1):
            if '<div class ="recentStories">' in line: 
                found = 1
                startingIndex = lineNumber
            if '</div>' in line and found == 1:
                endingIndex = lineNumber 
                break

    if startingIndex  is not None and endingIndex is not None:
        del lines[startingIndex:endingIndex-1]

    with open(os.path.join(pathToTop10), 'w', encoding='utf-8') as top10File:
        top10File.writelines(lines) 
        top10File.close()


def readLogFile():
    global content
    log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'logs', 'access.log')
    searchedLine = "CapstoneProject/HTMLFiles"
    HTMLExtension= ".html"
    with open(log_file_path, 'r', encoding='utf-8') as currentFile:
        while True:
            for line_f in currentFile:
                if searchedLine in line_f and  HTMLExtension in line_f:
                    start=0
                    end=0
                    array = line_f.split()
                    # To be able to move to the next line
                    for i in range((len(array))):
                        if '"' in array[i]:
                            if start == 0:
                                start = i
                            else:
                                end = i
                    saveFileName(array[start+1:end])    
            char = currentFile.read(1)         
            # To mark the end of the File
            if not char:
                break
        # close the file
        currentFile.close() 




def getStoryTitle(storyFile):
    storyPath = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'HTMLFiles',
        storyFile
    )

    try:
        with open(storyPath, 'r', encoding='utf-8-sig') as file:
            content = file.read()

        match = re.search(
            r'<title>(.*?)</title>',
            content,
            re.IGNORECASE | re.DOTALL
        )

        if match:
            return match.group(1).strip().title()

    except FileNotFoundError:
        pass

    return os.path.splitext(storyFile)[0]

def processContent():
    global content
    global tagRecurrence
    global fileRecurrence

    tagRecurrence = []
    fileRecurrence = []

    htmlDirectory = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'HTMLFiles'
    )

    for storyFile in content:

        # Ignore tags and non-HTML files
        if "Tag" in storyFile or not storyFile.upper().endswith(".html"):
            continue

        # Ignore stories that no longer exist
        storyPath = os.path.join(htmlDirectory, storyFile)

        if not os.path.isfile(storyPath):
            continue

        # Count views only for existing stories
        if storyFile in fileRecurrence:
            index = fileRecurrence.index(storyFile)
            fileRecurrence[index + 1] += 1
        else:
            fileRecurrence.append(storyFile)
            fileRecurrence.append(1)

def saveFileName(arr):
    global content
    indicator1 = "CapstoneProject"
    indicator2 = "HTMLFiles"
    # ['/CapstoneProject/HTMLFiles/SOLARSNOOKS.html']
    for link in arr:
        res = link.split('/')
        # ['CapstoneProject', 'HTMLFiles', 'SOLARSNOOKS
        for word in res:
            if word!= indicator1 and word!= indicator2 and word!='' : 
                content.append(word)


def addToHTML():
    global pathToTop10
    startingWord = '<div class ="recentStories">'
    startingIndex = None 

    bubbleSort()
    with open(os.path.join(pathToTop10), 'r', encoding='utf-8') as top10File:
        lines = top10File.readlines()
    
    for lineNumber, line in enumerate(lines, 1):
            if startingWord in line: 
                startingIndex = lineNumber
                break

    n=len(fileRecurrence)
    i=0
    while i <20  and i<n and startingIndex  is not None:
        storyFile = fileRecurrence[i]
        storyTitle = getStoryTitle(storyFile)

        lines.insert(
            startingIndex,
            '<a href="../HTMLFiles/' + storyFile +
            '" class="barLink">' + storyTitle + '</a><br>\n'
        )
        i=i+2
        startingIndex +=1
    with open(os.path.join(pathToTop10), 'w', encoding='utf-8') as top10File:
        top10File.writelines(lines) 


def bubbleSort():
    global fileRecurrence
    n = len(fileRecurrence)
    for i in range(n):
        swapped = False
        for j in range(1, n-i-2,2):
            if fileRecurrence[j] < fileRecurrence[j+2]:
                fileRecurrence[j], fileRecurrence[j+2] = fileRecurrence[j+2], fileRecurrence[j]
                fileRecurrence[j-1], fileRecurrence[j+1] = fileRecurrence[j+1], fileRecurrence[j-1]
                swapped = True
        if (swapped == False):
            break



if __name__=='__main__':
    main()
    