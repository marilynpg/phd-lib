# author: Marilyn Porras-Gomez
# date: 6-10-2019
# purpose: obtain volumes in uL for a lipid solution using film hydration


class LipidCalculator:
    mwDOPC = 786.113
    mwDOPG = 775.058
    toMolar = 1.0e-3

    def __init__(self, stockdopc=25, stockdopg=25):
        self.stockdopc = stockdopc
        self.stockdopg = stockdopg

    def calculate_volume(self, cf, vf, dopc_perc, dopg_perc):
        cfM = cf * self.toMolar
        totalmol = cfM * vf
        dopcmol = totalmol * (dopc_perc / 100)
        dopgmol = totalmol * (dopg_perc / 100)
        dopcmass = dopcmol * self.mwDOPC
        dopgmass = dopgmol * self.mwDOPG
        dopcvolinuL = dopcmass / self.stockdopc
        dopgvolinuL = dopgmass / self.stockdopg

        print(f'DOPC volume: {dopcvolinuL} uL\tDOPG volume: {dopgvolinuL} uL')
        return (dopcvolinuL, dopgvolinuL)

