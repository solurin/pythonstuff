#--------------------topcode, do not change!--------------------
from  tkinter import *
import tkinter.messagebox as box
import tkinter.simpledialog as simpledialog
import tkinter.filedialog as filedialog
import sys
import math
import functools


#--------------------common helper functions, do not change!--------------------
def settext(widget, newtext):
	'''
		This is how you change text in a widget.  What it does varies depending on the widget.
		Always give a string as the second parameter, even if you want to just put a number in it.
	'''
	if type(widget).__name__ == 'ScrolledList':               # have to do this because ScrolledList may not have been included
		widget.listbox.delete(0,END)
		if type(newtext) == list:
			for string in newtext:
				widget.listbox.insert(END,string)
		elif type(newtext) == str:
			for string in newtext.split('\n'):
 				widget.listbox.insert(END,string)

	elif type(widget).__name__ == 'ScrolledText':               # have to do this because ScrolledText may not have been included
		widget.text.delete('1.0', END)
		widget.text.insert('1.0', newtext)
		widget.text.mark_set(INSERT, '1.0')

	elif type(widget) == Text:
		widget.delete('1.0', END)
		widget.insert('1.0', newtext)

	elif type(widget) == Entry:
		widget.delete(0,END)
		widget.insert(0,newtext)

	elif type(widget) == Label:
		widget['text'] = newtext

	elif type(widget) == Button:
		widget.config(text=newtext)

	elif type(widget) == Checkbutton:
		widget.config(text=newtext)

	elif type(widget) == Scale:
		widget['label'] = newtext

	elif type(widget) == Listbox:
		widget.delete(0,END)
		if type(newtext) == list:
			for string in newtext:
				widget.insert(END,string)
		elif type(newtext) == str:
			for string in newtext.split('\n'):
				widget.insert(END,string)

	elif type(widget) == Menubutton:
		widget['text'] = newtext

def gettext(widget):
	'''
		This gets the contents of a widget and returns a string.  If it is a label, it just returns the label text.
		If it is a button, it returns the text on the face of the button.  If it is a list or checkbox, it returns the
		string that is currently selected.
	'''
	if type(widget).__name__ == 'ScrolledList':
		return list(widget.listbox.get(0,END))

	elif type(widget).__name__ == 'ScrolledText':
		return widget.text.get('1.0', END+'-1c')

	elif type(widget) == Text:
		return widget.get('1.0', END+'-1c')

	elif type(widget) == Entry:
		return widget.get()

	elif type(widget) == Label:
		return widget.cget('text')

	elif type(widget) == Button:
		return widget['text']

	elif type(widget) == Checkbutton:
		return widget.cget('text')

	elif type(widget) == Scale:
		return widget['label']

	elif type(widget) == Listbox:
		return list(widget.get(0,END))

	elif type(widget) == Menubutton:
		return widget['text']

def appendtext(widget, newtext):
	'''
		This sets the text by first getting the current text and appending to the end.
		It does not automatically insert a newline or any spaces.  You should do that yourself, if desired.
	'''
	current_text = gettext(widget)
	settext(widget, current_text + newtext)

def popup(msg):
	'''
		Use this to display a quick message to the user.  Just give it a string.
	'''
	box.showinfo('msg', msg)

def askforstring(prompt):
	'''
		Use this to get a string from the user.  The prompt is what is displayed on the dialog box.
	'''
	return simpledialog.askstring('request for input', prompt)

def askforyesno(prompt):
	'''
		Use this to get a String response from the user.  It is either yes or no.
		Notice, the type of the returned object is str, not boolean!
		The prompt is what is displayed on the dialog box.
	'''
	return box.askquestion('request for yes/no', prompt)

def getselected(somelistbox):
	'''
		Use this to get the currently selected text from a listbox.
	'''
	if type(somelistbox) == Listbox:
		try:
			return somelistbox.get(somelistbox.curselection()[0])
		except:
			return ''
	else:
		return somelistbox.getselected()

def readFile(filename):
	'''
		Read contents of file whose name is filename, and return it.
		Return empty string on error.
	'''
	try:
		f = open(filename,'r')
		text = f.read()
		f.close()
		return text
	except:
		print('Error in readfile:  filename='+filename)
		return ''

def writeFile(filename, text):
	'''
		Write contents into file whose name is filename.
		Return False on error, True on success
	'''
	try:
		f = open(filename,'w')
		f.write(text)
		f.close()
		return True
	except:
		print('Error in writefile:  filename='+filename)
		return False

def exists(filename):
	'''
		Return True if file named filename exists
	'''
	return os.path.isfile(filename)


#--------------------modulecode, do not change!--------------------

##%MODULECODE
import os,sys
from tkinter.filedialog import askopenfilename,asksaveasfilename,askdirectory

undos = []
path = ""
filename = ""
is_exposed = False

def load():
     filename = askopenfilename()   #"Where is the file containing Python code?")
     settext(filenameTF, filename)
     if os.path.exists(filename):
          with open(filename,"r") as f:
               text = f.read()
          sys.stdout.flush()
          bigTA.settext(text)
     else:
          box.showinfo("Could not open file: " + filename)

def save():
     global path, filename
     filename = path + "/" + gettext(filenameTF)
     if len(filename.strip()) == 0:
          fullpath = asksaveasfilename()
          path = parsePath(fullpath)[0]
          filename = parsePath(fullpath)[1]
          settext(filenameTF, filename)
          fp = open(filename, "w")
          fp.write(gettext(bigTA))
          fp.close()
     with open(filename,"w") as f:
          f.write(gettext(bigTA))
     box.showinfo('Saved!',"Your program was saved to:\n"+filename)

def save_as():
     global path, filename
     fullpath = asksaveasfilename()
     path = parsePath(fullpath)[0]
     filename = parsePath(fullpath)[1]
     fp = open(fullpath, "w")
     fp.write(gettext(bigTA))
     fp.close()
     settext(filenameTF, filename)
     box.showinfo('Saved!',"Your program was saved to:\n"+fullpath)

def parsePath(fullpath):
	'''
	Break a full path into [path to file, bare filename]
	and return a list with these two strings.  It uses the last forward slash
	to find the beginning of the bare filename.
	'''
	i = len(fullpath)-1
	while i >= 0 and fullpath[i] != '/':
		i -= 1
	if i == -1:    #this shouldn't happen
		return [fullpath, ""]
	else:
		return [fullpath[0:i], fullpath[i+1:]]

def indent():
     level = 0
     prefix = " " * int(gettext(numSpacesTF))
     active = False
     olds = gettext(bigTA)
     undos.append(olds)
     news = ""
     startflag = gettext(startFlagTF)
     endflag = gettext(endFlagTF)
     for line in olds.split("\n"):
          if line == startflag:
               active = True
               continue
          if line == endflag:
               active = False
               continue
          if not active:
               news += line if len(news) == 0 else "\n" + line
               continue
          line = line.strip()
          if line == "{":
               level += 1
          elif line.endswith("{"):
               line = line[0:-1]       # chop off final curly brace
               line = prefix * level + line
               news += line if len(news) == 0 else "\n" + line
               level += 1
          elif line == "}":
               level -= 1
          else:
               line = prefix * level + line
               news += line if len(news) == 0 else "\n" + line
     settext(bigTA, news)

def addCurlies():
     active = False
     olds = gettext(bigTA)
     undos.append(olds)
     news = ""
     startflag = gettext(startFlagTF)
     endflag = gettext(endFlagTF)
     for line in olds.split("\n"):
          if line == startflag:
               active = True
               news += line if len(news) == 0 else "\n" + line
               continue
          if line == endflag:
               active = False
               news += line if len(news) == 0 else "\n" + line
               continue
          if not active:
               news += line if len(news) == 0 else "\n" + line
               continue
          line = trimBlanksFromRightend(line)
          if line.strip().endswith(":"):
               line += " {"
          news += line if len(news) == 0 else "\n" + line
     settext(bigTA, news)

def trimBlanksFromRightend(line):
     if len(line) == 0: return line
     while line[-1] == ' ' or line[-1] == '\t' or line[-1] == '\r':
          line = line[0:-1]
     return line

def undo():
     if len(undos) == 0:
          popup("Nothing to undo")
          return
     settext(bigTA, undos.pop())

def loadSample():
     sampleName = gettext(samplesCH)
     if sampleName == "sample 1":
          settext(bigTA, sample1)
     elif sampleName == "sample 2":
          settext(bigTA, sample2)
     elif sampleName == "sample 3":
          settext(bigTA, sample3)

def help():
     s = "This program can help you fix Python's pesky problem of\n"
     s += "inconsistent indentation.  You denote the start of an \n"
     s += "block of code that you want to indent with an opening symbol,\n"
     s += "which is usually the curly brace { used by Java and C.\n"
     s += "Then put a closing symbol, usually the closing curly brace,\n"
     s += "on a line by itself at the end of the indented area.\n\n"
     s += "You can tell this program which lines to process by putting\n"
     s += "#$start right before the code to be changed and $#stop right\n"
     s += "after.  Code outside this area is unchanged.  These symbols\n"
     s += "can be changed.\n\n"
     s += "Another thing you can do is use IDLE to try to fix your problem:\n"
     s += "----------------------------------------------------------------\n"
     s += "Select All (with CONTROL-A) or Edit>Select All.\n"
     s += "Then go to the Format menu and select 'Untabify region.'\n"
     s += "Finally, go to the Format menu again and select 'Tabify region.'\n"
     s += "This usually fixes the problem.  If it does not, then use this\n"
     s += "program."
     popup(s)

sample1 = '''#this is a simple program:
#$start
if x == 5:
{
     if a < b:
     {
z = 2
     }      
}
else
{
print("Hi there")
}
'''

sample2 = '''#another simple program
#$start
if x == 5:{
     if a < b:      {
z = 2
     }      
}
else {
print("Hi there")
}
'''

sample3 = '''#this one has problems!
#$start
def myfunc(n):
	a = 2
     y = 17
     if a == y*y:
		print("This is crazy!")
'''

def untabify_unexposed():
	undos.append(gettext(bigTA))
	numpertab = int(askforstring("How many spaces per tab? "))
	s = ""
	lines = gettext(bigTA).split("\n")
	for line in lines:
		s += untabify_line_unexposed(line, numpertab) + "\n"
	settext(bigTA,s)

def untabify_line_unexposed(line, numpertab):
	''' Only untabify the front of the line, not its interior '''
	s = ""
	i = 0
	for ch in line:
		if ch != " " and ch != "\t":
			break
		if ch == "\t":
			s += " "*numpertab
		i += 1
	return s + line[i:]

def tabify_unexposed():
	undos.append(gettext(bigTA))
	numpertab = int(askforstring("How many spaces per tab? "))
	s = ""
	lines = gettext(bigTA).split("\n")
	for line in lines:
		s += tabify_line_unexposed(line, numpertab) + "\n"
	settext(bigTA,s)

def tabify_line_unexposed(line, numpertab):
	''' Only tabify the front of the line, not its interior '''
	s = ""
	i = 0
	numblanks_seen = 0
	for ch in line:
		if ch != " ":
			break
		if ch == " ":
			numblanks_seen += 1
		if numblanks_seen == numpertab:
			s += "\t"
			numblanks_seen = 0
		i += 1
	return s + " "*numblanks_seen + line[i:]

def untabify_exposed():
	undos.append(gettext(bigTA))
	numpertab = int(askforstring("How many spaces per tab? "))
	s = ""
	lines = gettext(bigTA).split("\n")
	for line in lines:
		s += untabify_line_exposed(line, numpertab) + "\n"
	settext(bigTA,s)

def untabify_line_exposed(line, numpertab):
	''' Only untabify the front of the line, not its interior '''
	newline = ""
	while len(line) > 0:
		if line.startswith("----->"):
			newline += "."*numpertab
			line = line[6:]
		else:
			break
	return newline + line

def tabify_exposed():
	undos.append(gettext(bigTA))
	numpertab = int(askforstring("How many spaces per tab? "))
	s = ""
	lines = gettext(bigTA).split("\n")
	for line in lines:
		s += tabify_line_exposed(line, numpertab) + "\n"
	settext(bigTA,s)

def tabify_line_exposed(line, numpertab):
	''' Only tabify the front of the line, not its interior '''
	newline = ""
	runperiods = "."*numpertab
	while len(line) > 0:
		if line.startswith(runperiods):
			newline += "----->"
			line = line[numpertab:]
		else:
			break
	return newline + line

def expose():
	undos.append(gettext(bigTA))
	s = ""
	lines = gettext(bigTA).split("\n")
	for line in lines:
		s += exposeLine(line) + "\n"
	settext(bigTA, s)

def unexpose():
	undos.append(gettext(bigTA))
	s = ""
	lines = gettext(bigTA).split("\n")
	for line in lines:
		s += unexposeLine(line) + "\n"
	settext(bigTA, s)

def exposeLine(line):
	newline = ""
	i = 0
	for ch in line:
		if ch != " " and ch != "\t":
			break
		if ch == " ":
			newline += "."
		elif ch == "\t":
			newline += "----->"
		i += 1
	newline += line[i:]
	return newline

def unexposeLine(line):
	newline = ""
	while len(line) > 0:
		if line[0] == ".":
			newline += " "
			line = line[1:]
		elif line.startswith("----->"):
			newline += "\t"
			line = line[6:]
		else:
			break
	return newline + line

def resize_code(event):
	w, h = event.width, event.height
	bigTA.place(x=8, y=25, width=w-15, height=(h-80))
	y = h - 80 + 5
	for comp in [startflagL, startFlagTF, openerL, openingCharTF, numspacesL, numSpacesTF, goB, undoB, moreCommandCH, moreL]:
		w = comp.winfo_width()
		h = comp.winfo_height()
		x = comp.winfo_x()
		if comp == moreCommandCH or comp == moreL:
			comp.place(x=x, y=y+h+6, width=w, height=h)
		else:
			comp.place(x=x, y=y+h, width=w, height=h)
	y += endflagL.winfo_height() + 3
	for comp in [endflagL, endFlagTF, closerL, closingCharTF, samplesL, samplesCH, loadSampleB, exposedCB]:
		w = comp.winfo_width()
		h = comp.winfo_height()
		x = comp.winfo_x()
		comp.place(x=x, y=y+h, width=w, height=h)

def moreCommand(what):
	if what == "Change tabs to blanks":
		if is_exposed:
			untabify_exposed()
		else:
			untabify_unexposed()
	elif what == "Change blanks to tabs":
		if is_exposed:
			tabify_exposed()
		else:
			tabify_unexposed()
	elif what == "Add curly braces after :":
		addCurlies()


##%ENDCODE

def window_init():
     global root
     root=Tk()
     root.geometry("915x564")
     root.configure(background='#ebebeb')
     root.title("Python application")
     canvas = Canvas(bd=0, highlightthickness=0)
     canvas.pack(fill=BOTH, expand=1)
     canvas.bind("<Configure>", resizeMe)

#--------------------internally defined widget classes, do not change!--------------------
class ScrolledText(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self._makewidgets()

	def _makewidgets(self):
		sbar = Scrollbar(self)
		text = Text(self, relief=SUNKEN)
		sbar.config(command=text.yview)
		text.config(yscrollcommand=sbar.set)
		sbar.pack(side=RIGHT,fill=Y)
		text.pack(side=LEFT,expand=YES,fill=BOTH)
		self.text = text
	
	def settext(self, text=''):
		self.text.delete('1.0', END)
		self.text.insert('1.0', text)
		self.text.mark_set(INSERT, '1.0')

	def gettext(self):
		return self.text.get('1.0', END+'-1c');

	def append(self, text=''):
		self.text.insert(END,text)



#--------------------functions for widget event handlers, do not change!--------------------
def loadB_action_code():
    load()

def saveB_action_code():
    save()

def goB_action_code():
    indent()

def undoB_action_code():
    undo()

def saveAsB_action_code():
    save_as()

def samplesCH_respond(keycode):
     if keycode == 1:
          samplesCH.config(text='sample 1')
          for thing in samplesCH_varlist:
               thing.set(0)
          samplesCH_xvar1.set(1)
     if keycode == 2:
          samplesCH.config(text='sample 2')
          for thing in samplesCH_varlist:
               thing.set(0)
          samplesCH_xvar2.set(1)
     if keycode == 3:
          samplesCH.config(text='sample 3')
          for thing in samplesCH_varlist:
               thing.set(0)
          samplesCH_xvar3.set(1)
def loadSampleB_action_code():
    loadSample()

def helpB_action_code():
    help()

def untabifyB_action_code():
    if is_exposed:
    	untabify_exposed()
    else:
    	untabify_unexposed()

def tabifyB_action_code():
    if is_exposed:
    	tabify_exposed()
    else:
    	tabify_unexposed()

def onCheckbuttonPress_exposedCB(labelname):
    global is_exposed
    
    #popup("exposed_var.get() = "+str(exposed_var.get()))
    if exposed_var.get() == 1:
    	is_exposed = True
    	expose()
    else:
    	is_exposed = False
    	unexpose()

def moreCommandCH_item_code():
    moreCommand(gettext(moreCommandCH))

def moreCommandCH_respond(keycode):
     if keycode == 1:
          moreCommandCH.config(text='--select--')
          for thing in moreCommandCH_varlist:
               thing.set(0)
          moreCommandCH_xvar1.set(1)
     if keycode == 2:
          moreCommandCH.config(text='Change tabs to blanks')
          for thing in moreCommandCH_varlist:
               thing.set(0)
          moreCommandCH_xvar2.set(1)
     if keycode == 3:
          moreCommandCH.config(text='Change blanks to tabs')
          for thing in moreCommandCH_varlist:
               thing.set(0)
          moreCommandCH_xvar3.set(1)
     if keycode == 4:
          moreCommandCH.config(text='Add curly braces after :')
          for thing in moreCommandCH_varlist:
               thing.set(0)
          moreCommandCH_xvar4.set(1)
     moreCommand(gettext(moreCommandCH))


#--------------------Menu defs, do not change!--------------------


#--------------------extra class code, you can change this!--------------------
##%EXTRACLASSCODE

##%ENDCODE

def resizeMe(event):
     if 'resize_code' in globals():
          resize_code(event)
def main():
     window_init()
     global component0BL
     global Button1_var
     global filenameTF
     global loadB
     global saveB
     global bigTA
     global startflagL
     global Button1_var
     global startFlagTF
     global Button1_var
     global endFlagTF
     global endflagL
     global openerL
     global Button1_var
     global openingCharTF
     global Button1_var
     global closingCharTF
     global closerL
     global goB
     global undoB
     global saveAsB
     global numspacesL
     global Button1_var
     global numSpacesTF
     global samplesL
     global samplesCH_varlist
     global samplesCH_xvar1
     global samplesCH_xvar2
     global samplesCH_xvar3
     global samplesCH
     global loadSampleB
     global helpB
     global untabifyB
     global tabifyB
     global exposed_var
     global exposedCB
     global moreCommandCH_varlist
     global moreCommandCH_xvar1
     global moreCommandCH_xvar2
     global moreCommandCH_xvar3
     global moreCommandCH_xvar4
     global moreCommandCH
     global moreL
#--------------------widget making code, do not change anything from here to the end of the file!--------------------
     component0BL = Label(root, text="Filename:",width=76,height=22)
     component0BL.place(x=8,y=3, width=76, height=22)
     component0BL.config(font=("SansSerif", 11, 'bold'))
     component0BL.config(bg=root['bg'])
     component0BL.config(fg=("#000000"))
     Button1_var=StringVar()
     Button1_var.set("")
     filenameTF = Entry(root,width=635, textvariable=Button1_var)
     filenameTF.place(x=85,y=3, width=635, height=22)
     filenameTF.config(font=("SansSerif", 10, 'normal'))
     filenameTF.config(fg=("#000000"))
     filenameTF.config(bg=("#ffffff"))
     loadB = Button(root, text="Load",width=41,height=22,command=loadB_action_code)
     loadB.place(x=721,y=3, width=41, height=22)
     loadB.config(font=("SansSerif", 11, 'normal'))
     loadB.config(bg=("#ffffff"))
     loadB.config(fg=("#000000"))
     saveB = Button(root, text="Save",width=42,height=22,command=saveB_action_code)
     saveB.place(x=763,y=3, width=42, height=22)
     saveB.config(font=("SansSerif", 11, 'normal'))
     saveB.config(bg=("#ffffff"))
     saveB.config(fg=("#000000"))
     bigTA = ScrolledText(root)
     bigTA.place(x=8,y=27, width=903, height=485)
     bigTA.settext("")
     bigTA.text.config(font=("Courier", 11, 'normal'))
     bigTA.text.config(bg=("#ffffff"))
     bigTA.text.config(fg=("#000000"))
     startflagL = Label(root, text="Starting flag:",width=89,height=20)
     startflagL.place(x=6,y=514, width=89, height=20)
     startflagL.config(font=("SansSerif", 11, 'normal'))
     startflagL.config(bg=root['bg'])
     startflagL.config(fg=("#000000"))
     Button1_var=StringVar()
     Button1_var.set("#$start")
     startFlagTF = Entry(root,width=59, textvariable=Button1_var)
     startFlagTF.place(x=97,y=514, width=59, height=20)
     startFlagTF.config(font=("SansSerif", 11, 'normal'))
     startFlagTF.config(fg=("#000000"))
     startFlagTF.config(bg=("#ffffff"))
     Button1_var.set("#$start")
     Button1_var=StringVar()
     Button1_var.set("#$stop")
     endFlagTF = Entry(root,width=59, textvariable=Button1_var)
     endFlagTF.place(x=97,y=537, width=59, height=20)
     endFlagTF.config(font=("SansSerif", 11, 'normal'))
     endFlagTF.config(fg=("#000000"))
     endFlagTF.config(bg=("#ffffff"))
     Button1_var.set("#$stop")
     endflagL = Label(root, text="Stop flag:",width=89,height=20)
     endflagL.place(x=6,y=537, width=89, height=20)
     endflagL.config(font=("SansSerif", 11, 'normal'))
     endflagL.config(bg=root['bg'])
     endflagL.config(fg=("#000000"))
     openerL = Label(root, text="Opening char:",width=89,height=20)
     openerL.place(x=171,y=514, width=89, height=20)
     openerL.config(font=("SansSerif", 11, 'normal'))
     openerL.config(bg=root['bg'])
     openerL.config(fg=("#000000"))
     Button1_var=StringVar()
     Button1_var.set("{")
     openingCharTF = Entry(root,width=22, textvariable=Button1_var)
     openingCharTF.place(x=262,y=514, width=22, height=20)
     openingCharTF.config(font=("SansSerif", 11, 'normal'))
     openingCharTF.config(fg=("#000000"))
     openingCharTF.config(bg=("#ffffff"))
     Button1_var.set("{")
     Button1_var=StringVar()
     Button1_var.set("}")
     closingCharTF = Entry(root,width=21, textvariable=Button1_var)
     closingCharTF.place(x=262,y=537, width=21, height=20)
     closingCharTF.config(font=("SansSerif", 11, 'normal'))
     closingCharTF.config(fg=("#000000"))
     closingCharTF.config(bg=("#ffffff"))
     Button1_var.set("}")
     closerL = Label(root, text="Closing char:",width=89,height=20)
     closerL.place(x=171,y=537, width=89, height=20)
     closerL.config(font=("SansSerif", 11, 'normal'))
     closerL.config(bg=root['bg'])
     closerL.config(fg=("#000000"))
     goB = Button(root, text="Format to Python",width=125,height=20,command=goB_action_code)
     goB.place(x=457,y=514, width=125, height=20)
     goB.config(font=("SansSerif", 10, 'bold'))
     goB.config(bg=("#00ff00"))
     goB.config(fg=("#000000"))
     undoB = Button(root, text="Undo",width=54,height=20,command=undoB_action_code)
     undoB.place(x=584,y=514, width=54, height=20)
     undoB.config(font=("SansSerif", 12, 'bold'))
     undoB.config(bg=("#000000"))
     undoB.config(fg=("#ffffff"))
     saveAsB = Button(root, text="Save as",width=59,height=22,command=saveAsB_action_code)
     saveAsB.place(x=806,y=3, width=59, height=22)
     saveAsB.config(font=("SansSerif", 11, 'normal'))
     saveAsB.config(bg=("#ffffff"))
     saveAsB.config(fg=("#000000"))
     numspacesL = Label(root, text="Num spaces to indent:",width=139,height=20)
     numspacesL.place(x=290,y=514, width=139, height=20)
     numspacesL.config(font=("SansSerif", 10, 'normal'))
     numspacesL.config(bg=root['bg'])
     numspacesL.config(fg=("#000000"))
     Button1_var=StringVar()
     Button1_var.set("5")
     numSpacesTF = Entry(root,width=24, textvariable=Button1_var)
     numSpacesTF.place(x=431,y=514, width=24, height=20)
     numSpacesTF.config(font=("SansSerif", 12, 'normal'))
     numSpacesTF.config(fg=("#000000"))
     numSpacesTF.config(bg=("#ffffff"))
     Button1_var.set("5")
     samplesL = Label(root, text="Samples:",width=82,height=21)
     samplesL.place(x=290,y=536, width=82, height=21)
     samplesL.config(font=("SansSerif", 11, 'normal'))
     samplesL.config(bg=root['bg'])
     samplesL.config(fg=("#000000"))
     samplesCH = Menubutton(root, text='')
     samplesCH.place(x=374,y=536, width=167, height=21)
     samplesCH.config(font=("SansSerif", 12, 'normal'))
     samplesCH.config(bg=("#ffffff"))
     samplesCH.config(fg=("#000000"))
     samplesCH.menu = Menu(samplesCH, tearoff=0)
     samplesCH['menu'] = samplesCH.menu
     samplesCH_varlist=[]
     samplesCH_xvar1=IntVar()
     samplesCH_varlist.append(samplesCH_xvar1)
     samplesCH.menu.add_checkbutton(label='sample 1',variable=samplesCH_xvar1, command=functools.partial(samplesCH_respond, 1))
     samplesCH_xvar2=IntVar()
     samplesCH_varlist.append(samplesCH_xvar2)
     samplesCH.menu.add_checkbutton(label='sample 2',variable=samplesCH_xvar2, command=functools.partial(samplesCH_respond, 2))
     samplesCH_xvar3=IntVar()
     samplesCH_varlist.append(samplesCH_xvar3)
     samplesCH.menu.add_checkbutton(label='sample 3',variable=samplesCH_xvar3, command=functools.partial(samplesCH_respond, 3))
     loadSampleB = Button(root, text="load",width=39,height=21,command=loadSampleB_action_code)
     loadSampleB.place(x=543,y=536, width=39, height=21)
     loadSampleB.config(font=("SansSerif", 10, 'normal'))
     loadSampleB.config(bg=("#ffffff"))
     loadSampleB.config(fg=("#000000"))
     helpB = Button(root, text="Help!",width=45,height=22,command=helpB_action_code)
     helpB.place(x=866,y=3, width=45, height=22)
     helpB.config(font=("SansSerif", 12, 'normal'))
     helpB.config(bg=("#ffffff"))
     helpB.config(fg=("#000000"))
     untabifyB = Button(root, text="Change tabs to blanks",width=157,height=20,command=untabifyB_action_code)
     untabifyB.place(x=925,y=494, width=157, height=20)
     untabifyB.config(font=("SansSerif", 9, 'normal'))
     untabifyB.config(bg=("#ffffff"))
     untabifyB.config(fg=("#000000"))
     tabifyB = Button(root, text="Change blanks to tab",width=167,height=20,command=tabifyB_action_code)
     tabifyB.place(x=960,y=447, width=167, height=20)
     tabifyB.config(font=("SansSerif", 9, 'normal'))
     tabifyB.config(bg=("#ffffff"))
     tabifyB.config(fg=("#000000"))
     exposed_var=IntVar()
     exposedCB = Checkbutton(root, text="Exposed", variable=exposed_var, command=(lambda what="Exposed":onCheckbuttonPress_exposedCB(what)))
     exposedCB.config(bg=root['bg'])
     exposedCB.place(x=585,y=536, width=124, height=20)
     moreCommandCH = Menubutton(root, text='')
     moreCommandCH.place(x=725,y=520, width=187, height=17)
     moreCommandCH.config(font=("SansSerif", 10, 'normal'))
     moreCommandCH.config(bg=("#ffffff"))
     moreCommandCH.config(fg=("#000000"))
     moreCommandCH.menu = Menu(moreCommandCH, tearoff=0)
     moreCommandCH['menu'] = moreCommandCH.menu
     moreCommandCH_varlist=[]
     moreCommandCH_xvar1=IntVar()
     moreCommandCH_varlist.append(moreCommandCH_xvar1)
     moreCommandCH.menu.add_checkbutton(label='--select--',variable=moreCommandCH_xvar1, command=functools.partial(moreCommandCH_respond, 1))
     moreCommandCH_xvar2=IntVar()
     moreCommandCH_varlist.append(moreCommandCH_xvar2)
     moreCommandCH.menu.add_checkbutton(label='Change tabs to blanks',variable=moreCommandCH_xvar2, command=functools.partial(moreCommandCH_respond, 2))
     moreCommandCH_xvar3=IntVar()
     moreCommandCH_varlist.append(moreCommandCH_xvar3)
     moreCommandCH.menu.add_checkbutton(label='Change blanks to tabs',variable=moreCommandCH_xvar3, command=functools.partial(moreCommandCH_respond, 3))
     moreCommandCH_xvar4=IntVar()
     moreCommandCH_varlist.append(moreCommandCH_xvar4)
     moreCommandCH.menu.add_checkbutton(label='Add curly braces after :',variable=moreCommandCH_xvar4, command=functools.partial(moreCommandCH_respond, 4))
     moreCommandCH.bind("<<ListboxSelect>>", (lambda event: moreCommandCH_item_code()))
     moreL = Label(root, text="Commands:",width=72,height=15)
     moreL.place(x=651,y=520, width=72, height=15)
     moreL.config(font=("SansSerif", 10, 'normal'))
     moreL.config(bg=root['bg'])
     moreL.config(fg=("#000000"))


     root.mainloop()

if __name__ == '__main__':
     main()

####DIRECTIVES
##%START
##%PROGRAM DATE=Tue, Feb 19, 2019 6:41:39 PM
##%VERSION=PY2
##%CLASS_STYLE=no class
##%WHENWRITTEN=Wed Mar 06 22:16:00 EST 2019
##%CLASSNAME=MainWindow
##%PACKAGENAME=
##%DIRECTORY=C:/Users/rmark/Dropbox/SOFTWARE/PYINDENTER
##%GUITYPE=Python
##%EXTRAMETHODS=0
##%PROGTYPE=Application
##%TITLEBAR=Python application
##%SAVEMYTEXTAREA=true
##%SNAPSHOTVARLIST=
##%RUNTIMECLASSPATH=
##%BGIMAGENAME=
##%BGIMAGERESIZE=true
##%USEBGIMAGE=true
##%CANRESIZEMAINWINDOW=true
##%MENUS
##%ENDMENU
##%BGCOLOR=235,235,235
##%WIDTH=930
##%HEIGHT=619
##%COMPONENTS
##%COMPONENT 
##%  id=1
##%  type=Label
##%  label=Filename:
##%  varname=component0BL
##%  startpoint=8,53
##%  endpoint=84,75
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=11
##%  fontstyle=bold
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=
##%  codeItem=
##%END
##%COMPONENT 
##%  id=2
##%  type=TextField
##%  label=
##%  varname=filenameTF
##%  startpoint=85,53
##%  endpoint=720,75
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=10
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=
##%  codeItem=
##%END
##%COMPONENT 
##%  id=3
##%  type=Button
##%  label=Load
##%  varname=loadB
##%  startpoint=721,53
##%  endpoint=762,75
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=11
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=load()
##%  codeItem=
##%END
##%COMPONENT 
##%  id=4
##%  type=Button
##%  label=Save
##%  varname=saveB
##%  startpoint=763,53
##%  endpoint=805,75
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=11
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=save()
##%  codeItem=
##%END
##%COMPONENT 
##%  id=5
##%  type=TextArea
##%  label=
##%  varname=bigTA
##%  startpoint=8,77
##%  endpoint=911,562
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=Monospaced
##%  fontsize=11
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=
##%  codeItem=
##%END
##%COMPONENT 
##%  id=6
##%  type=Label
##%  label=Starting flag:
##%  varname=startflagL
##%  startpoint=6,564
##%  endpoint=95,584
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=11
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=
##%  codeItem=
##%END
##%COMPONENT 
##%  id=7
##%  type=TextField
##%  label=#$start
##%  varname=startFlagTF
##%  startpoint=97,564
##%  endpoint=156,584
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=11
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=
##%  codeItem=
##%END
##%COMPONENT 
##%  id=10
##%  type=TextField
##%  label=#$stop
##%  varname=endFlagTF
##%  startpoint=97,587
##%  endpoint=156,607
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=11
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=
##%  codeItem=
##%END
##%COMPONENT 
##%  id=11
##%  type=Label
##%  label=Stop flag:
##%  varname=endflagL
##%  startpoint=6,587
##%  endpoint=95,607
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=11
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=
##%  codeItem=
##%END
##%COMPONENT 
##%  id=16
##%  type=Label
##%  label=Opening char:
##%  varname=openerL
##%  startpoint=171,564
##%  endpoint=260,584
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=11
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=
##%  codeItem=
##%END
##%COMPONENT 
##%  id=17
##%  type=TextField
##%  label={
##%  varname=openingCharTF
##%  startpoint=262,564
##%  endpoint=284,584
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=11
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=
##%  codeItem=
##%END
##%COMPONENT 
##%  id=18
##%  type=TextField
##%  label=}
##%  varname=closingCharTF
##%  startpoint=262,587
##%  endpoint=283,607
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=11
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=
##%  codeItem=
##%END
##%COMPONENT 
##%  id=19
##%  type=Label
##%  label=Closing char:
##%  varname=closerL
##%  startpoint=171,587
##%  endpoint=260,607
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=11
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=
##%  codeItem=
##%END
##%COMPONENT 
##%  id=20
##%  type=Button
##%  label=Format to Python
##%  varname=goB
##%  startpoint=457,564
##%  endpoint=582,584
##%  fgcolor=0,0,0
##%  bgcolor=0,255,0
##%  fontname=SansSerif
##%  fontsize=10
##%  fontstyle=bold
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=indent()
##%  codeItem=
##%END
##%COMPONENT 
##%  id=21
##%  type=Button
##%  label=Undo
##%  varname=undoB
##%  startpoint=584,564
##%  endpoint=638,584
##%  fgcolor=255,255,255
##%  bgcolor=0,0,0
##%  fontname=SansSerif
##%  fontsize=12
##%  fontstyle=bold
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=undo()
##%  codeItem=
##%END
##%COMPONENT 
##%  id=22
##%  type=Button
##%  label=Save as
##%  varname=saveAsB
##%  startpoint=806,53
##%  endpoint=865,75
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=11
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=save_as()
##%  codeItem=
##%END
##%COMPONENT 
##%  id=23
##%  type=Label
##%  label=Num spaces to indent:
##%  varname=numspacesL
##%  startpoint=290,564
##%  endpoint=429,584
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=10
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=
##%  codeItem=
##%END
##%COMPONENT 
##%  id=24
##%  type=TextField
##%  label=5
##%  varname=numSpacesTF
##%  startpoint=431,564
##%  endpoint=455,584
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=12
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=
##%  codeItem=
##%END
##%COMPONENT 
##%  id=25
##%  type=Label
##%  label=Samples:
##%  varname=samplesL
##%  startpoint=290,586
##%  endpoint=372,607
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=11
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=
##%  codeItem=
##%END
##%COMPONENT 
##%  id=26
##%  type=Choice
##%  label=
##%  varname=samplesCH
##%  startpoint=374,586
##%  endpoint=541,607
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=12
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=samples_var
##%  other=sample 1\nsample 2\nsample 3
##%  codeAction=
##%  codeItem=
##%END
##%COMPONENT 
##%  id=27
##%  type=Button
##%  label=load
##%  varname=loadSampleB
##%  startpoint=543,586
##%  endpoint=582,607
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=10
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=loadSample()
##%  codeItem=
##%END
##%COMPONENT 
##%  id=28
##%  type=Button
##%  label=Help!
##%  varname=helpB
##%  startpoint=866,53
##%  endpoint=911,75
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=12
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=help()
##%  codeItem=
##%END
##%COMPONENT 
##%  id=29
##%  type=Button
##%  label=Change tabs to blanks
##%  varname=untabifyB
##%  startpoint=925,544
##%  endpoint=1082,564
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=9
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=if is_exposed:\n	untabify_exposed()\nelse:\n	untabify_unexposed()
##%  codeItem=
##%END
##%COMPONENT 
##%  id=31
##%  type=Button
##%  label=Change blanks to tab
##%  varname=tabifyB
##%  startpoint=960,497
##%  endpoint=1127,517
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=9
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=if is_exposed:\n	tabify_exposed()\nelse:\n	tabify_unexposed()
##%  codeItem=
##%END
##%COMPONENT 
##%  id=32
##%  type=Checkbox
##%  label=Exposed
##%  varname=exposedCB
##%  startpoint=585,586
##%  endpoint=709,606
##%  fgcolor=0,0,0
##%  bgcolor=235,235,235
##%  fontname=SansSerif
##%  fontsize=11
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=exposed_var
##%  other=
##%  codeAction=
##%  codeItem=global is_exposed\n\n#popup("exposed_var.get() = "+str(exposed_var.get()))\nif exposed_var.get() == 1:\n	is_exposed = True\n	expose()\nelse:\n	is_exposed = False\n	unexpose()
##%END
##%COMPONENT 
##%  id=33
##%  type=Choice
##%  label=
##%  varname=moreCommandCH
##%  startpoint=725,570
##%  endpoint=912,587
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=10
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=more_var
##%  other=--select--\nChange tabs to blanks\nChange blanks to tabs\nAdd curly braces after :
##%  codeAction=
##%  codeItem=moreCommand(gettext(moreCommandCH))
##%END
##%COMPONENT 
##%  id=34
##%  type=Label
##%  label=Commands:
##%  varname=moreL
##%  startpoint=651,570
##%  endpoint=723,585
##%  fgcolor=0,0,0
##%  bgcolor=255,255,255
##%  fontname=SansSerif
##%  fontsize=10
##%  fontstyle=plain
##%  samebgcolor=1
##%  fixedx=0
##%  fixedy=0
##%  resizable=1
##%  filename=
##%  scrollbar_isHorizontal=true
##%  list_rowsMultiselect=false
##%  minval=1
##%  maxval=100
##%  startingval=50
##%  rescaleImage=1
##%  moreoptions=
##%  assocvarname=Button1_var
##%  other=
##%  codeAction=
##%  codeItem=
##%END
##%ENDCOMPONENTS


####END