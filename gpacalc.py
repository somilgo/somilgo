__author__ = 'Govani'
try:
    from tkinter import *
except:
    from Tkinter import *
gpa = Tk()

gpa.configure(background="#BFD4FF")
gpa.geometry("525x400+450+100")
gpa.title("Somil\'s GPA Calculator")

gpa.columnconfigure(1, minsize=100)
gpa.columnconfigure(0, minsize=140)





def calculate():

    print(2)


    if grade1.get() == "Grade" or grade2.get() == "Grade" or grade3.get() == "Grade" or grade4.get() == "Grade" or acadw.get() == "Academic" or honw.get() == "Honors" or apw.get() == "AP":
        result.set("Enter All Fields")


    else:


        tapioca = float(grades[grade1.get()] + grades[grade2.get()] + grades[grade3.get()] + grades[grade4.get()])
        swagger = float(tapioca + float(rig1.get()) + float(rig2.get()) + float(rig3.get()) + float(rig4.get()))

        result.set(round(swagger / 4, 5))


result = StringVar()
pirate = Label(gpa, textvariable=result, font="Arial", bg="#BFD4FF")
pirate.grid(row=10, column=0, padx=10, pady=10, stick=W)



#Heading
heading = Label(gpa, text="Somil's GPA Calculator", font="Arial, 20", pady = 10, bg ="#BFD4FF" )
heading.grid(padx=120, row=0, column=0, columnspan=70)



#Block Titles
block1 = Label(gpa, text="Block 1 Class", bg="#BFD4FF", font="Arial, 14").grid(sticky=W, row=1, column=0, pady=10, padx=5)
block2 = Label(gpa, text="Block 2 Class", bg="#BFD4FF", font="Arial, 14").grid(sticky=W, row=2, column=0, pady=10, padx=5)
block3 = Label(gpa, text="Block 3 Class", bg="#BFD4FF", font="Arial, 14").grid(sticky=W, row=3, column=0, pady=10, padx=5)
block4 = Label(gpa, text="Block 4 Class", bg="#BFD4FF", font="Arial, 14").grid(sticky=W, row=4, column=0, pady=10, padx=5)

#Grade Variables
grade1 = StringVar(gpa)
grade2 = StringVar(gpa)
grade3 = StringVar(gpa)
grade4 = StringVar(gpa)
apw = StringVar(gpa)
honw = StringVar(gpa)
acadw = StringVar(gpa)


#Rigor Variables

riga = IntVar()
rigb = IntVar()
rigc = IntVar()
rigd = IntVar()
rig1 = StringVar()
rig2 = StringVar()
rig3 = StringVar()
rig4 = StringVar()


#Grade drop-downs
grades = {"A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7,
          "D+": 1.3, "D": 1.0, "D-": 0.7, "F": 0.0}
gradesx = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]

grade1.set("Grade")
grade2.set("Grade")
grade3.set("Grade")
grade4.set("Grade")

block1_grd = OptionMenu(gpa, grade1, *gradesx).grid(sticky=W, row=1, column=1, padx=10)
block2_grd = OptionMenu(gpa, grade2, *gradesx).grid(sticky=W, row=2, column=1, padx=10)
block3_grd = OptionMenu(gpa, grade3, *gradesx).grid(sticky=W, row=3, column=1, padx=10)
block4_grd = OptionMenu(gpa, grade4, *gradesx).grid(sticky=W, row=4, column=1, padx=10)

#Set Class Weights
academic = Label(gpa, text="Academic", bg="#BFD4FF", font="Arial, 10").grid(sticky=W, row=6, column=1, pady=10, padx=5)
honors = Label(gpa, text="Honors", bg="#BFD4FF", font="Arial, 10").grid(sticky=W, row=6, column=2, pady=10, padx=5)
apl = Label(gpa, text="AP", bg="#BFD4FF", font="Arial, 10").grid(sticky=W, row=6, column=3, pady=10, padx=5)
weights = Label(gpa, text="Weights", bg="#BFD4FF", font="Arial 10 bold").grid(sticky=W, row=6, column=0, pady=10, padx=5)



acadw.set(0.00)
honw.set(0.25)
apw.set(1.00)

acad = Spinbox(gpa, from_=0, to=10, textvariable=acadw, format='%.2f', increment=.25, width = 5).grid(sticky=W, row=7, column=1, padx=10)
honors = Spinbox(gpa, from_=0, to=10, textvariable=honw, format='%.2f', increment=.25, width = 5).grid(sticky=W, row=7, column=2, padx=10)
ap = Spinbox(gpa, from_=0, to=10, textvariable=apw, format='%.2f', increment=.25, width = 5).grid(sticky=W, row=7, column=3, padx=10)

def rigs():
    print(riga.get())
    bill = [riga.get(), rigb.get(), rigc.get(), rigd.get()]
    till = [rig1, rig2, rig3, rig4]
    for i,f in zip(bill,till):

        if i == 0:
            f.set(acadw.get())
        elif i == 1:
            f.set(honw.get())
        elif i == 2:
            f.set(apw.get())


#Calculate Button
def button():
    rigs()
    calculate()

riga.set(0)
Radiobutton(gpa, text="Academic", variable=riga, value=0).grid(row=1, column=2, padx=5)
Radiobutton(gpa, text="Honors", variable=riga, value=1).grid(row=1, column=3, padx=5)
Radiobutton(gpa, text="AP", variable=riga, value=2).grid(row=1, column=4, padx=5)

rigb.set(0)
Radiobutton(gpa, text="Academic", variable=rigb, value=0).grid(row=2, column=2, padx=5)
Radiobutton(gpa, text="Honors", variable=rigb, value=1).grid(row=2, column=3, padx=5)
Radiobutton(gpa, text="AP", variable=rigb, value=2).grid(row=2, column=4, padx=5)

rigc.set(0)
Radiobutton(gpa, text="Academic", variable=rigc, value=0).grid(row=3, column=2, padx=5)
Radiobutton(gpa, text="Honors", variable=rigc, value=1).grid(row=3, column=3, padx=5)
Radiobutton(gpa, text="AP", variable=rigc, value=2).grid(row=3, column=4, padx=5)

rigd.set(0)
Radiobutton(gpa, text="Academic", variable=rigd, value=0).grid(row=4, column=2, padx=5)
Radiobutton(gpa, text="Honors", variable=rigd, value=1).grid(row=4, column=3, padx=5)
Radiobutton(gpa, text="AP", variable=rigd, value=2).grid(row=4, column=4, padx=5)


calcbutt = Button(text='Calculate!', command=button).grid(row=8, column=0, sticky=W, padx = 10)



mainloop()
