from pathlib import Path


from tokenizers import BertWordPieceTokenizer
paths = "dataset/syllables.txt"

# Initialize a tokenizer
tokenizer = BertWordPieceTokenizer()

tokenizer.train(files=paths, vocab_size=52_000, min_frequency=1, special_tokens=[
    "<s>",
    "<pad>",
    "</s>",
    "<unk>",
    "<mask>",
])

output=tokenizer.encode("washed")
print(output.tokens)
print(output.ids)
# Customize training
tokenizer.save_model(".", "esperberto")

# Save files to disk
