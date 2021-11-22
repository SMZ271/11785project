from syllabipy.sonoripy import SonoriPy

f_in=open("dataset/limericks_input.txt","r",encoding="utf-8")
f_out=open("dataset/syllables.txt","w",encoding="utf-8")
for line in f_in:
    line=line.replace("\n","")
    if(line=="<|endoftext|>"):
        f_out.write("\n")
        continue
    temp=line.split(" ")
    for word in temp:
        word=SonoriPy(word)
        for syllable in word:
            f_out.write(syllable+" ")