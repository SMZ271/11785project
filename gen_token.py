# from pathlib import Path

from tokenizers import ByteLevelBPETokenizer

paths = ['limericks_with_syllables_new.txt']
sy_path = "syllable.txt"

# Initialize a tokenizer
tokenizer = ByteLevelBPETokenizer()


f = open(sy_path)               
line = f.readline()  
special_tokens=['<|endoftext|>']

while line: 
    # print line,                   
    line = f.readline()  
    special_tokens.append("<" + line.strip('\n') + ">")
f.close()  
print(special_tokens)
# Customize training
tokenizer.train(files=paths, vocab_size=52000, min_frequency=2, special_tokens=special_tokens)

# special_tokens_dict = {'bos_token': '<BOS>', 'eos_token': '<EOS>', 'pad_token': '<PAD>'}
# tokenizer.add_special_tokens(special_tokens_dict)

# # Save files to disk
tokenizer.save_model("poem")