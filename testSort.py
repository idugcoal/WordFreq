filenames=['C:\Users\Public\Documents\Transcript Stats\Unique Words Abby 1.txt',
           'C:\Users\Public\Documents\Transcript Stats\Unique Words Holly 1.txt',
           'C:\Users\Public\Documents\Transcript Stats\Unique Words Holly 2.txt',
           'C:\Users\Public\Documents\Transcript Stats\Unique Words Holly 3.txt',
           'C:\Users\Public\Documents\Transcript Stats\Unique Words Melissa 1.txt']
filename = open(filenames[0], 'r')

tmp = []
temp = []
words = []
file1 = []
file2 = []
file3 = []
file4 = []
file5 = []
for line in filename:
    line = line.strip()
    temp.append(line)

for i in range(len(temp)):
    if(i % 2 == 0 and i > 1 and i <= (len(temp) - 10)):
        tmp = (temp[i], temp[i+1])
        words.append(tmp)

sorted(words, key=lambda words: words[0])


    
        
    
