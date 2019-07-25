# author: Santiago Nunez-Corrales
# date: 6-10-2019
# purpose: create an interface for the lipid calculator

import tkinter as tk
from porrasg2.lipids.calculations.volumes import LipidCalculator

class VolumeGUI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.master.title("Lipid solution volume calculator")

        self.master.geometry("300x400")
        self.cflabel = tk.Label(self, text='Final concentration (mM):')
        self.cflabel.grid(row=0, column=0)
        self.cfinput = tk.Entry(self, justify=tk.RIGHT, width=10)
        self.cfinput.grid(row=0, column=1)
        self.vflabel = tk.Label(self, text='Final volume (uL): ')
        self.vflabel.grid(row=1, column=0)
        self.vfinput = tk.Entry(self, justify=tk.RIGHT, width=10)
        self.vfinput.grid(row=1, column=1)
        self.dopcplabel = tk.Label(self, text='DOPC percentage:')
        self.dopcplabel.grid(row=2, column=0)
        self.dopcpinput = tk.Entry(self, justify=tk.RIGHT, width=10)
        self.dopcpinput.grid(row=2, column=1)
        self.dopgplabel = tk.Label(self, text='DOPG percentage: ')
        self.dopgplabel.grid(row=3, column=0)
        self.dopgpinput = tk.Entry(self, justify=tk.RIGHT, width=10)
        self.dopgpinput.grid(row=3, column=1)

        self.dopcslabel = tk.Label(self, text='DOPC stock conc.:')
        self.dopcslabel.grid(row=5, column=0)
        self.dopcsinput = tk.Entry(self, justify=tk.RIGHT, width=10, state=tk.NORMAL)
        self.dopcsinput.grid(row=5, column=1)
        self.dopcsinput.insert(0, '25')
        self.dopgslabel = tk.Label(self, text='DOPG stock conc.: ')
        self.dopgslabel.grid(row=6, column=0)
        self.dopgsinput = tk.Entry(self, justify=tk.RIGHT, width=10, state=tk.NORMAL)
        self.dopgsinput.grid(row=6, column=1)
        self.dopgsinput.insert(0, '25')

        self.calculate = tk.Button(self, text="Calculate", width=10, command=self.calculateVolume, default=tk.NORMAL)
        self.calculate.grid(row=7, column=0)

        self.dopcrlabel = tk.Label(self, text='DOPC volume:')
        self.dopcrlabel.grid(row=8, column=0)
        self.dopcrinput = tk.Entry(self, justify=tk.RIGHT, width=10, state=tk.NORMAL)
        self.dopcrinput.grid(row=8, column=1)
        self.dopgrlabel = tk.Label(self, text='DOPG volume: ')
        self.dopgrlabel.grid(row=9, column=0)
        self.dopgrinput = tk.Entry(self, justify=tk.RIGHT, width=10, state=tk.NORMAL)
        self.dopgrinput.grid(row=9, column=1)

    def setStockHandler(self):
        if self.stockset.get():
            self.dopcsinput.configure(state=tk.NORMAL)
            self.dopgsinput.configure(state=tk.NORMAL)
        else:
            self.dopcsinput.configure(state=tk.NORMAL)
            self.dopgsinput.configure(state=tk.NORMAL)

    def calculateVolume(self):
        cf = float(self.cfinput.get())
        vf = float(self.vfinput.get())
        dopcp = float(self.dopcpinput.get())
        dopgp = float(self.dopgpinput.get())

        calculator = LipidCalculator()
        dopcv, dopgv = calculator.calculate_volume(cf, vf, dopcp, dopgp)
        self.dopcrinput.delete(0, 'end')
        self.dopcrinput.insert(0, "%.2f" % dopcv)
        self.dopgrinput.delete(0, 'end')
        self.dopgrinput.insert(0, "%.2f" % dopgv)


if __name__ == "__main__":
    app = VolumeGUI()
    app.mainloop()

