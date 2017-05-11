#!/usr/bin/python
import os, sys
import random

class paragraph(object):
    def __init__(self, lines):
        self.lines= lines

class document(object):
    def __init__(self):
        self.paras= []
        
    def clear(self):
        self.paras= []
    
    def load(self, path):
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
    
    def mkpara(self, word, wordcount):
        return paragraph( [" ".join((word for i in range(wordcount)))+"\n"] + ["\n"] )
    
    def mkparas(self, word, wordcount, paracount):
        for i in range(paracount):
            self.paras.append(self.mkpara(word, wordcount))
        
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
    doc= document()
    wordA= "AAAAAAA"
    wordB= "BBBBBBB"
    
    #~ doc.clear()
    #~ doc.mkparas(wordA, 50, 10)
    #~ doc.write("a.txt")
    #~ doc.clear()
    #~ for i in range(1, 5):
        #~ doc.mkparas(wordA, 50, 1)
        #~ doc.mkparas(wordB, 50, 1)
    #~ doc.write("b.txt")
    #~ os.system("php dodiff.php a.txt b.txt")
    #~ exit(0)
    
    wordsPerParagraph= 100
    for i in range(1, 50):
        doc.clear()
        doc.mkparas(wordA, wordsPerParagraph, i)
        doc.write("a.txt")
        doc.clear()
        doc.mkparas(wordB, wordsPerParagraph, i)
        doc.write("b.txt")
        os.system("php dodiff.php a.txt b.txt")
        sys.stdout.flush()
    #~ os.remove("a.txt")
    #~ os.remove("b.txt")
    exit(0)
    
    doc= document("a.txt")
    doc.permutate("tmp.txt", 1)
    exit(0)
    
    
    sample= "enwiki-sample-1.txt"
    doc= document()
    doc.load("enwiki-sample-1.txt")
    #~ doc.printparas()
    #~ doc.write("tmp.txt")
    
    for i in range(1, 100):
        #~ print i
        sys.stdout.flush()
        doc.permutate("tmp.txt", i)
        os.system("php dodiff.php %s tmp.txt" % sample)
