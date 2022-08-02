import atheris
import sys
import os
from conllu import parse, parse_tree
from conllu.exceptions import ParseException

def TestOneInput(data):
    data1 = " The quick brown fox jumps over the lazy dog."
    barray=bytearray(data)
    fdp=atheris.FuzzedDataProvider(data)
    try:
        if len(barray)>0:
            if barray[0]%3==0:
                sentences=parse(fdp.ConsumeString(len(data)))
            if barray[0]%3==1:
                sentences=parse_tree(fdp.ConsumeString(len(data)))
            else:
                sentences=parse(data1)
                sentences=filter(form=fdp.ConsumeString(len(data)))
        else:
            sentences=parse(fdp.ConsumeString(len(data)))
    except ParseException as e:
        pass



atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
