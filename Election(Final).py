from tkinter import *
from PIL import ImageTk ,Image

def main():
    global main
    global bg
    main=Tk()
    main.geometry("1366x768")
    main.configure(bg="black")
    main.title("Election Homepage")
    bg = ImageTk.PhotoImage(Image.open("bg.png"))
    Label(main, image = bg).place(x=0,y=0)
    Label(main, text="Welcome",bg="grey21",fg="gold3",font=("Algerian",(50))).place(x=550,y=15)
    Button(main,text="Voting",bg="grey5",fg="gold3",height=2,width=10,bd=10,font=("Times New Roman",(30)),command=voting).place(x=350,y=250)
    Button(main,text="Counting",bg="grey5",fg="gold3",height=2,width=10,bd=10,font=("Times New Roman",(30)),command=counting).place(x=800,y=250)
    main.mainloop()

def voting():
    global screen
    global bg3
    screen=Toplevel(main)
    screen.geometry("1366x768")
    screen.configure(bg="black")
    screen.title("Voting Homepage")
    bg3=ImageTk.PhotoImage(Image.open("bg8.jpg"))
    Label(screen,image=bg3).place(x=0,y=0)
    Label(screen, text="Welcome to the Election Day",bg="black",fg="red",font=("Algerian",(45))).pack(pady=10)
    Label(screen, text="Select Your house",bg="black",fg="red",font=("Times New Roman",(25))).pack()
    Button(screen, text="Raven"  ,bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=raven).place(x=300,y=200)
    Button(screen, text="Moeven" ,bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=moeven).place(x=300,y=400)
    Button(screen, text="Pelican",bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=pelican).place(x=800,y=200)
    Button(screen, text="Falcon" ,bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=falcon).place(x=800,y=400)
    Button(screen,text="Main Menu",bg="black",fg="red",height=1,width=10,bd=6,font=("Times New Roman",15),command=main_menu).place(x=1200,y=600)

def raven():
    global screen1
    screen1=Toplevel(main)
    screen1.geometry("1366x768")
    screen1.configure(bg="black")
    screen1.title("Raven house")
    Label(screen1,image=bg3).place(x=0,y=0)
    Label(screen1,text="Raven House",bg="black",fg="blue",font=('Algerian',45)).pack(pady=20)
    Button(screen1, text="Captain",bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=raven_captain_vote).place(x=400,y=275)
    Button(screen1, text="Vice-Captain"  ,bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='disabled',command=raven_vice_vote).place(x=700,y=275)
    Button(screen1,text="Back",bg="black",fg="blue",height=1,width=5,bd=5,font=('Times New Roman',15),command=destroy1).place(x=1200,y=600)
    
def raven_captain_vote():
    global screen2
    screen2=Toplevel(main)
    screen2.geometry("1366x768")
    screen2.configure(bg="black")
    screen2.title("Raven")
    Label(screen2,image=bg3).place(x=0,y=0)
    Label(screen2,text="Choose your candidate",bg="black",fg="blue",font=("Algerian",(40))).pack(pady=10)
    Button(screen2, text="Candidate A",bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=rc_a).place(x=350,y=200)
    Button(screen2, text="Candidate B",bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=rc_b).place(x=350,y=400)
    Button(screen2, text="Candidate C",bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=rc_c).place(x=800,y=200)
    Button(screen2, text="Candidate D",bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=rc_d).place(x=800,y=400)

def raven_vice_vote():
    global screen3
    screen3=Toplevel(main)
    screen3.geometry("1366x768")
    screen3.configure(bg="black")
    screen3.title("Raven")
    Label(screen3,image=bg3).place(x=0,y=0)
    Label(screen3,text="Choose your candidate",bg="black",fg="blue",font=("Algerian",(40))).pack(pady=10)
    Button(screen3, text="Candidate A",bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=rvc_a).place(x=350,y=200)
    Button(screen3, text="Candidate B",bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=rvc_b).place(x=350,y=400)
    Button(screen3, text="Candidate C",bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=rvc_c).place(x=800,y=200)
    Button(screen3, text="Candidate D",bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=rvc_d).place(x=800,y=400)

def moeven():
    global screen4
    screen4=Toplevel(main)
    screen4.geometry("1366x768")
    screen4.configure(bg="black")
    screen4.title("Moeven")
    Label(screen4,image=bg3).place(x=0,y=0)
    Button(screen4, text="Captain"  ,bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=moeven_captain_vote).place(x=400,y=275)
    Button(screen4, text="Vice-Captain"  ,bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='disabled',command=moeven_vice_vote).place(x=700,y=275)
    Button(screen4,text="Back",bg="black",fg="green2",height=1,width=5,bd=5,font=('Times New Roman',15),command=destroy2).place(x=1200,y=600)
    
def moeven_captain_vote():
    global screen5
    screen5=Toplevel(main)
    screen5.geometry("1366x768")
    screen5.configure(bg="black")
    screen5.title("Moeven Captain")
    Label(screen5,image=bg3).place(x=0,y=0)
    Label(screen5,text="Choose your candidate",bg="black",fg="green2",font=("Algerian",(40))).pack(pady=10)
    Button(screen5, text="Candidate A",bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=mc_a).place(x=350,y=200)
    Button(screen5, text="Candidate B",bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=mc_b).place(x=350,y=400)
    Button(screen5, text="Candidate C",bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=mc_c).place(x=800,y=200)
    Button(screen5, text="Candidate D",bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=mc_d).place(x=800,y=400)

def moeven_vice_vote():
    global screen6
    screen6=Toplevel(main)
    screen6.geometry("1366x768")
    screen6.configure(bg="black")
    screen6.title("Moeven Vice Captain")
    Label(screen6,image=bg3).place(x=0,y=0)
    Label(screen6,text="Choose your candidate",bg="black",fg="green2",font=("Algerian",(40))).pack(pady=10)
    Button(screen6, text="Candidate A",bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=mvc_a).place(x=350,y=200)
    Button(screen6, text="Candidate B",bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=mvc_b).place(x=350,y=400)
    Button(screen6, text="Candidate C",bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=mvc_c).place(x=800,y=200)
    Button(screen6, text="Candidate D",bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=mvc_d).place(x=800,y=400)

def pelican():
    global screen7
    screen7=Toplevel(main)
    screen7.geometry("1366x768")
    screen7.configure(bg="black")
    screen7.title("Pelican house")
    Label(screen7,image=bg3).place(x=0,y=0)
    Button(screen7, text="Captain"  ,bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=pelican_captain_vote).place(x=400,y=275)
    Button(screen7, text="Vice-Captain"  ,bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",25),state='disabled',command=pelican_vice_vote).place(x=700,y=275)
    Button(screen7,text="Back",bg="black",fg="yellow",height=1,width=5,bd=5,font=('Times New Roman',15),command=destroy3).place(x=1200,y=600)
    
def pelican_captain_vote():
    global screen8
    screen8=Toplevel(main)
    screen8.geometry("1366x768")
    screen8.configure(bg="black")
    screen8.title("Pelican Captain")
    Label(screen8,image=bg3).place(x=0,y=0)
    Label(screen8,text="Choose your candidate",bg="black",fg="yellow",font=("Algerian",(40))).pack(pady=10)
    Button(screen8, text="Candidate A",bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=pc_a).place(x=350,y=200)
    Button(screen8, text="Candidate B",bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=pc_b).place(x=350,y=400)
    Button(screen8, text="Candidate C",bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=pc_c).place(x=800,y=200)
    Button(screen8, text="Candidate D",bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=pc_d).place(x=800,y=400)

def pelican_vice_vote():
    global screen9
    screen9=Toplevel(main)
    screen9.geometry("1366x768")
    screen9.configure(bg="black")
    screen9.title("Pelican")
    Label(screen9,image=bg3).place(x=0,y=0)
    Label(screen9,text="Choose your candidate",bg="black",fg="yellow",font=("Algerian",(40))).pack(pady=10)
    Button(screen9, text="Candidate A",bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=pvc_a).place(x=350,y=200)
    Button(screen9, text="Candidate B",bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=pvc_b).place(x=350,y=400)
    Button(screen9, text="Candidate C",bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=pvc_c).place(x=800,y=200)
    Button(screen9, text="Candidate D",bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=pvc_d).place(x=800,y=400)

def falcon():
    global screen10
    screen10=Toplevel(main)
    screen10.geometry("1366x768")
    screen10.configure(bg="black")
    screen10.title("Falcon")
    Label(screen10,image=bg3).place(x=0,y=0)
    Button(screen10, text="Captain"  ,bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=falcon_captain_vote).place(x=400,y=275)
    Button(screen10, text="Vice-Captain"  ,bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='disabled',command=falcon_vice_vote).place(x=700,y=275)
    Button(screen10,text="Back",bg="black",fg="orange",height=1,width=5,bd=5,font=('Times New Roman',15),command=destroy4).place(x=1200,y=600)

def falcon_captain_vote():
    global screen11
    screen11=Toplevel(main)
    screen11.geometry("1366x768")
    screen11.configure(bg="black")
    screen11.title("Falcon")
    Label(screen11,image=bg3).place(x=0,y=0)
    Label(screen11,text="Choose your candidate",bg="black",fg="orange",font=("Algerian",(40))).pack(pady=10)
    Button(screen11, text="Candidate A",bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=fc_a).place(x=350,y=200)
    Button(screen11, text="Candidate B",bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=fc_b).place(x=350,y=400)
    Button(screen11, text="Candidate C",bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=fc_c).place(x=800,y=200)
    Button(screen11, text="Candidate D",bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=fc_d).place(x=800,y=400)

def falcon_vice_vote():
    global screen12
    screen12=Toplevel(main)
    screen12.geometry("1366x768")
    screen12.configure(bg="black")
    screen12.title("Falcon")
    Label(screen12,image=bg3).place(x=0,y=0)
    Label(screen12,text="Choose your candidate",bg="black",fg="orange",font=("Algerian",(40))).pack(pady=10)
    Button(screen12, text="Candidate A",bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=fvc_a).place(x=350,y=200)
    Button(screen12, text="Candidate B",bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=fvc_b).place(x=350,y=400)
    Button(screen12, text="Candidate C",bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=fvc_c).place(x=800,y=200)
    Button(screen12, text="Candidate D",bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=fvc_d).place(x=800,y=400)

def rc_a():
    global screen14
    screen14=Toplevel(main)
    screen14.geometry("1366x768")
    screen14.configure(bg="black")
    screen14.title("Please Wait")
    Label(screen14,image=bg3).place(x=0,y=0)
    Label(screen14,text="PLEASE WAIT",font=('Algerian',40),bg="black",fg="blue").pack(pady=150)
    screen14.after(1500,destroy14)
    f=open("Raven.txt","a")
    f.write("rc1\n")
    f.close()
    screen2.destroy()
    Button(screen1, text="Vice-Captain"  ,bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='normal',command=raven_vice_vote).place(x=700,y=275)
    Button(screen1, text="Captain",bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='disabled',command=raven_captain_vote).place(x=400,y=275)

def rc_b():
    global screen14
    screen14=Toplevel(main)
    screen14.geometry("1366x768")
    screen14.configure(bg="black")
    screen14.title("Please Wait")
    Label(screen14,image=bg3).place(x=0,y=0)
    Label(screen14,text="PLEASE WAIT",font=('Algerian',40),bg="black",fg="blue").pack(pady=200)
    screen14.after(1500,destroy14)
    f=open("Raven.txt","a")
    f.write("rc2\n")
    f.close()
    screen2.destroy()
    Button(screen1, text="Vice-Captain"  ,bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='normal',command=raven_vice_vote).place(x=700,y=275)
    Button(screen1, text="Captain",bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='disabled',command=raven_captain_vote).place(x=400,y=275)

def rc_c():
    global screen14
    screen14=Toplevel(main)
    screen14.geometry("1366x768")
    screen14.configure(bg="black")
    screen14.title("Please Wait")
    Label(screen14,image=bg3).place(x=0,y=0)
    Label(screen14,text="PLEASE WAIT",font=('Algerian',40),bg="black",fg="blue").pack(pady=200)
    screen14.after(1500,destroy14)
    f=open("Raven.txt","a")
    f.write("rc3\n")
    f.close()
    screen2.destroy()
    Button(screen1, text="Vice-Captain"  ,bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='normal',command=raven_vice_vote).place(x=700,y=275)
    Button(screen1, text="Captain",bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='disabled',command=raven_captain_vote).place(x=400,y=275)

def rc_d():
    global screen14
    screen14=Toplevel(main)
    screen14.geometry("1366x768")
    screen14.configure(bg="black")
    screen14.title("Please Wait")
    Label(screen14,image=bg3).place(x=0,y=0)
    Label(screen14,text="PLEASE WAIT",font=('Algerian',40),bg="black",fg="blue").pack(pady=200)
    screen14.after(1500,destroy14)
    f=open("Raven.txt","a")
    f.write("rc4\n")
    f.close()
    screen2.destroy()
    Button(screen1, text="Vice-Captain"  ,bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='normal',command=raven_vice_vote).place(x=700,y=275)
    Button(screen1, text="Captain",bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='disabled',command=raven_captain_vote).place(x=400,y=275)

def mc_a():
    global screen14
    screen14=Toplevel(main)
    screen14.geometry("1366x768")
    screen14.configure(bg="black")
    screen14.title("Please Wait")
    Label(screen14,image=bg3).place(x=0,y=0)
    Label(screen14,text="PLEASE WAIT",font=('Algerian',40),bg="black",fg="green2").pack(pady=200)
    screen14.after(1500,destroy14)
    f=open("Moeven.txt","a")
    f.write("mc1\n")
    f.close()
    screen5.destroy()
    Button(screen4, text="Vice-Captain"  ,bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='normal',command=moeven_vice_vote).place(x=700,y=275)
    Button(screen4, text="Captain"  ,bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='disabled',command=moeven_captain_vote).place(x=400,y=275)

def mc_b():
    global screen14
    screen14=Toplevel(main)
    screen14.geometry("1366x768")
    screen14.configure(bg="black")
    screen14.title("Please Wait")
    Label(screen14,image=bg3).place(x=0,y=0)
    Label(screen14,text="PLEASE WAIT",font=('Algerian',40),bg="black",fg="green2").pack(pady=200)
    screen14.after(1500,destroy14)
    f=open("Moeven.txt","a")
    f.write("mc2\n")
    f.close()
    screen5.destroy()
    Button(screen4, text="Vice-Captain"  ,bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='normal',command=moeven_vice_vote).place(x=700,y=275)
    Button(screen4, text="Captain"  ,bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='disabled',command=moeven_captain_vote).place(x=400,y=275)

def mc_c():
    global screen14
    screen14=Toplevel(main)
    screen14.geometry("1366x768")
    screen14.configure(bg="black")
    screen14.title("Please Wait")
    Label(screen14,image=bg3).place(x=0,y=0)
    Label(screen14,text="PLEASE WAIT",font=('Algerian',40),bg="black",fg="green2").pack(pady=200)
    screen14.after(1500,destroy14)
    f=open("Moeven.txt","a")
    f.write("mc3\n")
    f.close()
    screen5.destroy()
    Button(screen4, text="Vice-Captain"  ,bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='normal',command=moeven_vice_vote).place(x=700,y=275)
    Button(screen4, text="Captain"  ,bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='disabled',command=moeven_captain_vote).place(x=400,y=275)

def mc_d():
    global screen14
    screen14=Toplevel(main)
    screen14.geometry("1366x768")
    screen14.configure(bg="black")
    screen14.title("Please Wait")
    Label(screen14,image=bg3).place(x=0,y=0)
    Label(screen14,text="PLEASE WAIT",font=('Algerian',40),bg="black",fg="green2").pack(pady=200)
    screen14.after(1500,destroy14)
    f=open("Moeven.txt","a")
    f.write("mc4\n")
    f.close()
    screen5.destroy()
    Button(screen4, text="Vice-Captain"  ,bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='normal',command=moeven_vice_vote).place(x=700,y=275)
    Button(screen4, text="Captain"  ,bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='disabled',command=moeven_captain_vote).place(x=400,y=275)

def pc_a():
    global screen14
    screen14=Toplevel(main)
    screen14.geometry("1366x768")
    screen14.configure(bg="black")
    screen14.title("Please Wait")
    Label(screen14,image=bg3).place(x=0,y=0)
    Label(screen14,text="PLEASE WAIT",font=('Algerian',40),bg="black",fg="yellow").pack(pady=200)
    screen14.after(1500,destroy14)
    f=open("Pelican.txt","a")
    f.write("pc1\n")
    f.close()
    screen8.destroy()
    Button(screen7, text="Vice-Captain"  ,bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='normal',command=pelican_vice_vote).place(x=700,y=275)
    Button(screen7, text="Captain"  ,bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='disabled',command=pelican_captain_vote).place(x=400,y=275)

def pc_b():
    global screen14
    screen14=Toplevel(main)
    screen14.geometry("1366x768")
    screen14.configure(bg="black")
    screen14.title("Please Wait")
    Label(screen14,image=bg3).place(x=0,y=0)
    Label(screen14,text="PLEASE WAIT",font=('Algerian',40),bg="black",fg="yellow").pack(pady=200)
    screen14.after(1500,destroy14)
    f=open("Pelican.txt","a")
    f.write("pc2\n")
    f.close()
    screen8.destroy()
    Button(screen7, text="Vice-Captain"  ,bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='normal',command=pelican_vice_vote).place(x=700,y=275)
    Button(screen7, text="Captain"  ,bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='disabled',command=pelican_captain_vote).place(x=400,y=275)
    
def pc_c():
    global screen14
    screen14=Toplevel(main)
    screen14.geometry("1366x768")
    screen14.configure(bg="black")
    screen14.title("Please Wait")
    Label(screen14,image=bg3).place(x=0,y=0)
    Label(screen14,text="PLEASE WAIT",font=('Algerian',40),bg="black",fg="yellow").pack(pady=200)
    screen14.after(1500,destroy14)
    f=open("Pelican.txt","a")
    f.write("pc3\n")
    f.close()
    screen8.destroy()
    Button(screen7, text="Vice-Captain"  ,bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='normal',command=pelican_vice_vote).place(x=700,y=275)
    Button(screen7, text="Captain"  ,bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='disabled',command=pelican_captain_vote).place(x=400,y=275)    

def pc_d():
    global screen14
    screen14=Toplevel(main)
    screen14.geometry("1366x768")
    screen14.configure(bg="black")
    screen14.title("Please Wait")
    Label(screen14,image=bg3).place(x=0,y=0)
    Label(screen14,text="PLEASE WAIT",font=('Algerian',40),bg="black",fg="yellow").pack(pady=200)
    screen14.after(1500,destroy14)
    f=open("Pelican.txt","a")
    f.write("pc4\n")
    f.close()
    screen8.destroy()
    Button(screen7, text="Vice-Captain"  ,bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='normal',command=pelican_vice_vote).place(x=700,y=275)
    Button(screen7, text="Captain"  ,bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='disabled',command=pelican_captain_vote).place(x=400,y=275)
    
def fc_a():
    global screen14
    screen14=Toplevel(main)
    screen14.geometry("1366x768")
    screen14.configure(bg="black")
    screen14.title("Please Wait")
    Label(screen14,image=bg3).place(x=0,y=0)
    Label(screen14,text="PLEASE WAIT",font=('Algerian',40),bg="black",fg="orange").pack(pady=200)
    screen14.after(1500,destroy14)
    f=open("Falcon.txt","a")
    f.write("fc1\n")
    f.close()
    screen11.destroy()
    Button(screen10, text="Vice-Captain"  ,bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='normal',command=falcon_vice_vote).place(x=700,y=275)
    Button(screen10, text="Captain"  ,bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='disabled',command=falcon_captain_vote).place(x=400,y=275)

def fc_b():
    global screen14
    screen14=Toplevel(main)
    screen14.geometry("1366x768")
    screen14.configure(bg="black")
    screen14.title("Please Wait")
    Label(screen14,image=bg3).place(x=0,y=0)
    Label(screen14,text="PLEASE WAIT",font=('Algerian',40),bg="black",fg="orange").pack(pady=200)
    screen14.after(1500,destroy14)
    f=open("Falcon.txt","a")
    f.write("fc2\n")
    f.close()
    screen11.destroy()
    Button(screen10, text="Vice-Captain"  ,bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='normal',command=falcon_vice_vote).place(x=700,y=275)
    Button(screen10, text="Captain"  ,bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='disabled',command=falcon_captain_vote).place(x=400,y=275)

def fc_c():
    global screen14
    screen14=Toplevel(main)
    screen14.geometry("1366x768")
    screen14.configure(bg="black")
    screen14.title("Please Wait")
    Label(screen14,image=bg3).place(x=0,y=0)
    Label(screen14,text="PLEASE WAIT",font=('Algerian',40),bg="black",fg="orange").pack(pady=200)
    screen14.after(1500,destroy14)
    f=open("Falcon.txt","a")
    f.write("fc3\n")
    f.close()
    screen11.destroy()
    Button(screen10, text="Vice-Captain"  ,bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='normal',command=falcon_vice_vote).place(x=700,y=275)
    Button(screen10, text="Captain"  ,bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='disabled',command=falcon_captain_vote).place(x=400,y=275)

def fc_d():
    global screen14
    screen14=Toplevel(main)
    screen14.geometry("1366x768")
    screen14.configure(bg="black")
    screen14.title("Please Wait")
    Label(screen14,image=bg3).place(x=0,y=0)
    Label(screen14,text="PLEASE WAIT",font=('Algerian',40),bg="black",fg="orange").pack(pady=200)
    screen14.after(1500,destroy14)
    f=open("Falcon.txt","a")
    f.write("fc4\n")
    f.close()
    screen11.destroy()
    Button(screen10, text="Vice-Captain"  ,bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='normal',command=falcon_vice_vote).place(x=700,y=275)
    Button(screen10, text="Captain"  ,bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),state='disabled',command=falcon_captain_vote).place(x=400,y=275)

def rvc_a():
    global screen13
    screen13=Toplevel(main)
    screen13.geometry("1366x768")
    screen13.configure(bg="black")

    screen13.title("Thank you")
    Label(screen13,image=bg3).place(x=0,y=0)
    Label(screen13,text='''THANK YOU FOR VOTING
HAVE A GREAT DAY!!''',font=('Algerian',40),bg="black",fg="blue").pack(pady=150)
    screen13.after(5000,destroy13)
    f=open("Raven.txt","a")
    f.write("rvc1\n")
    f.close()
    screen1.destroy()
    screen3.destroy()
    
def rvc_b():
    global screen13
    screen13=Toplevel(main)
    screen13.geometry("1366x768")
    screen13.configure(bg="black")
    screen13.title("Thank you")
    Label(screen13,image=bg3).place(x=0,y=0)
    Label(screen13,text='''THANK YOU FOR VOTING
HAVE A GREAT DAY!!''',font=('Algerian',40),bg="black",fg="blue").pack(pady=150)
    screen13.after(5000,destroy13)
    f=open("Raven.txt","a")
    f.write("rvc2\n")
    f.close()
    screen1.destroy()
    screen3.destroy()
    
def rvc_c():
    global screen13
    screen13=Toplevel(main)
    screen13.geometry("1366x768")
    screen13.configure(bg="black")
    screen13.title("Thank you")
    Label(screen13,image=bg3).place(x=0,y=0)
    Label(screen13,text='''THANK YOU FOR VOTING
HAVE A GREAT DAY!!''',font=('Algerian',40),bg="black",fg="blue").pack(pady=150)
    screen13.after(5000,destroy13)
    f=open("Raven.txt","a")
    f.write("rvc3\n")
    f.close()
    screen1.destroy()
    screen3.destroy()
    
def rvc_d():
    global screen13
    screen13=Toplevel(main)
    screen13.geometry("1366x768")
    screen13.configure(bg="black")
    screen13.title("Thank you")
    Label(screen13,image=bg3).place(x=0,y=0)
    Label(screen13,text='''THANK YOU FOR VOTING
HAVE A GREAT DAY!!''',font=('Algerian',40),bg="black",fg="blue").pack(pady=150)
    screen13.after(5000,destroy13)
    f=open("Raven.txt","a")
    f.write("rvc4\n")
    f.close()
    screen1.destroy()
    screen3.destroy()
    
def mvc_a():
    global screen13
    screen13=Toplevel(main)
    screen13.geometry("1366x768")
    screen13.configure(bg="black")
    screen13.title("Thank you")
    Label(screen13,image=bg3).place(x=0,y=0)
    Label(screen13,text='''THANK YOU FOR VOTING
HAVE A GREAT DAY!!''',font=('Algerian',40),bg="black",fg="green2").pack(pady=150)
    screen13.after(5000,destroy13)
    f=open("Moeven.txt","a")
    f.write("mvc1\n")
    f.close()
    screen4.destroy()
    screen6.destroy()

def mvc_b():
    global screen13
    screen13=Toplevel(main)
    screen13.geometry("1366x768")
    screen13.configure(bg="black")
    screen13.title("Thank you")
    Label(screen13,image=bg3).place(x=0,y=0)
    Label(screen13,text='''THANK YOU FOR VOTING
HAVE A GREAT DAY!!''',font=('Algerian',40),bg="black",fg="green2").pack(pady=150)
    screen13.after(5000,destroy13)
    f=open("Moeven.txt","a")
    f.write("mvc2\n")
    f.close()
    screen4.destroy()
    screen6.destroy()
    
def mvc_c():
    global screen13
    screen13=Toplevel(main)
    screen13.geometry("1366x768")
    screen13.configure(bg="black")
    screen13.title("Thank you")
    Label(screen13,image=bg3).place(x=0,y=0)
    Label(screen13,text='''THANK YOU FOR VOTING
HAVE A GREAT DAY!!''',font=('Algerian',40),bg="black",fg="green2").pack(pady=150)
    screen13.after(5000,destroy13)
    f=open("Moeven.txt","a")
    f.write("mvc3\n")
    f.close()
    screen4.destroy()
    screen6.destroy()
    
def mvc_d():
    global screen13
    screen13=Toplevel(main)
    screen13.geometry("1366x768")
    screen13.configure(bg="black")
    screen13.title("Thank you")
    Label(screen13,image=bg3).place(x=0,y=0)
    Label(screen13,text='''THANK YOU FOR VOTING
HAVE A GREAT DAY!!''',font=('Algerian',40),bg="black",fg="green2").pack(pady=150)
    screen13.after(5000,destroy13)
    f=open("Moeven.txt","a")
    f.write("mvc4\n")
    f.close()
    screen4.destroy()
    screen6.destroy()
    
def pvc_a():
    global screen13
    screen13=Toplevel(main)
    screen13.geometry("1366x768")
    screen13.configure(bg="black")
    screen13.title("Thank you")
    Label(screen13,image=bg3).place(x=0,y=0)
    Label(screen13,text='''THANK YOU FOR VOTING
HAVE A GREAT DAY!!''',font=('Algerian',40),bg="black",fg="yellow").pack(pady=150)
    screen13.after(5000,destroy13)
    f=open("Pelican.txt","a")
    f.write("pvc1\n")
    f.close()
    screen7.destroy()
    screen9.destroy()
    
def pvc_b():
    global screen13
    screen13=Toplevel(main)
    screen13.geometry("1366x768")
    screen13.configure(bg="black")
    screen13.title("Thank you")
    Label(screen13,image=bg3).place(x=0,y=0)
    Label(screen13,text='''THANK YOU FOR VOTING
HAVE A GREAT DAY!!''',font=('Algerian',40),bg="black",fg="yellow").pack(pady=150)
    screen13.after(5000,destroy13)
    f=open("Pelican.txt","a")
    f.write("pvc2\n")
    f.close()
    screen7.destroy()
    screen9.destroy()
    
def pvc_c():
    global screen13
    screen13=Toplevel(main)
    screen13.geometry("1366x768")
    screen13.configure(bg="black")
    screen13.title("Thank you")
    Label(screen13,image=bg3).place(x=0,y=0)
    Label(screen13,text='''THANK YOU FOR VOTING
HAVE A GREAT DAY!!''',font=('Algerian',40),bg="black",fg="yellow").pack(pady=150)
    screen13.after(5000,destroy13)
    f=open("Pelican.txt","a")
    f.write("pvc3\n")
    f.close()
    screen7.destroy()
    screen9.destroy()
    
def pvc_d():
    global screen13
    screen13=Toplevel(main)
    screen13.geometry("1366x768")
    screen13.configure(bg="black")
    screen13.title("Thank you")
    Label(screen13,image=bg3).place(x=0,y=0)
    Label(screen13,text='''THANK YOU FOR VOTING
HAVE A GREAT DAY!!''',font=('Algerian',40),bg="black",fg="yellow").pack(pady=150)
    screen13.after(5000,destroy13)
    f=open("Pelican.txt","a")
    f.write("pvc4\n")
    f.close()
    screen7.destroy()
    screen9.destroy()
    
def fvc_a():
    global screen13
    screen13=Toplevel(main)
    screen13.geometry("1366x768")
    screen13.configure(bg="black")
    screen13.title("Thank you")
    Label(screen13,image=bg3).place(x=0,y=0)
    Label(screen13,text='''THANK YOU FOR VOTING
HAVE A GREAT DAY!!''',font=('Algerian',40),bg="black",fg="orange").pack(pady=150)
    screen13.after(5000,destroy13)
    f=open("Falcon.txt","a")
    f.write("fvc1\n")
    f.close()
    screen10.destroy()
    screen12.destroy()
    
def fvc_b():
    global screen13
    screen13=Toplevel(main)
    screen13.geometry("1366x768")
    screen13.configure(bg="black")
    screen13.title("Thank you")
    Label(screen13,image=bg3).place(x=0,y=0)
    Label(screen13,text='''THANK YOU FOR VOTING
HAVE A GREAT DAY!!''',font=('Algerian',40),bg="black",fg="orange").pack(pady=150)
    screen13.after(5000,destroy13)
    f=open("Falcon.txt","a")
    f.write("fvc2\n")
    f.close()
    screen10.destroy()
    screen12.destroy()
    
def fvc_c():
    global screen13
    screen13=Toplevel(main)
    screen13.geometry("1366x768")
    screen13.configure(bg="black")
    screen13.title("Thank you")
    Label(screen13,image=bg3).place(x=0,y=0)
    Label(screen13,text='''THANK YOU FOR VOTING
HAVE A GREAT DAY!!''',font=('Algerian',40),bg="black",fg="orange").pack(pady=150)
    screen13.after(5000,destroy13)
    f=open("Falcon.txt","a")
    f.write("fvc3\n")
    f.close()
    screen10.destroy()
    screen12.destroy()
    
def fvc_d():
    global screen13
    screen13=Toplevel(main)
    screen13.geometry("1366x768")
    screen13.configure(bg="black")
    screen13.title("Thank you")
    Label(screen13,image=bg3).place(x=0,y=0)
    Label(screen13,text='''THANK YOU FOR VOTING
HAVE A GREAT DAY!!''',font=('Algerian',40),bg="black",fg="orange").pack(pady=150)
    screen13.after(5000,destroy13)
    f=open("Falcon.txt","a")
    f.write("fvc4\n")
    f.close()
    screen10.destroy()
    screen12.destroy()

def destroy1():
    screen1.destroy()

def destroy2():
    screen4.destroy()

def destroy3():
    screen7.destroy()

def destroy4():
    screen10.destroy()
    
def destroy13():
    screen13.destroy()

def destroy14():
    screen14.destroy()

def main_menu():
    screen.destroy()

#-----------------------------------------------Counting----------------------------------------------------

def counting():
    global cscreen
    global bg3
    cscreen=Toplevel(main)
    cscreen.geometry("1366x768")
    cscreen.configure(bg="black")
    cscreen.title("Counting Homepage")
    bg3=ImageTk.PhotoImage(Image.open("bg8.jpg"))
    Label(cscreen,image=bg3).place(x=0,y=0)
    Label(cscreen,text="Select House",bg="black",fg="red",font=('Algerian',(45))).place(x=450,y=10)
    Button(cscreen, text="Raven"  ,bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=raven_count).place(x=300,y=200)
    Button(cscreen, text="Moeven" ,bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=moeven_count).place(x=300,y=400)
    Button(cscreen, text="Pelican",bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=pelican_count).place(x=800,y=200)
    Button(cscreen, text="Falcon" ,bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=falcon_count).place(x=800,y=400)
    Button(cscreen,text="Main Menu",bg="black",fg="red",height=1,width=10,bd=6,font=('Times New Roman',15),command=main_menu_c).place(x=1200,y=600)

def main_menu_c():
    cscreen.destroy()


#------------------------------------------------------Raven-------------------------------------------------


    
    
def raven_count():
    global rc1,rc2,rc3,rc4,rvc1,rvc2,rvc3,rvc4
    file=open("Raven.txt","r")
    read=file.read()
    read1=read.split()
    rc1=0
    rc2=0
    rc3=0
    rc4=0
    rvc1=0
    rvc2=0
    rvc3=0
    rvc4=0
    for i in read1:
        if i=="rc1":
            rc1+=1
        elif i=="rc2":
            rc2+=1
        elif i=="rc3":
            rc3+=1
        elif i=="rc4":
            rc4+=1
        elif i=="rvc1":
            rvc1+=1
        elif i=="rvc2":
            rvc2+=1
        elif i=="rvc3":
            rvc3+=1
        elif i=="rvc4":
            rvc4+=1
    global rscreen
    rscreen=Toplevel(main)
    rscreen.geometry("1366x768")
    rscreen.configure(bg="black")
    rscreen.title("Raven Counting")
    Label(rscreen,image=bg3).place(x=0,y=0)
    Label(rscreen, text="Raven Vote Count",bg="black",fg="blue",font=("Algerian",(45))).pack(pady=30)
    Button(rscreen,text="Captain",bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=rc).place(x=400,y=275)
    Button(rscreen, text="Vice Captain",bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=rvc).place(x=700,y=275)
    Button(rscreen,text="Back",bg="black",fg="blue",height=1,width=10,bd=6,font=('Times New Roman',15),command=main_menu1).place(x=1200,y=600)


def rc():
    global rscreen1
    rscreen1=Toplevel(main)
    rscreen1.geometry("1366x768")
    rscreen1.configure(bg="black")
    rscreen1.title("Raven Captain")
    Label(rscreen1,image=bg3).place(x=0,y=0)
    Label(rscreen1,text="Votes secured by Candidate A - %s" % (rc1) ,bg="black",fg="blue",font=("Times New Roman",(30))).place(x=400,y=50)
    Label(rscreen1,text="Votes secured by Candidate B - %s" % (rc2),bg="black",fg="blue",font=("Times New Roman",(30))).place(x=400,y=120)
    Label(rscreen1,text="Votes secured by Candidate C - %s" % (rc3),bg="black",fg="blue",font=("Times New Roman",(30))).place(x=400,y=190)
    Label(rscreen1,text="Votes secured by Candidate D - %s" % (rc4),bg="black",fg="blue",font=("Times New Roman",(30))).place(x=400,y=260)
    Button(rscreen1,text="Winner",bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=rwin1).place(x=550,y=400)
    Button(rscreen1,text="Back",bg="black",fg="blue",height=1,width=5,bd=5,font=("Times New Roman",(15)),command=rback1).place(x=1200,y=600)
    
def rwin1():
    if rc1>rc2 and rc1>rc3 and rc1>rc4:
        Label(rscreen1,text="!!! Candidate A is the Winner !!!",bg="black",fg="blue",font=('Times New Roman',(30))).place(x=400,y=550)
    elif rc2>rc1 and rc2>rc3 and rc2>rc4:
        Label(rscreen1,text="!!! Candidate B is the Winner !!!",bg="black",fg="blue",font=('Times New Roman',(30))).place(x=400,y=550)
    elif rc3>rc1 and rc3>rc2 and rc3>rc4:
        Label(rscreen1,text="!!! Candidate C is the Winner !!!",bg="black",fg="blue",font=('Times New Roman',(30))).place(x=400,y=550)
    elif rc4>rc1 and rc4>rc2 and rc4>rc3:
        Label(rscreen1,text="!!! Candidate D is the Winner !!!",bg="black",fg="blue",font=('Times New Roman',(30))).place(x=400,y=550)
    else :
        Label(rscreen1,text="!!! It`s a Draw !!!",bg="black",fg="blue",font=('Times New Roman',30)).place(x=515,y=550)

def rvc():
    global rscreen2
    rscreen2=Toplevel(main)
    rscreen2.geometry("1366x768")
    rscreen2.configure(bg="black")
    rscreen2.title("Vice Captain")
    Label(rscreen2,image=bg3).place(x=0,y=0)
    Label(rscreen2,text="Votes secured by Candidate A - %s" % (rvc1),bg="black",fg="blue",font=("Times New Roman",(30))).place(x=400,y=50)
    Label(rscreen2,text="Votes secured by Candidate B - %s" % (rvc2),bg="black",fg="blue",font=("Times New Roman",(30))).place(x=400,y=120)
    Label(rscreen2,text="Votes secured by Candidate C - %s" % (rvc3),bg="black",fg="blue",font=("Times New Roman",(30))).place(x=400,y=190)
    Label(rscreen2,text="Votes secured by Candidate D - %s" % (rvc4),bg="black",fg="blue",font=("Times New Roman",(30))).place(x=400,y=260)
    Button(rscreen2,text="Winner",bg="black",fg="blue",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=rwin2).place(x=550,y=400)
    Button(rscreen2,text="Back",bg="black",fg="blue",height=1,width=5,bd=5,font=("Times New Roman",(15)),command=rback2).place(x=1200,y=600)
    
def rwin2():
    if rvc1>rvc2 and rvc1>rvc3 and rvc1>rvc4:
        Label(rscreen2,text="!!! Candidate A is the Winner !!!",bg="black",fg="blue",font=('Times New Roman',(30))).place(x=400,y=550)
    elif rvc2>rvc1 and rvc2>rvc3 and rvc2>rvc4:
        Label(rscreen2,text="!!! Candidate B is the Winner !!!",bg="black",fg="blue",font=('Times New Roman',(30))).place(x=400,y=550)
    elif rvc3>rvc1 and rvc3>rvc2 and rvc3>rvc4:
        Label(rscreen2,text="!!! Candidate C is the Winner !!!",bg="black",fg="blue",font=('Times New Roman',(30))).place(x=400,y=550)
    elif rvc4>rvc1 and rvc4>rvc2 and rvc4>rvc3:
        Label(rscreen2,text="!!! Candidate D is the Winner !!!",bg="black",fg="blue",font=('Times New Roman',(30))).place(x=400,y=550)
    else :
        Label(rscreen2,text="!!! It`s a Draw !!!",bg="black",fg="blue",font=('Times New Roman',30)).place(x=515,y=550)

def main_menu1():
    rscreen.destroy()

def rback1():
    rscreen1.destroy()

def rback2():
    rscreen2.destroy()

#-------------------------------------------Moeven-----------------------------------------------


def moeven_count():
    global mc1, mc2, mc3, mc4, mvc1, mvc2, mvc3, mvc4
    file = open("Moeven.txt", "r")
    read = file.read()
    read1 = read.split()
    mc1 = 0
    mc2 = 0
    mc3 = 0
    mc4 = 0
    mvc1 = 0
    mvc2 = 0
    mvc3 = 0
    mvc4 = 0
    for i in read1:
        if i == "mc1":
            mc1 += 1
        elif i == "mc2":
            mc2 += 1
        elif i == "mc3":
            mc3 += 1
        elif i == "mc4":
            mc4 += 1
        elif i == "mvc1":
            mvc1 += 1
        elif i == "mvc2":
            mvc2 += 1
        elif i == "mvc3":
            mvc3 += 1
        elif i == "mvc4":
            mvc4 += 1
    global mscreen
    mscreen=Toplevel(main)
    mscreen.geometry("1366x768")
    mscreen.configure(bg="black")
    mscreen.title("Moeven Counting")
    Label(mscreen,image=bg3).place(x=0,y=0)
    Label(mscreen, text="Moeven Vote Count",bg="black",fg="green2",font=("Algerian",(45))).pack(pady=30)
    Button(mscreen,text="Captain",bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=mc).place(x=400,y=275)
    Button(mscreen, text="Vice-Captain",bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=mvc).place(x=700,y=275)
    Button(mscreen,text="Back",bg="black",fg="green2",height=1,width=10,bd=6,font=('Times New Roman',15),command=main_menu2).place(x=1200,y=600)


def mc():
    global mscreen1
    mscreen1=Toplevel(main)
    mscreen1.geometry("1366x768")
    mscreen1.configure(bg="black")
    mscreen1.title("Captain")
    Label(mscreen1,image=bg3).place(x=0,y=0)
    Label(mscreen1,text="Votes secured by Candidate A - %s" % (mc1),bg="black",fg="green2",font=("Times New Roman",(30))).place(x=400,y=50)
    Label(mscreen1,text="Votes secured by Candidate B - %s" % (mc2),bg="black",fg="green2",font=("Times New Roman",(30))).place(x=400,y=120)
    Label(mscreen1,text="Votes secured by Candidate C - %s" % (mc3),bg="black",fg="green2",font=("Times New Roman",(30))).place(x=400,y=190)
    Label(mscreen1,text="Votes secured by Candidate D - %s" % (mc4),bg="black",fg="green2",font=("Times New Roman",(30))).place(x=400,y=260)
    Button(mscreen1,text="Winner",bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=mwin1).place(x=550,y=400)
    Button(mscreen1,text="Back",bg="black",fg="green2",height=1,width=5,bd=5,font=("Times New Roman",(15)),command=mback1).place(x=1200,y=600)
        
def mwin1():
    if mc1>mc2 and mc1>mc3 and mc1>mc4:
        Label(mscreen1,text="!!! Candidate A is the Winner !!!",bg="black",fg="green2",font=('Times New Roman',(30))).place(x=400,y=550)
    elif mc2>mc1 and mc2>mc3 and mc2>mc4:
        Label(mscreen1,text="!!! Candidate B is the Winner !!!",bg="black",fg="green2",font=('Times New Roman',(30))).place(x=400,y=550)
    elif mc3>mc1 and mc3>mc2 and mc3>mc4:
        Label(mscreen1,text="!!! Candidate C is the Winner !!!",bg="black",fg="green2",font=('Times New Roman',(30))).place(x=400,y=550)
    elif mc4>mc1 and mc4>mc2 and mc4>mc3:
        Label(mscreen1,text="!!! Candidate D is the Winner !!!",bg="black",fg="green2",font=('Times New Roman',(30))).place(x=400,y=550)
    else :
        Label(mscreen1,text="!!! It`s a Draw !!!",bg="black",fg="green2",font=('Times New Roman',30)).place(x=515,y=550)

def mvc():
    global mscreen2
    mscreen2=Toplevel(main)
    mscreen2.geometry("1366x768")
    mscreen2.configure(bg="black")
    mscreen2.title("Vice Captain")
    Label(mscreen2,image=bg3).place(x=0,y=0)
    Label(mscreen2,text="Votes secured by Candidate A - %s" % (mvc1),bg="black",fg="green2",font=("Times New Roman",(30))).place(x=400,y=50)
    Label(mscreen2,text="Votes secured by Candidate B - %s" % (mvc2),bg="black",fg="green2",font=("Times New Roman",(30))).place(x=400,y=120)
    Label(mscreen2,text="Votes secured by Candidate C - %s" % (mvc3),bg="black",fg="green2",font=("Times New Roman",(30))).place(x=400,y=190)
    Label(mscreen2,text="Votes secured by Candidate D - %s" % (mvc4),bg="black",fg="green2",font=("Times New Roman",(30))).place(x=400,y=260)
    Button(mscreen2,text="Winner",bg="black",fg="green2",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=mwin2).place(x=550,y=400)
    Button(mscreen2,text="Back",bg="black",fg="green2",height=1,width=5,bd=5,font=("Times New Roman",(15)),command=mback2).place(x=1200,y=600)
    
def mwin2():
    if mvc1>mvc2 and mvc1>mvc3 and mvc1>mvc4:
        Label(mscreen2,text="!!! Candidate A is the Winner !!!",bg="black",fg="green2",font=('Times New Roman',(30))).place(x=400,y=550)
    elif mvc2>mvc1 and mvc2>mvc3 and mvc2>mvc4:
        Label(mscreen2,text="!!! Candidate B is the Winner !!!",bg="black",fg="green2",font=('Times New Roman',(30))).place(x=400,y=550)
    elif mvc3>mvc1 and mvc3>mvc2 and mvc3>mvc4:
        Label(mscreen2,text="!!! Candidate C is the Winner !!!",bg="black",fg="green2",font=('Times New Roman',(30))).place(x=400,y=550)
    elif mvc4>mvc1 and mvc4>mvc2 and mvc4>mvc3:
        Label(mscreen2,text="!!! Candidate D is the Winner !!!",bg="black",fg="green2",font=('Times New Roman',(30))).place(x=400,y=550)
    else :
        Label(mscreen2,text="!!! It`s a Draw !!!",bg="black",fg="green2",font=('Times New Roman',30)).place(x=515,y=550)

def main_menu2():
    mscreen.destroy()
    
def mback1():
    mscreen1.destroy()

def mback2():
    mscreen2.destroy()

#------------------------------------------------Pelican---------------------------------------------------------

def pelican_count():
    global pscreen
    global pc1, pc2, pc3, pc4, pvc1, pvc2, pvc3, pvc4
    file = open("Pelican.txt", "r")
    read = file.read()
    read1 = read.split()
    pc1 = 0
    pc2 = 0
    pc3 = 0
    pc4 = 0
    pvc1 = 0
    pvc2 = 0
    pvc3 = 0
    pvc4 = 0
    for i in read1:
        if i == "pc1":
            pc1 += 1
        elif i == "pc2":
            pc2 += 1
        elif i == "pc3":
            pc3 += 1
        elif i == "pc4":
            pc4 += 1
        elif i == "pvc1":
            pvc1 += 1
        elif i == "pvc2":
            pvc2 += 1
        elif i == "pvc3":
            pvc3 += 1
        elif i == "pvc4":
            pvc4 += 1
    pscreen=Toplevel(main)
    pscreen.geometry("1366x768")
    pscreen.configure(bg="black")
    pscreen.title("Pelican Counting")
    Label(pscreen,image=bg3).place(x=0,y=0)
    Label(pscreen, text="Pelican Vote Count",bg="black",fg="yellow",font=("Algerian",(45))).pack(pady=30)
    Button(pscreen,text="Captain",bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=pc).place(x=400,y=275)
    Button(pscreen, text="Vice-Captain",bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=pvc).place(x=700,y=275)
    Button(pscreen,text="Back",bg="black",fg="yellow",height=1,width=10,bd=6,font=('Times New Roman',15),command=main_menu3).place(x=1200,y=600)


def pc():
    global pscreen1
    pscreen1=Toplevel(main)
    pscreen1.geometry("1366x768")
    pscreen1.configure(bg="black")
    pscreen1.title("Captain")
    Label(pscreen1,image=bg3).place(x=0,y=0)
    Label(pscreen1,text="Votes secured by Candidate A - %s" % (pc1),bg="black",fg="yellow",font=("Times New Roman",(30))).place(x=400,y=50)
    Label(pscreen1,text="Votes secured by Candidate B - %s" % (pc2),bg="black",fg="yellow",font=("Times New Roman",(30))).place(x=400,y=120)
    Label(pscreen1,text="Votes secured by Candidate C - %s" % (pc3),bg="black",fg="yellow",font=("Times New Roman",(30))).place(x=400,y=190)
    Label(pscreen1,text="Votes secured by Candidate D - %s" % (pc4),bg="black",fg="yellow",font=("Times New Roman",(30))).place(x=400,y=260)
    Button(pscreen1,text="Winner",bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=pwin1).place(x=550,y=400)
    Button(pscreen1,text="Back",bg="black",fg="yellow",height=1,width=5,bd=5,font=("Times New Roman",(15)),command=pback1).place(x=1200,y=600)
    
def pwin1():
    if pc1>pc2 and pc1>pc3 and pc1>pc4:
        Label(pscreen1,text="!!! Candidate A is the Winner !!!",bg="black",fg="yellow",font=('Times New Roman',(30))).place(x=400,y=550)
    elif pc2>pc1 and pc2>pc3 and pc2>pc4:
        Label(pscreen1,text="!!! Candidate B is the Winner !!!",bg="black",fg="yellow",font=('Times New Roman',(30))).place(x=400,y=550)
    elif pc3>pc1 and pc3>pc2 and pc3>pc4:
        Label(pscreen1,text="!!! Candidate C is the Winner !!!",bg="black",fg="yellow",font=('Times New Roman',(30))).place(x=400,y=550)
    elif pc4>pc1 and pc4>pc2 and pc4>pc3:
        Label(pscreen1,text="!!! Candidate D is the Winner !!!",bg="black",fg="yellow",font=('Times New Roman',(30))).place(x=400,y=550)
    else :
        Label(pscreen1,text="!!! It`s a Draw !!!",bg="black",fg="yellow",font=('Times New Roman',30)).place(x=515,y=550)
    
def pvc():
    global pscreen2
    pscreen2=Toplevel(main)
    pscreen2.geometry("1366x768")
    pscreen2.configure(bg="black")
    pscreen2.title("Vice Captain")
    Label(pscreen2,image=bg3).place(x=0,y=0)
    Label(pscreen2,text="Votes secured by Candidate A - %s" % (pvc1),bg="black",fg="yellow",font=("Times New Roman",(30))).place(x=400,y=50)
    Label(pscreen2,text="Votes secured by Candidate B - %s" % (pvc2),bg="black",fg="yellow",font=("Times New Roman",(30))).place(x=400,y=120)
    Label(pscreen2,text="Votes secured by Candidate C - %s" % (pvc3),bg="black",fg="yellow",font=("Times New Roman",(30))).place(x=400,y=190)
    Label(pscreen2,text="Votes secured by Candidate D - %s" % (pvc4),bg="black",fg="yellow",font=("Times New Roman",(30))).place(x=400,y=260)
    Button(pscreen2,text="Winner",bg="black",fg="yellow",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=pwin2).place(x=550,y=400)
    Button(pscreen2,text="Back",bg="black",fg="yellow",height=1,width=5,bd=5,font=("Times New Roman",(15)),command=pback2).place(x=1200,y=600)    

def pwin2():
    if pvc1>pvc2 and pvc1>pvc3 and pvc1>pvc4:
        Label(pscreen2,text="!!! Candidate A is the Winner !!!",bg="black",fg="yellow",font=('Times New Roman',(30))).place(x=400,y=550)
    elif pvc2>pvc1 and pvc2>pvc3 and pvc2>pvc4:
        Label(pscreen2,text="!!! Candidate B is the Winner !!!",bg="black",fg="yellow",font=('Times New Roman',(30))).place(x=400,y=550)
    elif pvc3>pvc1 and pvc3>pvc2 and pvc3>pvc4:
        Label(pscreen2,text="!!! Candidate C is the Winner !!!",bg="black",fg="yellow",font=('Times New Roman',(30))).place(x=400,y=550)
    elif pvc4>pvc1 and pvc4>pvc2 and pvc4>pvc3:
        Label(pscreen2,text="!!! Candidate D is the Winner !!!",bg="black",fg="yellow",font=('Times New Roman',(30))).place(x=400,y=550)
    else :
        Label(pscreen2,text="!!! It`s a Draw !!!",bg="black",fg="yellow",font=('Times New Roman',30)).place(x=515,y=550)

def main_menu3():
    pscreen.destroy()

def pback1():
    pscreen1.destroy()

def pback2():
    pscreen2.destroy()

#------------------------------------------Falcon--------------------------------------------------

def falcon_count():
    global fc1, fc2, fc3, fc4, fvc1, fvc2, fvc3, fvc4
    file = open("Falcon.txt", "r")
    read = file.read()
    read1 = read.split()
    fc1 = 0
    fc2 = 0
    fc3 = 0
    fc4 = 0
    fvc1 = 0
    fvc2 = 0
    fvc3 = 0
    fvc4 = 0
    for i in read1:
        if i == "fc1":
            fc1 += 1
        elif i == "fc2":
            fc2 += 1
        elif i == "fc3":
            fc3 += 1
        elif i == "fc4":
            fc4 += 1
        elif i == "fvc1":
            fvc1 += 1
        elif i == "fvc2":
            fvc2 += 1
        elif i == "fvc3":
            fvc3 += 1
        elif i == "fvc4":
            fvc4 += 1
    global fscreen
    fscreen=Toplevel(main)
    fscreen.geometry("1366x768")
    fscreen.configure(bg="black")
    fscreen.title("Falcon Counting")
    Label(fscreen,image=bg3).place(x=0,y=0)
    Label(fscreen, text="Falcon Vote Count",bg="black",fg="orange",font=("Algerian",(45))).pack(pady=30)
    Button(fscreen,text="Captain",bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=fc).place(x=400,y=275)
    Button(fscreen, text="Vice-Captain",bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=fvc).place(x=700,y=275)
    Button(fscreen,text="Back",bg="black",fg="orange",height=1,width=10,bd=6,font=('Times New Roman',15),command=main_menu4).place(x=1200,y=600)

def fc():
    global fscreen1
    fscreen1=Toplevel(main)
    fscreen1.geometry("1366x768")
    fscreen1.configure(bg="black")
    fscreen1.title("Captain")
    Label(fscreen1,image=bg3).place(x=0,y=0)
    Label(fscreen1,text="Votes secured by Candidate A - %s" % (fc1),bg="black",fg="orange",font=("Times New Roman",(30))).place(x=400,y=50)
    Label(fscreen1,text="Votes secured by Candidate B - %s" % (fc2),bg="black",fg="orange",font=("Times New Roman",(30))).place(x=400,y=120)
    Label(fscreen1,text="Votes secured by Candidate C - %s" % (fc3),bg="black",fg="orange",font=("Times New Roman",(30))).place(x=400,y=190)
    Label(fscreen1,text="Votes secured by Candidate D - %s" % (fc4),bg="black",fg="orange",font=("Times New Roman",(30))).place(x=400,y=260)
    Button(fscreen1,text="Winner",bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=fwin1).place(x=550,y=400)
    Button(fscreen1,text="Back",bg="black",fg="orange",height=1,width=5,bd=5,font=("Times New Roman",(15)),command=fback1).place(x=1200,y=600)
    
def fwin1():
    if fc1>fc2 and fc1>fc3 and fc1>fc4:
        Label(fscreen1,text="!!! Candidate A is the Winner !!!",bg="black",fg="orange",font=('Times New Roman',(30))).place(x=400,y=550)
    elif fc2>fc1 and fc2>fc3 and fc2>fc4:
        Label(fscreen1,text="!!! Candidate B is the Winner !!!",bg="black",fg="orange",font=('Times New Roman',(30))).place(x=400,y=550)
    elif fc3>fc1 and fc3>fc2 and fc3>fc4:
        Label(fscreen1,text="!!! Candidate C is the Winner !!!",bg="black",fg="orange",font=('Times New Roman',(30))).place(x=400,y=550)
    elif fc4>fc1 and fc4>fc2 and fc4>fc3:
        Label(fscreen1,text="!!! Candidate D is the Winner !!!",bg="black",fg="orange",font=('Times New Roman',(30))).place(x=400,y=550)
    else :
        Label(fscreen1,text="!!! It`s a Draw !!!",bg="black",fg="orange",font=('Times New Roman',30)).place(x=515,y=550)
    
def fvc():
    global fscreen2
    fscreen2=Toplevel(main)
    fscreen2.geometry("1366x768")
    fscreen2.configure(bg="black")
    fscreen2.title("Vice Captain")
    Label(fscreen2,image=bg3).place(x=0,y=0)
    Label(fscreen2,text="Votes secured by Candidate A - %s" % (fvc1),bg="black",fg="orange",font=("Times New Roman",(30))).place(x=400,y=50)
    Label(fscreen2,text="Votes secured by Candidate B - %s" % (fvc2),bg="black",fg="orange",font=("Times New Roman",(30))).place(x=400,y=120)
    Label(fscreen2,text="Votes secured by Candidate C - %s" % (fvc3),bg="black",fg="orange",font=("Times New Roman",(30))).place(x=400,y=190)
    Label(fscreen2,text="Votes secured by Candidate D - %s" % (fvc4),bg="black",fg="orange",font=("Times New Roman",(30))).place(x=400,y=260)
    Button(fscreen2,text="Winner",bg="black",fg="orange",height=2,width=10,bd=10,font=("Times New Roman",(25)),command=fwin2).place(x=550,y=400)
    Button(fscreen2,text="Back",bg="black",fg="orange",height=1,width=5,bd=5,font=("Times New Roman",(15)),command=fback2).place(x=1200,y=600)    

def fwin2():
    if fvc1>fvc2 and fvc1>fvc3 and fvc1>fvc4:
        Label(fscreen2,text="!!! Candidate A is the Winner !!!",bg="black",fg="orange",font=('Times New Roman',(30))).place(x=400,y=550)
    elif fvc2>fvc1 and fvc2>fvc3 and fvc2>fvc4:
        Label(fscreen2,text="!!! Candidate B is the Winner !!!",bg="black",fg="orange",font=('Times New Roman',(30))).place(x=400,y=550)
    elif fvc3>fvc1 and fvc3>fvc2 and fvc3>fvc4:
        Label(fscreen2,text="!!! Candidate C is the Winner !!!",bg="black",fg="orange",font=('Times New Roman',(30))).place(x=400,y=550)
    elif fvc4>fvc1 and fvc4>fvc2 and fvc4>fvc3:
        Label(fscreen2,text="!!! Candidate D is the Winner !!!",bg="black",fg="orange",font=('Times New Roman',(30))).place(x=400,y=550)
    else :
        Label(fscreen2,text="!!! It`s a Draw !!!",bg="black",fg="orange",font=('Times New Roman',30)).place(x=515,y=550)

def main_menu4():
    fscreen.destroy()

def fback1():
    fscreen1.destroy()

def fback2():
    fscreen2.destroy()

main()

