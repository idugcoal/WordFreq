filenames=['C:\Users\Public\Documents\Transcript Stats\Unique Words Abby 1.txt',
           'C:\Users\Public\Documents\Transcript Stats\Unique Words Holly 1.txt',
           'C:\Users\Public\Documents\Transcript Stats\Unique Words Holly 2.txt',
           'C:\Users\Public\Documents\Transcript Stats\Unique Words Holly 3.txt',
           'C:\Users\Public\Documents\Transcript Stats\Unique Words Melissa 1.txt']
lines =[0,0]

startIndex = 0
for i in range(5):
    print 'FILE: ', filenames[i]
    temp = [line.strip() for line in open(filenames[i])]
    #print temp
    print 'TEMP LENGTH:', len(temp)
    
    if startIndex == 0:
        full = list(temp)
        startIndex = len(full)
        
        print 'first run!!'
        print 'masterList LENGTH: ', len(full)

    f = 2
    t = 2
    print temp[t]
    print full[f]

    #PROBLEM: THESE WORK OUT TO BE THE SAME NUMBER RIGHT NOW!
  
    firstTempWord = startIndex + 2
    firstListWord = startIndex + 2
    lastTempWord = (len(temp) - 11)
    lastListWord = (len(full) - 11)

    print 'STUFF:', firstTempWord, firstListWord, lastTempWord, lastListWord
    
    print lastTempWord, temp[lastTempWord]
    print lastListWord, full[lastListWord]

    while f <= lastListWord:
        while t <= lastTempWord:
            print temp[t]
            print full[f]
            if temp[t] == full[f]:
                full[f+1] = temp[t+1]
                t+=2
            f+=2
    full.append(temp[t])
    full.append(temp[t+1])
    startIndex = len(full)
    
   
