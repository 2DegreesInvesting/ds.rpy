# Included in Anaconda
import nltk
import spacy

sent = "Please book my flight to California."

tokenized_sent_nltk = nltk.sent_tokenize(sent)
[nltk.pos_tag(nltk.word_tokenize(word)) for word in tokenized_sent_nltk]

# conda install -c conda-forge spacy-model-en_core_web_sm
nlp = spacy.load("en_core_web_sm")
spacy_doc = nlp(sent)

print(spacy_doc)

for token in spacy_doc:
    print(token.text, token.pos_)
