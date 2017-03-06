#!/usr/bin/python
import sys

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
    doc= document("enwiki-sample-1.txt")
    doc.printparas()
    doc.write("tmp.txt")