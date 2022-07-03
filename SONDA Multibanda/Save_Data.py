
class Save:
    def __init__(self):
        pass
    
    def Modulation_Begin(self, file):
        with open(file,'a') as text:
                text.write('[')
    
    def Modulation(self, file, M):
        with open(file,'a') as text:
                text.write(str(M) + ',\n')
                
                
    def Modulation_End(self, file):
        with open(file,'a') as text:
                text.write(']\n')