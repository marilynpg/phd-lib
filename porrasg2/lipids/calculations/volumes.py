# author: Marilyn Porras-Gomez
# date: 6-10-2019
# purpose: obtain volumes in uL for a lipid solution using film hydration


class LipidCalculator:
    mwDOPC = 786.113
    mwDOPG = 775.058
    mwDPPC = 734.039
    mwCL = 1494.319
    toMolar = 1.0e-3

    def __init__(self, stockdopc=25, stockdopg=25, stockdppc=25, stockCL=25):
        self.stockdopc = stockdopc
        self.stockdopg = stockdopg
        self.stockdppc = stockdppc
        self.stockCL = stockCL

    def calculate_volume(self, cf, vf, dopc_perc, dopg_perc, dppc_perc, CL_perc):
        cfM = cf * self.toMolar
        totalmol = cfM * vf
        dopcmol = totalmol * (dopc_perc / 100)
        dopgmol = totalmol * (dopg_perc / 100)
        dopcmass = dopcmol * self.mwDOPC
        dopgmass = dopgmol * self.mwDOPG
        dopcvolinuL = dopcmass / self.stockdopc
        dopgvolinuL = dopgmass / self.stockdopg
        dppcmol = totalmol * (dppc_perc / 100)
        CLmol = totalmol * (CL_perc / 100)
        dppcmass = dppcmol * self.mwDPPC
        CLmass = CLmol * self.mwCL
        dppcvolinuL = dppcmass / self.stockdppc
        CLvolinuL = CLmass / self.stockCL

        print(f'DOPC volume: {dopcvolinuL} uL\tDOPG volume: {dopgvolinuL} uL\tDPPC volume: {dppcvolinuL} ul\tCL volume: {CLvolinuL}')
        return (dopcvolinuL, dopgvolinuL, dppcvolinuL, CLvolinuL)

