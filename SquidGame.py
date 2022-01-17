#Player1: Abhiram
#Player2: Ajay
#Player3: Ganesh

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from string import ascii_uppercase
#import pygame
import random

global score
score=0
global bonus
bonus=0


root=Tk()
root.title("Squid Game")
root.iconbitmap("images/sgicon.ico")
w=400
h=200
sw=root.winfo_screenwidth()
sh=root.winfo_screenheight()
x=(sw/2)-(w/2)-50
y=(sh/2)-(h/2)-100
root.geometry(f'{w}x{h}+{int(x)}+{int(y)}')
root.maxsize(400,200)
root.minsize(400,200)

def round1():
    #root.iconify()
    #no=0
    #the_word_withSpaces = ""
    word_list=["WHISKEY","BUFFALO","CYCLE","JIGSAW","JOKING","IVORY","QUEUE","RHYTHM","QUIZZES",
               "PUPPY","YUMMY","JOGGING","PAJAMA","ZIGZAG","KEYHOLE","ZOMBIE","YOUTH","SUBWAY","MATRIX","AWKWARD","GALAXY","GOSSIP","ABSURD",
               "INJURY","BRAVE","FAMILY","HONESTY","ZEBRA","GANDHI","TOXIC","BLIZZARD","JAUNDICE","SLEEP","BUTTER","PAPER","WINTER","GHOST",
               "MIDDLE","DEATH","EARTH","MOUNTAIN","BLOOD","HISTORY","ATTACK","MACHINE","FAITH","LUXURY"];
    hint_list=["An alcoholic beverage","A black animal","Two wheeler","Puzzle","Not serious","Elephant husks","Standing in a line",
               "Music pattern","A short test","Small dog","Delicious","Sprint walking","Nightwear","Not straight",
               "Lock","Graveyard","Teenage","Healthy fast joint","Rows and Columns","Embarrassed","Milky Way",
               "Informal discussion","Not making sense","Wound","Courageous","People you trust","Best policy","Black and White","Non Violence",
               "Poisonous","Snow storm","Yellow fever","Rest","Bread and...","Made from trees","Cold season","Afterlife","In Between",
               "End of life","Planet with water","Place to hike","Flows in veins","In the past","Punch and Kick","Reduces employment","Believing in something",
               "Filthy rich"]
    photos=[PhotoImage(file="images/hang0.png"),PhotoImage(file="images/hang1.png"),PhotoImage(file="images/hang2.png"),
            PhotoImage(file="images/hang3.png"),PhotoImage(file="images/hang4.png"),PhotoImage(file="images/hang5.png"),
            PhotoImage(file="images/hang6.png"),PhotoImage(file="images/hang7.png"),PhotoImage(file="images/hang8.png"),
            PhotoImage(file="images/hang9.png"),PhotoImage(file="images/hang10.png"),PhotoImage(file="images/hang11.png")]
    global the_word_withSpaces
    global no
    global lblWord
    global imgLabel
    global r1
    global score,bonus
    tot=10
    bonus=100
    r1=Toplevel()
    w=493
    h=517
    sw=root.winfo_screenwidth()
    sh=root.winfo_screenheight()
    x=(sw/2)-(w/2)-40
    y=(sh/2)-(h/2)-50
    r1.geometry(f'{w}x{h}+{int(x)}+{int(y)}')
    r1.iconbitmap("images/sgicon.ico")
    #r1.overrideredirect(True)
    
    f1=LabelFrame(r1,text="HANGMAN",font=("Consolas bold",48))
    Label(f1,text="Guess before you get hanged").pack()
    f1.grid(row=0,column=0,padx=70)

    l=random.randint(0,len(word_list)-1)
    the_word=word_list[l]
    the_hint=hint_list[l]
    
    f5=LabelFrame(r1,pady=5)
    f51=LabelFrame(f5,text="Hint",font="Consolas 24 bold",bg="yellow")
    Label(f51,text=the_hint,font="comicsans").grid(row=0,column=0)
    f51.grid(row=1,column=0)
    f52=LabelFrame(f5,text="Score",font="Consolas 24 bold",bg="blue")
    sl=Label(f52,text=str(tot*bonus),font="comicsans")
    sl.grid(row=1,column=1)
    f52.grid(row=1,column=1,padx=20)
    f53=LabelFrame(f5,text="Bonus",font="Consolas 24 bold",bg="red")
    sl2=Label(f53,text=str(bonus),font="comicsans")
    sl2.grid(row=1,column=2)
    f53.grid(row=1,column=2)
    f5.grid(row=1,column=0)

    """f2=LabelFrame(r3)
    f21=LabelFrame(f2,text="Guess",font="Consolas 24 bold",bg="yellow")
    Label(f21,textvariable=lblWord,font="Consolas 24 bold").grid(row=0,column=3,columnspan=6,padx=10)
    f21.grid(row=1,column=0,padx=20)
    f22=LabelFrame(f2,text="Score",font=("Consolas bold",20),bg="blue")
    sl=Label(f22,text=str(score),font="comicsans")
    sl.grid(row=1,column=1)
    f22.grid(row=1,column=1)
    f23=LabelFrame(f2,text="Check",font=("Consolas bold",20),bg="red")
    sl2=Label(f23,text=str(no),font="comicsans")
    sl2.grid(row=1,column=2)
    f23.grid(row=1,column=2,padx=20)
    f2.grid(row=1,column=0)"""
    f2=LabelFrame(r1)
    Label(f2,text="Round 1",font="Consolas 24 bold")
    imgLabel=Label(f2)
    r1.title("Round 1")
    #messagebox.showinfo("HINT",the_hint)
    #imgLabel=Label(r1)
    imgLabel.grid(row=0,column=0,columnspan=3,padx=10,pady=40)
    imgLabel.config(image=photos[0])
    lblWord=StringVar()
    Label(f2,textvariable=lblWord,font="Consolas 24 bold").grid(row=0,column=3,columnspan=6,padx=10)
    #Label(f2,text="Hint:"+the_hint,font=("consolas",20)).grid(row=0,column=0,rowspan=10,columnspan=6,padx=20)
    n=0
    for c in ascii_uppercase:
        b=Button(f2,text=c,command=lambda c=c:guess(c),font=18,width=4)
        b.grid(row=1+n//9,column=n%9)
        n+=1
    no=0
    imgLabel.config(image=photos[0])
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))
    def guess(letter):
        global r1
        global no
        global imgLabel
        global lblWord
        global score,bonus
        if no<11:
            txt=list(the_word_withSpaces)
            guessed=list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    
                    if txt[c]==letter:
                        bonus+=100
                        score=tot*bonus
                        sl.config(text=str(tot*bonus))
                        sl2.config(text=str(bonus),font="comicsans")
                        guessed[c]=letter
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        try:
                            root.iconify()
                            r1.destroy()
                            #breaks()
                            messagebox.showinfo("R1 COMPLETED!","Congrats on surpassing Round 1\n"+"Your score:"+str(score))
                            messagebox.showinfo("R1 COMPLETED!","You can proceed to the next round")
                        except:
                            pass
                        round2()

                    
            else:
                no+=1
                imgLabel.config(image=photos[no])
                if no==11:
                    messagebox.showwarning("Hangman","Game Over\nYour scored "+str(score))
                    r1.destroy()
                    root.state('zoomed')
    f2.grid(row=2,column=0,padx=2)
    r1.mainloop()


def round2():
    global root
    root.iconify()
    r2=Toplevel()
    r2.iconbitmap("images/sgicon.ico")
    w=365
    h=350
    sw=root.winfo_screenwidth()
    sh=root.winfo_screenheight()
    x=(sw/2)-(w/2)-50
    y=(sh/2)-(h/2)-100
    r2.geometry(f'{w}x{h}+{int(x)}+{int(y)}')
    r2.title("Round 2")
    #r2.overrideredirect(True)
    f1=LabelFrame(r2,text="Memory Game",font="Consolas 24 bold")
    Label(f1,text="Pick 2 count 1").pack()
    f1.grid(row=0,column=0)
    global check2
    check2=0
    f5=LabelFrame(r2,pady=5)
    f51=LabelFrame(f5,text="Check",font="Consolas 24 bold",bg="yellow")
    s2=Label(f51,text=str(check2),font="comicsans")
    s2.grid(row=0,column=0)
    f51.grid(row=1,column=0,columnspan=1,padx=40)
    f52=LabelFrame(f5,text="Score",font="Consolas 24 bold",bg="blue")
    sl=Label(f52,text=str(score),font="comicsans")
    sl.grid(row=1,column=1)
    f52.grid(row=1,column=1,columnspan=5,padx=40)
    f5.grid(row=1,column=0)

    matches=[1,1,2,2,3,3,4,4,5,5,6,6]
    random.shuffle(matches)
    f2=LabelFrame(r2)
    #global score
    global count,answer_list,answer_dict
    global check
    count,check=0,0
    answer_list=[]
    answer_dict={}
    def button_click(b,number):
        global check,check2,count,score,answer_list,answer_dict
        if b["text"]==' ' and count<2:
            b["text"]=matches[number]
            answer_list.append(number)
            answer_dict[b]=matches[number]
            count+=1
        if len(answer_list)==2:
            if matches[answer_list[0]]==matches[answer_list[1]]:
                score+=1000
                sl.config(text=score)
                #f2.config(text="Match!")
                for k in answer_dict:
                    k["state"]="disabled"
                check+=1
                #Label(r2,text="Count:"+str(check),font="Consolas 24 bold").pack()
                if(check==6):
                    try:
                        r2.destroy()
                        messagebox.showinfo("R2 COMPLETED!","Congrats one surpassing Round 2\n"+"Your score:"+str(score))
                        messagebox.showinfo("R2 COMPLETED!","You can proceed to the next round")
                    except:
                        pass
                    round3()
                count=0
                answer_list=[]
                answer_dict={}
            else:
                if check2==10:
                    r2.destroy()
                    messagebox.showwarning("Memory Game","Game Over\nYour scored "+str(score))
                    root.state('zoomed')
                else:
                    count=0
                    check2+=1
                    s2.config(text=str(11-check2))
                    answer_list=[]
                    
                    messagebox.showinfo("Reminder","Wrong Guess!")
                    for k in answer_dict:
                        k["text"]=" "
                    answer_dict={}

    b0=Button(f2,text=' ',font="Consolas 24 bold",height=1,width=4,command=lambda:button_click(b0,0))
    b1=Button(f2,text=' ',font="Consolas 24 bold",height=1,width=4,command=lambda:button_click(b1,1))
    b2=Button(f2,text=' ',font="Consolas 24 bold",height=1,width=4,command=lambda:button_click(b2,2))
    b3=Button(f2,text=' ',font="Consolas 24 bold",height=1,width=4,command=lambda:button_click(b3,3))
    b4=Button(f2,text=' ',font="Consolas 24 bold",height=1,width=4,command=lambda:button_click(b4,4))
    b5=Button(f2,text=' ',font="Consolas 24 bold",height=1,width=4,command=lambda:button_click(b5,5))
    b6=Button(f2,text=' ',font="Consolas 24 bold",height=1,width=4,command=lambda:button_click(b6,6))
    b7=Button(f2,text=' ',font="Consolas 24 bold",height=1,width=4,command=lambda:button_click(b7,7))
    b8=Button(f2,text=' ',font="Consolas 24 bold",height=1,width=4,command=lambda:button_click(b8,8))
    b9=Button(f2,text=' ',font="Consolas 24 bold",height=1,width=4,command=lambda:button_click(b9,9))
    b10=Button(f2,text=' ',font="Consolas 24 bold",height=1,width=4,command=lambda:button_click(b10,10))
    b11=Button(f2,text=' ',font="Consolas 24 bold",height=1,width=4,command=lambda:button_click(b11,11))
    
    b0.grid(row=0,column=0)
    b1.grid(row=0,column=1)
    b2.grid(row=0,column=2)
    b3.grid(row=0,column=3)
    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)
    b7.grid(row=1,column=3)
    b8.grid(row=2,column=0)
    b9.grid(row=2,column=1)
    b10.grid(row=2,column=2)
    b11.grid(row=2,column=3)


    f2.grid(row=2,column=0)
    r2.mainloop()


    
def round3():
    global root
    global score
    global no
    no=0
    root.iconify()
    r3=Toplevel()
    r3.iconbitmap("images/sgicon.ico")
    w=510
    h=590
    sw=root.winfo_screenwidth()
    sh=root.winfo_screenheight()
    x=(sw/2)-(w/2)-10
    y=(sh/2)-(h/2)-30
    r3.geometry(f'{w}x{h}+{int(x)}+{int(y)}')
    r3.title("4 Pics 1 Word")
    #r3.overrideredirect(True)
    f1=LabelFrame(r3,text="4 Pics 1 Word",font="Consolas 24 bold")
    Label(f1,text="Enjoy pics art").grid(row=0,column=0)
    word_list=["CURRENT","FLY","MATCH","RIGHT","TIME","TIP","TOMATO","TRACK","TREE","WET","ADDRESS","PAIN","ROCK","SPEED","YELLOW"]
    s1=[PhotoImage(file="images/current.1.png"),PhotoImage(file="images/fly.1.png"),PhotoImage(file="images/match.1.png"),
        PhotoImage(file="images/right.1.png"),PhotoImage(file="images/time.1.png"),PhotoImage(file="images/tip.1.png"),
        PhotoImage(file="images/tomato.1.png"),PhotoImage(file="images/track.1.png"),PhotoImage(file="images/tree.1.png"),
        PhotoImage(file="images/wet.1.png"),PhotoImage(file="images/address.1.png"),PhotoImage(file="images/pain.1.png"),
        PhotoImage(file="images/rock.1.png"),PhotoImage(file="images/speed.1.png"),PhotoImage(file="images/yellow.1.png")]
    s2=[PhotoImage(file="images/current.2.png"),PhotoImage(file="images/fly.2.png"),PhotoImage(file="images/match.2.png"),
        PhotoImage(file="images/right.2.png"),PhotoImage(file="images/time.2.png"),PhotoImage(file="images/tip.2.png"),
        PhotoImage(file="images/tomato.2.png"),PhotoImage(file="images/track.2.png"),PhotoImage(file="images/tree.2.png"),
        PhotoImage(file="images/wet.2.png"),PhotoImage(file="images/address.2.png"),PhotoImage(file="images/pain.2.png"),
        PhotoImage(file="images/rock.2.png"),PhotoImage(file="images/speed.2.png"),PhotoImage(file="images/yellow.2.png")]
    s3=[PhotoImage(file="images/current.3.png"),PhotoImage(file="images/fly.3.png"),PhotoImage(file="images/match.3.png"),
        PhotoImage(file="images/right.3.png"),PhotoImage(file="images/time.3.png"),PhotoImage(file="images/tip.3.png"),
        PhotoImage(file="images/tomato.3.png"),PhotoImage(file="images/track.3.png"),PhotoImage(file="images/tree.3.png"),
        PhotoImage(file="images/wet.3.png"),PhotoImage(file="images/address.3.png"),PhotoImage(file="images/pain.3.png"),
        PhotoImage(file="images/rock.3.png"),PhotoImage(file="images/speed.3.png"),PhotoImage(file="images/yellow.4.png")]
    s4=[PhotoImage(file="images/current.4.png"),PhotoImage(file="images/fly.4.png"),PhotoImage(file="images/match.4.png"),
        PhotoImage(file="images/right.4.png"),PhotoImage(file="images/time.4.png"),PhotoImage(file="images/tip.4.png"),
        PhotoImage(file="images/tomato.4.png"),PhotoImage(file="images/track.4.png"),PhotoImage(file="images/tree.4.png"),
        PhotoImage(file="images/wet.4.png"),PhotoImage(file="images/address.4.png"),PhotoImage(file="images/pain.4.png"),
        PhotoImage(file="images/rock.4.png"),PhotoImage(file="images/speed.3.png"),PhotoImage(file="images/yellow.4.png")]
    l=random.randint(0,9)
    the_word=s=word_list[l]
    Label(f1,image=s1[l]).grid(row=1,column=0)
    Label(f1,image=s2[l]).grid(row=1,column=1)
    Label(f1,image=s3[l]).grid(row=2,column=0)
    Label(f1,image=s4[l]).grid(row=2,column=1)
    f1.grid(row=0,column=0)

    
    global lblWord
    lblWord=StringVar()
    f2=LabelFrame(r3)
    f21=LabelFrame(f2,text="Guess",font="Consolas 24 bold",bg="yellow")
    Label(f21,textvariable=lblWord,font="Consolas 24 bold").grid(row=0,column=3,columnspan=6,padx=10)
    f21.grid(row=1,column=0,padx=20)
    f22=LabelFrame(f2,text="Score",font=("Consolas bold",20),bg="blue")
    sl=Label(f22,text=str(score),font="comicsans")
    sl.grid(row=1,column=1)
    f22.grid(row=1,column=1)
    f23=LabelFrame(f2,text="Check",font=("Consolas bold",20),bg="red")
    sl2=Label(f23,text=str(no),font="comicsans")
    sl2.grid(row=1,column=2)
    f23.grid(row=1,column=2,padx=20)
    f2.grid(row=1,column=0)

    f3=LabelFrame(r3)
    n=0
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))
    for c in ''.join(random.sample("FGHQYALSPRKI", len("FGHQYALSPRKI"))):
        if(len(s)%12!=0):
            s+=c
    for c in ''.join(random.sample(s, len(s))):
        Button(f3,text=c,command=lambda c=c:guess(c),font="Consolas 24 bold",width=4).grid(row=1+n//6,column=n%6)
        n+=1
    f3.grid(row=2,column=0)

    def guess(letter):
        global r1,score
        global no
        global lblWord
        if no<len(the_word):
            txt=list(the_word_withSpaces)
            guessed=list(lblWord.get())
            if the_word_withSpaces.count(letter)>0:
                for c in range(len(txt)):
                    if txt[c]==letter:
                        guessed[c]=letter
                        score+=1000
                        sl.config(text=str(score))
                    lblWord.set("".join(guessed))
                    if lblWord.get()==the_word_withSpaces:
                        try:
                            r3.destroy()
                            messagebox.showinfo("R3 COMPLETED!","Congrats one surpassing Round 3\n"+"Your score:"+str(score))
                            messagebox.showinfo("HURRAY!","Congrats!! You win the game")
                            root.state('zoomed')
                        except:
                            pass
                        break
                    #else:
                     #   messagebox.showwarning("Warning!","Chances remaining:"+str(len(the_word)-1))
                        
                    
            else:
                no+=1
                #s2.config(text=str(no))
                sl2.config(text=str(len(str(lblWord))-no))
                if no==len(str(lblWord)):
                    r3.destroy()
                    messagebox.showwarning("4 Pics 1 Word","Game Over\nYou were able to score "+str(score))
                    root.state('zoomed')
    
    r3.mainloop()


        
#def play():
#    pygame.mixer.music.stop()



def ins():
    r=Toplevel(root)
    r.iconbitmap("images/sgicon.ico")
    r.title("Instructions")
    r.geometry("500x350")
    Label(r,text="INSTRUCTIONS",font=("consolas bold",40)).pack()
    Label(r,text="\nRound 1\nGuess the Correct letters of the Word\nWith any wrong guesses, Man is closer to Death!!\n",font=("consolas bold",10)).pack()
    Label(r,text="\nRound 2\nThis is the Ultimate test of your Memory!! \nRemember the Tile Number and match with Similar Tile\n",font=("consolas bold",10)).pack()
    Label(r,text="\nRound 3\nAre you Creative enough??\nFind the relation between ALL 4 Pictures\n",font=("consolas bold",10)).pack()
    r.mainloop()


image=Image.open("images/logo game.png")
image=image.resize((250,50),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
f1=LabelFrame(root,width=100,height=50,padx=75,pady=30)
Label(f1,image=photo).grid(row=0,column=0)
#pygame.mixer.init()
#pygame.mixer.music.load("music.mp3")
#pygame.mixer.music.play(loops=0)

#my_button=Button(root,text="Stop Song",command=play)
#my_button.pack()

play_button=Button(f1,text="Play Game",font=("fixedsys",11),command=round1,pady=8)
play_button.grid(row=2,column=0)
ins_button=Button(f1,text="View Instructions",font=("fixedsys",11),command=ins,pady=10)
ins_button.grid(row=3,column=0)
#lb_button=Button(f1,text="View Leaderboard",font="fixedsys",pady=5)
#lb_button.grid(row=5,column=0)
f1.grid(row=1,column=0)
root.mainloop()
