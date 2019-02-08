from tkinter import *
from tkinter import ttk
import math

def calculate(*args):
    try:
        value_fsr = float(fsr_entry.get())
        val_accr = float(accr_entry.get())
        val_resol = float(resol_entry.get())
        val_zerr = float(zerror_entry.get())
        val_ninp = float(noinp_entry.get())
        val_inp1 = float(inp_1_entry.get())
        val_inp2 = float(inp_2_entry.get())
        val_inp3 = float(inp_3_entry.get())
        val_inp4 = float(inp_4_entry.get())
        val_inp5 = float(inp_5_entry.get())
        val_inp6 = float(inp_6_entry.get())
        val_inp7 = float(inp_7_entry.get())
        val_inp8 = float(inp_8_entry.get())
        val_inp9 = float(inp_9_entry.get())
        val_inp10 = float(inp_10_entry.get())
        decidig=int(abs(math.floor(math.log10(abs(val_resol)))))
        err1 = (val_accr / 100) * value_fsr
        err2 = val_resol / 2
        alii = [val_inp1, val_inp2, val_inp3, val_inp4, val_inp5, val_inp6, val_inp7, val_inp8, val_inp9, val_inp10]
        summ = 0
        for ii in range(int(val_ninp)):
        	summ = summ + alii[ii]
        mymean = summ / val_ninp
        summ = 0
        for ii in range(int(val_ninp)):
        	ee = (mymean - alii[ii])*(mymean - alii[ii])
        	summ = summ + ee
        varr = math.sqrt(summ/(val_ninp-1))
        err3 = varr / math.sqrt(varr)
        su1 = (err1)/2
        su2 = err2 / math.sqrt(3)
        su3=err3
        su=math.sqrt((su1*su1)+(su2*su2)+(su3*su3)) 
        esu=su*2
        esu=round(esu,decidig)
        fimea=mymean-val_zerr
        fimea=round(fimea,decidig);
        resul.set(fimea)
        unci.set(esu)
    except ValueError:
        pass
    
root = Tk()
root.title("Uncertainty Measurement")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

resul = StringVar()
unci = StringVar()
fsr = StringVar()
accr = StringVar()
resol = StringVar()
zerror = StringVar()
noinp = StringVar()
numinps = StringVar()
inp_1 = StringVar()
inp_2= StringVar()
inp_3 = StringVar()
inp_4 = StringVar()
inp_5 = StringVar()
inp_6 = StringVar()
inp_7 = StringVar()
inp_8 = StringVar()
inp_9 = StringVar()
inp_10 = StringVar()

fsr_entry = ttk.Entry(mainframe, width=7, textvariable=fsr)
fsr_entry.grid(column=2, row=2, sticky=(W,E))
fsr_entry.insert(0,"0")

accr_entry = ttk.Entry(mainframe, width=7, textvariable=accr)
accr_entry.grid(column=2, row=3, sticky=(W,E))
accr_entry.insert(0,"0")

resol_entry = ttk.Entry(mainframe, width=7, textvariable=resol)
resol_entry.grid(column=2, row=4, sticky=(W,E))
resol_entry.insert(0,"0")

zerror_entry = ttk.Entry(mainframe, width=7, textvariable=zerror)
zerror_entry.grid(column=2, row=5, sticky=(W,E))
zerror_entry.insert(0,"0")

noinp_entry = ttk.Entry(mainframe, width=7, textvariable=noinp)
noinp_entry.grid(column=2, row=6, sticky=(W,E))
noinp_entry.insert(0,"0")

inp_1_entry = ttk.Entry(mainframe, width=7, textvariable=inp_1)
inp_1_entry.grid(column=2, row=7, sticky=(W,E))
inp_1_entry.insert(0,"0")

inp_2_entry = ttk.Entry(mainframe, width=7, textvariable=inp_2)
inp_2_entry.grid(column=2, row=8, sticky=(W,E))
inp_2_entry.insert(0,"0")

inp_3_entry = ttk.Entry(mainframe, width=7, textvariable=inp_3)
inp_3_entry.grid(column=2, row=9, sticky=(W,E))
inp_3_entry.insert(0,"0")

inp_4_entry = ttk.Entry(mainframe, width=7, textvariable=inp_4)
inp_4_entry.grid(column=2, row=10, sticky=(W,E))
inp_4_entry.insert(0,"0")

inp_5_entry = ttk.Entry(mainframe, width=7, textvariable=inp_5)
inp_5_entry.grid(column=2, row=11, sticky=(W,E))
inp_5_entry.insert(0,"0")

inp_6_entry = ttk.Entry(mainframe, width=7, textvariable=inp_6)
inp_6_entry.grid(column=2, row=12, sticky=(W,E))
inp_6_entry.insert(0,"0")

inp_7_entry = ttk.Entry(mainframe, width=7, textvariable=inp_7)
inp_7_entry.grid(column=2, row=13, sticky=(W,E))
inp_7_entry.insert(0,"0")

inp_8_entry = ttk.Entry(mainframe, width=7, textvariable=inp_8)
inp_8_entry.grid(column=2, row=14, sticky=(W,E))
inp_8_entry.insert(0,"0")

inp_9_entry = ttk.Entry(mainframe, width=7, textvariable=inp_9)
inp_9_entry.grid(column=2, row=15, sticky=(W,E))
inp_9_entry.insert(0,"0")

inp_10_entry = ttk.Entry(mainframe, width=7, textvariable=inp_10)
inp_10_entry.grid(column=2, row=16, sticky=(W,E))
inp_10_entry.insert(0,"0")

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=17, sticky=W)

ttk.Label(mainframe, text="Full Scale Reading").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Accuracy").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Resolution").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="Zero Error").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text="Number of Inputs").grid(column=1, row=6, sticky=W)
ttk.Label(mainframe, text="Input 1").grid(column=1, row=7, sticky=W)
ttk.Label(mainframe, text="Input 2").grid(column=1, row=8, sticky=W)
ttk.Label(mainframe, text="Input 3").grid(column=1, row=9, sticky=W)
ttk.Label(mainframe, text="Input 4").grid(column=1, row=10, sticky=W)
ttk.Label(mainframe, text="Input 5").grid(column=1, row=11, sticky=W)
ttk.Label(mainframe, text="Input 6").grid(column=1, row=12, sticky=W)
ttk.Label(mainframe, text="Input 7").grid(column=1, row=13, sticky=W)
ttk.Label(mainframe, text="Input 8").grid(column=1, row=14, sticky=W)
ttk.Label(mainframe, text="Input 9").grid(column=1, row=15, sticky=W)
ttk.Label(mainframe, text="Input 10").grid(column=1, row=16, sticky=W)
ttk.Label(mainframe, text="Result is").grid(column=1, row=(18), sticky=E)
ttk.Label(mainframe, textvariable=resul).grid(column=2,row=18, sticky=(W,E))
ttk.Label(mainframe, text="units").grid(column=3, row=(18), sticky=W)
ttk.Label(mainframe, text= u"\u00B1").grid(column=1, row=19, sticky=E)
ttk.Label(mainframe, textvariable=unci).grid(column=2, row=19, sticky=(W,E))
ttk.Label(mainframe, text="with approximately").grid(column=1,row=20,sticky=E)
ttk.Label(mainframe, text="95 percent Level").grid(column=2,row=20,sticky=(W,E))
ttk.Label(mainframe, text="of Confidence").grid(column=3,row=20,sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

fsr_entry.focus()
accr_entry.focus()
resol_entry.focus()
zerror_entry.focus()
noinp_entry.focus()
inp_1_entry.focus()
inp_2_entry.focus()
inp_3_entry.focus()
inp_4_entry.focus()
inp_5_entry.focus()
inp_6_entry.focus()
inp_7_entry.focus()
inp_8_entry.focus()
inp_9_entry.focus()
inp_10_entry.focus()

root.bind('<Return>', calculate)

root.mainloop()
