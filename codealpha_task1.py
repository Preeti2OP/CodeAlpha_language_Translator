from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox

#GUI page
root = Tk()
root.title('Language Translator')
root.geometry('1000x400')
icon=PhotoImage(file="pngwing.com (6).png")
root.iconphoto(False,icon)


language=googletrans.LANGUAGES
lang=list(language.values())

text1=Text(root,height=15,width=50)
text1.grid(row=3,column=0,padx=10)
text2=Text(root,height=15,width=50)
text2.grid(row=3,column=2,pady=20,padx=10)

#to select language
#input language
colmbo1=ttk.Combobox(root,width=50,value=lang)
colmbo1.current(21)
colmbo1.grid(row=0,column=0)
label1=Label(root,text='Input language',width=15,font='segoe 20 bold',bd=5,relief=GROOVE)
label1.grid(row=1,column=0)

#output language
colmbo2=ttk.Combobox(root,width=50,value=lang)
colmbo2.current(21)
colmbo2.grid(row=0,column=2)
label2=Label(root,text='Output language',width=15,font='segoe 20 bold',bd=5,relief=GROOVE)
label2.grid(row=1,column=2)


def translate():
  try :
      for key, value in language.items():
        if (value == colmbo1.get()):
          from_language_key = key

      for key, value in language.items():
			    if (value == colmbo2.get()):
				     to_language_key = key
      words=textblob.TextBlob(text1.get(1.0, END))
      words = words.translate(from_lang=from_language_key , to=to_language_key)

      text2.insert(1.0, words)
  except Exception as e:
        messagebox.showerror(e)

def clear():
    text1.delete(1.0,END)
    text2.delete(1.0,END)

def label_change():
    c=colmbo1.get()
    c1=colmbo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)
label_change()

button1=Button(root,text='clear',font=("times,40"),command=clear).grid(row=6,column=0)
button=Button(root,text='Translate',font=("times,40"),command=translate).grid(row=6,column=1)

root.mainloop()





