from PhysicalConstants import *

class BandSelection:
    def __init__(self):
        pass
    
    def getBandwidthO(self):
        result = c * ((1/LO) - (1/LE))
        return(result)

    def getBandwidthE(self):
        result = c * ((1/LE) - (1/LS))
        return(result)

    def getBandwidthS(self):
        result = c * ((1/LS) - (1/LC))
        return(result)

    def getBandwidthC(self):
        result = c * ((1/LC) - (1/LL))
        return(result)

    def getBandwidthL(self):
        result = c * ((1/LL) - (1/LU))
        return(result)