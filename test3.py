class wordFreq(object):
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

filenames=['C:\Users\Public\Documents\Transcript Stats\Unique Words Abby 1.txt',
           'C:\Users\Public\Documents\Transcript Stats\Unique Words Holly 1.txt',
           'C:\Users\Public\Documents\Transcript Stats\Unique Words Holly 2.txt',
           'C:\Users\Public\Documents\Transcript Stats\Unique Words Holly 3.txt',
           'C:\Users\Public\Documents\Transcript Stats\Unique Words Melissa 1.txt']
temp =[]
words=[]
balls = []
startIndex = 0
for i in range(5):
    myfile = open(filenames[i], 'r')
    print 'FILE: ', filenames[i]

    for line in myfile:
        line = line.strip()
        temp.append(line)
            
    if startIndex == 0:
        print 'first run!!'
        for i in range(len(temp)):
            if(i % 2 == 0 and i > 1 and i <= (len(temp) - 10)):
                tmp = wordFreq(temp[i], temp[i+1])
                words.append(tmp)
                startIndex += len(words)
        words.sort()
        
    else:
        for i in range(len(temp)):
            if(i % 2 == 0 and i > 1 and i <= (len(temp) - 10)):
                tmp = wordFreq(temp[i], temp[i+1])
                balls.append(tmp)
                startIndex += len(balls)
        balls.sort
        temp = []                         
        for i in range(len(balls)):
            
                
                
        
        


        
        
        
