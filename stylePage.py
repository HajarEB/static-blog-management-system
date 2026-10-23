from tkinter import colorchooser
import tkinter

import webcolors
import os
from tkinter import *
color =""
pathToStylingStoriesCSS = os.path.join(os.path.dirname(os.path.abspath(__file__)),'stylingStories.css')

def main():
    while True:
        print("\n************ HTML Page Styling: ************\n")
        print("1- Style through the command Line")
        print("2- Style through the GUI")
        print("3- Exit")

        try:
            styling = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter 1, 2, or 3.")
            continue

        if styling == 1:
            print("\n1- Styling through Color names")
            print("2- Styling through RGB codes")

            try:
                response = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter 1 or 2.")
                continue

            if response == 1:
                colorStyling()
                break
            elif response == 2:
                RGBStyling()
                break
            else:
                print("Invalid choice.")

        elif styling == 2:
            openDialog()
            break

        elif styling == 3:
            print("Exiting...")
            break

        else:
            print("Please enter 1, 2, or 3.")

def checkFormat(RGBCode):
    for i in RGBCode:
        try:
            i=int(i)
            if  isinstance(i, int) and i>=0 and i<=255:      
                continue
            else:
                exit("\nError: Please Respect the required format of X,Y,Z\n")

        except:
            exit("\nError: Please Respect the required format of X,Y,Z\n")
    
def RGBStyling():
    print("\n********** Please Enter All the Values Using This FORMAT X,Y,Z **********\n")
    titleColor = input("Please enter the title color\n").split(',')
    checkFormat(titleColor)

    textColor = input("Please enter the text color\n").split(',')
    checkFormat(textColor)
    
    backgroundColor =  input("Please enter the background color\n").split(',')
    checkFormat(backgroundColor)

    tagsColor = input("Please enter the tags color\n").split(',')
    checkFormat(tagsColor)

    borderColor = input("Please enter the border color\n").split(',')
    checkFormat(borderColor)


    updateCSS(titleColor,".storyTitle", "color: ")
    updateCSS(textColor,"storyText", "color: ")
    updateCSS(backgroundColor,"body", "background-color: ")
    updateCSS(tagsColor,"tags a", "color: ")
    updateCSS(borderColor,"storyText", "border: 2px solid ") 

def colorStyling():
    answer = input("\nIf you want to see the available colors press 1 otherwise press 0\n")
    if answer == "1":
        print(webcolors.names("css3"))
    titleColor = input("Please enter the title color\n").strip().lower()
    titleColor = webcolors.name_to_rgb(titleColor)

    textColor = input("Please enter the text color\n").strip().lower()
    textColor = webcolors.name_to_rgb(textColor)
    
    backgroundColor = input("Please enter the background color\n").strip().lower()
    backgroundColor = webcolors.name_to_rgb(backgroundColor)

    tagsColor = input("Please enter the tags color\n").strip().lower()
    tagsColor = webcolors.name_to_rgb(tagsColor)

    borderColor = input("Please enter the border color\n").strip().lower()
    borderColor = webcolors.name_to_rgb(borderColor)

    updateCSS(titleColor,".storyTitle", "color: ")
    updateCSS(textColor,"storyText", "color: ")
    updateCSS(backgroundColor,"body", "background-color: ")
    updateCSS(tagsColor,"tags a", "color: ")
    updateCSS(borderColor,"storyText", "border: 2px solid ")           
        

def openDialog():
    dialog = Tk()
    dialog.geometry("500x500")
    dialog.grid_columnconfigure(0, weight=1)
    dialog.grid_columnconfigure(1, weight=1)
    dialog.grid_columnconfigure(2, weight=1)
    
    button1 = Button(dialog, text="Select Title Color", command=lambda: pickColor(1,label1), width=25,height=2, bg="#09F353", fg="#2e1a02", font=('Helvetica', 12, 'bold'), relief="flat")
    button1.grid(row=0, column=1, pady=(15, 5))

    button2 = Button(dialog, text="Select Text Color", command=lambda: pickColor(2,label2), width=25,height=2, bg="#09F37A", fg="#2e1a02", font=('Helvetica', 12, 'bold'), relief="flat")
    button2.grid(row=1, column=1, pady=5)

    button3 = Button(dialog, text="Select Background Color", command=lambda: pickColor(3,label3), width=25,height=2, bg="#09F3B7", fg="#2e1a02", font=('Helvetica', 12, 'bold'), relief="flat")
    button3.grid(row=2, column=1, pady=5)
        
    button4 = Button(dialog, text="Select Tags Color", command=lambda: pickColor(4,label4), width=25,height=2, bg="#09F3EF", fg="#2e1a02", font=('Helvetica', 12, 'bold'), relief="flat")
    button4.grid(row=3, column=1, pady=5)
        
    button5 = Button(dialog, text="Select Border Color", command=lambda: pickColor(5,label5), width=25,height=2, bg="#09CFF3", fg="#2e1a02", font=('Helvetica', 12, 'bold'), relief="flat")
    button5.grid(row=4, column=1, pady=5)

    label1 =  tkinter.Label(dialog, text="", bg="#DAFBEB", fg="#034827", font=('Helvetica', 10, 'bold'))
    label1.grid(row=0, column=2, pady=5,padx= 10)

    label2 = tkinter.Label(dialog, text="", bg="#DAFBEB", fg="#034827", font=('Helvetica', 10, 'bold'))
    label2.grid(row=1, column=2, pady=5,padx= 10)
    
    label3 = tkinter.Label(dialog, text="", bg="#DAFBEB", fg="#034827", font=('Helvetica', 10, 'bold'))
    label3.grid(row=2, column=2, pady=5,padx= 10)
    
    label4 = tkinter.Label(dialog, text="", bg="#DAFBEB", fg="#034827", font=('Helvetica', 10, 'bold'))
    label4.grid(row=3, column=2, pady=5,padx= 10)
    
    label5 = tkinter.Label(dialog, text="", bg="#DAFBEB", fg="#034827", font=('Helvetica', 10, 'bold'))
    label5.grid(row=4, column=2, pady=5,padx= 10)
    
    buttonDone = Button(
        dialog,
        text="Customize ✓",
        command=dialog.destroy,
        width=15,
        height=2,
        bg="#1B263B",
        fg="white",
        activebackground="#344966",
        activeforeground="white",
        font=('Helvetica', 12, 'bold'),
        relief="raised",
        bd=3,
        cursor="hand2"
    )

    buttonDone.grid(
        row=5,
        column=1,
        pady=(30, 20)
    )


    dialog.configure(bg="#DAFBEB")
    #execute tkinter
    dialog.mainloop()


def pickColor(index,label):
    value = colorchooser.askcolor(title="Select a Color")
    if value[0] is None:
        return
    if index ==1:
        updateCSS(value[0],".storyTitle", "color: ")
    elif index ==2:
        updateCSS(value[0],"storyText", "color: ")
    elif index ==3:
        updateCSS(value[0],"body", "background-color: ")
    elif index ==4:
        updateCSS(value[0],"tags a", "color: ")
    elif index ==5:
        updateCSS(value[0],"storyText", "border: 2px solid ")
    else:
        return
    
    label.config(text=f"rgb{value[0]}")
   
 


def updateCSS(element, className, tag):
    global pathToStylingStoriesCSS
    global color
    with open(os.path.join(pathToStylingStoriesCSS), 'r', encoding='utf-8-sig') as file:
        lines = file.readlines()
    lineNumber = findWithinBlock(className, tag)

    if element is None:
        color = "rgb(0, 0, 0)"
    else:
        color = "rgb("
        count = 1
        for i in element:
            color+= str(i)
            if count < 3:
                color+= str(',')
            else:
                color+= str(')')
            count +=1
    if lineNumber is not None:
        with open(os.path.join(pathToStylingStoriesCSS), 'w', encoding='utf-8-sig') as stylingFile:
            newLine = '\t'+ str(tag) + str(color) +';\n'
            del lines[lineNumber-1]
            lines.insert (lineNumber-1,newLine)
            stylingFile.writelines(lines)
    else:
        SystemError("error")



def findWithinBlock(className, word):
    global pathToStylingStoriesCSS
    withinBlock = 0
    with open(pathToStylingStoriesCSS, 'r') as file:
        for lineNumber, line in enumerate(file, 1):
            if className in line:
                withinBlock = 1
            elif '}' in line:
                withinBlock = 0
            if word in line and withinBlock == 1: 
                return lineNumber
    return None

if __name__=='__main__':
    main()
    

