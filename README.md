# 11785project

token_gen is used for generating syllable tokens, not word tokens
token_gen is used for generating syllable tokens, not word tokens
token_gen is used for generating syllable tokens, not word tokens

to load pretrained syllables token, use Bertokenizer from trainsformers.

tokenizer=BertTokenizer.from_pretrained("fre_1_syllables.txt") # or fre_2_syllables.txt

fre_1_syllables.txt and fre_2_syllables.txt are two tokenizer trained with different arguments. 
