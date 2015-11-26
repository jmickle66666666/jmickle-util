import sys, time

class progress:
    def __init__(self,max):
        self.start(max)
        
    def start(self,max):
        self.prg = 0
        self.max = max
        self.starttime = time.time()
        
    def update(self):
        self.prg += 1
        update_progress(self.prg/self.max)
        
    def end(self):
        print "time elapsed: {}".format(time.time()-self.starttime)
        
def update_progress(progress):
    barLength = 10 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()