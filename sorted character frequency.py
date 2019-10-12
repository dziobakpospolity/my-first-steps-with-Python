#   PCAP - Programming essentials in Python course - Cisco Networking Academy
#   LAB: (Sorted) Character frequency histogram

#   A text file contains some text (nothing unusual) but we need to know how often (or how rare)
#   each letter appears in the text. Such an analysis may be useful in cryptography, so we want
#   to be able to do that in reference to the Latin alphabet.

#   Your task is to write a program which:

#   - asks the user for the input file's name;
#   - reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
#   - prints a simple histogram (only non-zero counts should be presented)
#   - the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
#   - the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' (it should be concatenated to the original name)

from os import strerror

Alphabet = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,
            'm':0, 'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,
            'y':0,'z':0}

FileName = input("Source file name?: ")

try:
    InputFile = open(FileName, 'rt')
except IOError as e:
    print("Cannot open source file: ", strerror(e.errno))
    exit(e.errno)
    
content = InputFile.read()
for ch in content.lower():
    if ch in Alphabet:
        Alphabet[ch] += 1
            
InputFile.close()

try:
    OutputFile = open(FileName + ".hist", 'wt')
    for elem in sorted(Alphabet, key=Alphabet.get, reverse=True):
        if Alphabet[elem] > 0:
            print(elem, " -> ", Alphabet[elem])
            OutputFile.write(elem + " -> " + str(Alphabet[elem]) + "\n")
    OutputFile.close()
except IOError as e:
	print("I/O error occurred: ", strerr(e.errno))       


