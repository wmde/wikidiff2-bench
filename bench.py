#!/usr/bin/python
import os, sys
import random

class paragraph(object):
    def __init__(self, lines):
        self.lines= lines

class document(object):
    def __init__(self, path):
        self.paras= []
        f= open(path, "r")
        para= []
        state= 0
        # split document into paragraphs
        for line in f:
            if state==0:    # adding newlines preceding text (considered part of first paragraph)
                para.append(line)
                if len(line.split())!=0:
                    state= 1
            elif state==1:  # adding non-empty text lines
                para.append(line)
                if len(line.split())==0:
                    state= 2
            elif state==2:  # adding newlines after text
                if len(line.split())!=0:
                    self.paras.append(paragraph(para))
                    para= [ line ]
                    state= 1
                else:
                    para.append(line)
        self.paras.append(paragraph(para))
        self.build_perm_()
        
    # build permutation list
    def build_perm_(self):
        self.perm= []
        self.perm2= []
        permleft= [ i for i in range(len(self.paras)) ]
        permleft2= [ i for i in range(len(self.paras)) ]
        for i in range(len(self.paras)):
            k= random.randint(0, len(permleft)-1)
            self.perm.append(permleft[k])
            del permleft[k]
            k= random.randint(0, len(permleft2)-1)
            self.perm2.append(permleft2[k])
            del permleft2[k]
    
    # writes to path with n paragraphs exchanged
    def permutate(self, path, n):
        paralist= [ i for i in range(len(self.paras)) ]
        for i in range(n):
            k= self.perm2[i]
            paralist[k]= self.perm[k]
            paralist[self.perm[k]]= k
        #~ print permlist
        with open(path, "w") as f:
            for p in paralist:
                para= self.paras[p]
                #~ print("para %s" % p)
                for line in para.lines:
                    f.write(line)
    
    def printparas(self):
        # quick check to see if paragraphs look ok
        p= 0
        for para in self.paras:
            for line in para.lines:
                sys.stdout.write("[%03d] %s" % (p, line))
            p+= 1
    
    def write(self, path):
        with open(path, "w") as f:
            for para in self.paras:
                for line in para.lines:
                    f.write(line)

if __name__ == '__main__':
    #~ doc= document("a.txt")
    #~ doc.permutate("tmp.txt", 3)
    #~ exit(0)
    
    
    sample= "enwiki-sample-1.txt"
    doc= document("enwiki-sample-1.txt")
    #~ doc.printparas()
    #~ doc.write("tmp.txt")
    
    for i in range(1, 100):
        #~ print i
        sys.stdout.flush()
        doc.permutate("tmp.txt", i)
        os.system("php dodiff.php %s tmp.txt" % sample)
