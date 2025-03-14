import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp("i'm sad")
final = []
for token in doc:
    if token.is_punct or token.like_num:
        continue
    # Skip stop words UNLESS they are marked as sentiment-bearing.
    if token.is_stop:
        continue
    lemma = token.lemma_.lower().strip()
    if lemma and lemma != '-pron-':
        final.append(lemma)
print(final)