import os
import random
getTitle = []
getDate = []
getTag = []
getText = []
currentName = ""
fileContent =[]
tagFilePath= ""
filePath= ""
currentfileName=""
currentTag=""
pathToLibrary = os.path.join(os.path.dirname(os.path.abspath(__file__)),'.', 'MainFiles/library.html')
DirectoryPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),'.', 'Content')
OutputFilePath = os.path.join(os.path.dirname(os.path.abspath(__file__)),'.', 'HTMLFiles')


def cleanGeneratedFiles():
    for filename in os.listdir(OutputFilePath):
        if filename.lower().endswith('.html'):
            file_path = os.path.join(OutputFilePath, filename)

            if os.path.isfile(file_path):
                os.remove(file_path)
                
def main():
    global DirectoryPath
    cleanGeneratedFiles() # clears previously generated files
    initializeLibrary()
    ListFiles = os.listdir(DirectoryPath)
    for file in ListFiles:
        readFile(file)
    
        

def deleteLines(path, startingLine, endingLine):
    with open(path, 'r', encoding='utf-8-sig') as file:
        lines = file.readlines()

    start = next((i for i, line in enumerate(lines) if startingLine in line),None)

    end = next((i for i, line in enumerate(lines) if endingLine in line and start is not None and i > start),None)

    if start is None or end is None:
        raise ValueError("HTML section markers not found")

    # Keep the section markers and replace the generated content.
    lines[start + 1:end] = []

    with open(path, 'w', encoding='utf-8-sig') as file:
        file.writelines(lines)

def initializeLibrary():
    deleteLines(
        pathToLibrary,
        '<!-- STORIES_START -->',
        '<!-- STORIES_END -->'
    )

    deleteLines(
        pathToLibrary,
        '<!-- TAGS_START -->',
        '<!-- TAGS_END -->'
    )

def readFile(file):
    global DirectoryPath
    global currentName 
    global fileContent 
    global filePath
    global getDate 
    global getTag 
    global getText
    global getTitle
    global currentfileName
    currentName = ""
    fileContent =[]
    getDate = []
    getTag = []
    getText = []
    getTitle = []
    currentfileName = os.path.splitext(os.path.basename(file))[0]+'.html'
    filePath = OutputFilePath + '/'+ currentfileName
    # reading each word  
    with open(os.path.join(DirectoryPath, os.path.basename(file)), 'r', encoding='utf-8-sig') as currentFile:
        while True:
            for line_f in currentFile:
            # To be able to move to the next line
                if line_f.strip() == '' and (not fileContent or fileContent[-1] != '\n'):
                    fileContent.append('\n') 
                    # reading word by word from the input file 
                for word in line_f.split():
                    fileContent.append(word)   
            char = currentFile.read(1)         
            # To mark the end of the File
            if not char:
                break
                # close the file
        currentFile.close()
    processContent()
    addToLibrary(1)


def addToLibrary(index):
    global currentfileName
    global currentName
    global currentTag
    global tagFilePath
    global pathToLibrary

    green = random.randint(0, 50)
    red = random.randint(0, 50)
    blue = random.randint(150, 255)

    if index == 1:
        startingLine = '<!-- STORIES_END -->'
        path = "../HTMLFiles/" + currentfileName
        findName = currentName.strip().title()
    else:
        startingLine = '<!-- TAGS_END -->'
        path = "../HTMLFiles/" + os.path.basename(tagFilePath)
        findName = currentTag.capitalize()

    with open(pathToLibrary, 'r', encoding='utf-8-sig') as libraryFile:
        lines = libraryFile.readlines()

    # Prevent duplicate tags in the library
    if index == 2:
        tagLink = "../HTMLFiles/" + os.path.basename(tagFilePath)

        if any(tagLink in line for line in lines):
            return
        
    startingIndex = next(
        (i for i, line in enumerate(lines) if startingLine in line),
        None
    )

    if startingIndex is None:
        raise ValueError("Library section marker not found")

    newContent = [
        '<div id="container" style="background-color: rgb('
        + str(green) + ',' + str(red) + ',' + str(blue) + ');">\n',
        '<a href="' + path + '">' + findName + '</a>\n',
        '</div>\n'
    ]

    lines[startingIndex:startingIndex] = newContent

    with open(pathToLibrary, 'w', encoding='utf-8-sig') as libraryFile:
        libraryFile.writelines(lines)
           

def findInFile(word, path):
    with open(path, 'r') as file:
        for lineNumber, line in enumerate(file, 1):
            if word in line: 
                return lineNumber
    return None

def processContent():
    global currentName
    tag = []
    tagVal = 1
    i=0
    while i <=(len(fileContent)-1):
        if fileContent[i]== "TITLE":
            i+=1
            while (fileContent[i]!="DATE"):
                getTitle.append(fileContent[i])
                i+=1
            currentName= ' '.join(getTitle).strip().title()
        elif fileContent[i]== "DATE":
            i+=1
            while (fileContent[i]!="TAG"):
                getDate.append(fileContent[i])
                i+=1    
        elif fileContent[i]== "TAG":
            i+=1
            while tagVal== 1:
                if i <=(len(fileContent)-1) and '#' in fileContent[i]:
                #  case: #honesty
                    if len(fileContent[i])!= 1: 
                        if(fileContent[i][1:].isidentifier() or fileContent[i][1:].isalpha()):
                            getTag.append(fileContent[i])
                        #99 / # 
                        else:
                            print("Error: Incomplete Tag")   
                            tagVal=0     
                    else:
                        # case: #  generosity
                        i+=1
                        if(fileContent[i].isidentifier() or fileContent[i].isalpha() ):
                            tag = '#' + fileContent[i] 
                            getTag.append(tag)
                # No tag entered
                else:
                    if i == len(fileContent):
                        break
                    else:      
                        tagVal = 0
                        i-=1
                i+=1
        else:
            getText.append(fileContent[i])
            i=i+1
    createHTML()


def createHTML():
    global tagFilePath
    global filePath
    global currentName
    global currentfileName
    global currentTag
    tagFile =" "
    lineNumber = 0
    
    HTMLWord= '<div class="tagLinks">'
    # w+: overwrite or create a new file if it does not exist
    with open(os.path.join(filePath), 'w+', encoding='utf-8-sig') as outputFile:
        outputFile.write("<html>\n")
        outputFile.write("<head>\n")
        outputFile.write("<title>" +currentName+"</title>\n")
        outputFile.write('<link rel="stylesheet" type="text/css" href="../stylingStories.css" >\n')
        outputFile.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">')
        outputFile.write("</head>\n")
        outputFile.write("<body>\n")
        outputFile.write('<div class="header">')
        outputFile.write('\n<a class="logo">ST')
        outputFile.write('<i class="fa fa-clock-o" style="color: #fe06a3;"></i>')
        outputFile.write('RY TIME!</a>\n')
        outputFile.write('<a href="../MainFiles/home.html" class="barLink" style="color: white;">HOME</a>\n')
        outputFile.write('<a href="../MainFiles/library.html" class="barLink" style="color: white;">Library</a>\n')
        outputFile.write('<a href="../MainFiles/blog.html" class="barLink" style="color: white;">Blog</a>\n')
        outputFile.write('</div>\n')
        outputFile.write('<h1 class="storyTitle">' + currentName + '</h1>\n')
        outputFile.write('<div class="storyText">')
        outputFile.write("\n<p> ")
        for word in getText:
            if word == "\n":
                outputFile.write("\n</p> ")
                outputFile.write("\n<p> ")
            outputFile.write(str(word)+' ')
        outputFile.write("</p>\n")
        outputFile.write('</div>')
        outputFile.write("\n<p> ")
        outputFile.write('<div class="storyDate">\n')
        outputFile.write('<small> <b>'+"Published On: \t")
        for word in getDate:
            outputFile.write(str(word))
        outputFile.write('</small></div>')
        outputFile.write("</p>\n")
        outputFile.write('<div class="tags">')
        for tag in dict.fromkeys(getTag):
            isFilePathAdded = False
            displayTag = tag.title()
            tagFile = tag.replace(tag[0], "", 1) + 'Tag.html'
            tagFilePath =  os.path.join(OutputFilePath, tagFile)
            currentTag = tag.replace(tag[0], "", 1)
            addToLibrary(2)
            # Tag file already exists
            if os.path.exists(tagFilePath):
                with open(os.path.join(tagFilePath), 'r', encoding='utf-8-sig') as existingTagFile:
                    lines = existingTagFile.readlines()

                if findInFile(currentName, tagFilePath)!= None:
                    isFilePathAdded = True

                if isFilePathAdded == False: 
                    # append url in the middle of the file
                    lineNumber = findInFile(HTMLWord, tagFilePath) 
                    lines.insert (lineNumber, "\n<a href=" + "./"+currentfileName + ">"+currentName+ "</a><br>\n")
                    with open(os.path.join(tagFilePath), 'w') as existingTagFile:
                        existingTagFile.writelines(lines)  
                outputFile.write("\n<a href=" + "./"+tagFile + ">"+displayTag+ "</a>\n")
                existingTagFile.close()
            # Tag file was not created earlier
            else:
                with open(os.path.join(tagFilePath), 'w+', encoding='utf-8-sig') as newFile:
                    newFile.write("<html>\n")
                    newFile.write("<head>\n")
                    newFile.write("<title>" +tag+"</title>\n")
                    newFile.write('<link rel="stylesheet" type="text/css" href="../stylingTags.css" >\n')
                    newFile.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">')
                    newFile.write("</head>\n")
                    newFile.write("<body>\n")
                    newFile.write('<div class="header">')
                    newFile.write('\n<a class="logo">ST')
                    newFile.write('<i class="fa fa-clock-o" style="color: #fe06a3;"></i>')
                    newFile.write('RY TIME!</a>\n')
                    newFile.write('<a href="../MainFiles/home.html" class="barLink" style="color: white;">HOME</a>\n')
                    newFile.write('<a href="../MainFiles/library.html" class="barLink" style="color: white;">Library</a>\n')
                    newFile.write('<a href="../MainFiles/blog.html" class="barLink" style="color: white;">Blog</a>\n')
                    newFile.write('</div>\n')
                    newFile.write("<h1>" +(tag.replace(tag[0], "", 1)).capitalize()+" Tag</h1>\n")
                    newFile.write('<div class="tagLinks">\n')
                    newFile.write("<a href="+ "./"+currentfileName + ">"+currentName+ "</a><br>\n")
                    newFile.write('</div>\n')
                    newFile.write("</body>")
                    newFile.write("</html>\n")
                outputFile.write("\n<a href=" + "./"+tagFile + ">"+displayTag+ "</a>\n")              
        outputFile.write('</div>')
        outputFile.write("</html>\n")
        outputFile.write("</body>")




if __name__=='__main__':
    main()
    

