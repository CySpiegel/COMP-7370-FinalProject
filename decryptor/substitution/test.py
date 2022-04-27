#!/usr/bin/python
import os
from betterSubCrack import BetterSubCraker
pre = './gutenberg/'
out = './results/'
res = ''
i = 0
average = []
check = True
if  check:
    for f in os.listdir(pre):  
        if f != '':
            # open orginal book
            book = open(pre+f,'r').read().replace('\n','').replace(' ','')
            # get encrypted book
            encrypted = './gutenberg_encrypted/'+f
            output = './results/'+f

            # create a results folder with file that will be parsed
            os.system(' touch ./results/{}'.format(f))
            
            # creat a decrypt an object for decrypting
            solver = BetterSubCraker(encrypted, output)

            # solve problem
            res = solver.solve()
            
            # count mistakes
            count = 0
            res = res.replace('\n','').replace(' ','')
            for i in range(len(book)):
                if book[i] == res[i]:
                    count += 1
            # take the average of mistakes
            av = int(count/len(book) * 100)
            print(f, '\t\t\t',av, '----')

            # append all averages to get a cumulative av
            average.append(int(count/len(book) * 100))

            # save file
            solver.save()
        
    sum = 0
    for av in average:
        sum += av

    print('TOTAL AV: ', sum/len(average))
else:

    # for on off instances
    f = './gutenberg_encrypted/2542.txt.utf-8.1'
    
    print(f)
    book = open(f,'r').read()
    solver = BetterSubCraker(f, out+'2542.txt.utf-8.1')
    res = solver.solve()
    # print(res)
    count = 0
    for i in range(len(book)):
        if book[i] == res[i]:
            count += 1
    average.append(int(count/len(book) * 100))
    print(int(count/len(book) * 100), ' percent similar ', count)
    solver.save()
    i+=1

    sum = 0
    for av in average:
        sum += av

    print('TOTAL AV: ', sum/len(average))