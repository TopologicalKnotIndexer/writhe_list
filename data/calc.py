from sage.all import *
import os
dirnow           = os.path.dirname(os.path.abspath(__file__))
com_pd_code_file = os.path.join(dirnow, "com_pd_code_list.txt")
ans_writhe_file  = os.path.join(dirnow, "writhe_list.txt")

def main():
    fp = open(ans_writhe_file, "w")
    for line in open(com_pd_code_file):
        knot, pd_code = (line.strip()[1:-1]).split("|")
        writhe = (Knot(eval(pd_code)).writhe())
        fp.write("[%d|%s|%s]\n" % (writhe, str(pd_code), knot))
    fp.close()

if __name__ == "__main__":
    main()