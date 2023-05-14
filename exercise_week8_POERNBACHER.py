import spacy
import os


# QUESTION NR 1
def write_to_file(text, output_file_path):
    if os.path.exists(output_file_path):
        # if file already exists raise runtimeerror
        raise RuntimeError("Output file already exists!")
    # open file with write mode
    with open(output_file_path, 'w') as file:
        file.write(text)


# QUESTION NR 2
def count_stopwords(input_file_path):
    # en_core_web_sm = refers to the small english language model provided by spacy
    nlp = spacy.load('en_core_web_sm')
    stopwords = nlp.Defaults.stop_words
    count = 0
    # open file with read mode
    with open(input_file_path, 'r') as file:
        text = file.read()
        # go through text with spacy
        doc = nlp(text)
        for token in doc:
            if token.text.lower() in stopwords:
                count += 1
    return count


# QUESTION NR 3
def remove_stopwords(input_file_path, output_file_path):
    nlp = spacy.load('en_core_web_sm')
    stopwords = nlp.Defaults.stop_words
    # open input file with read mode
    with open(input_file_path, 'r') as input_file:
        text = input_file.read()
        # go through text with spacy
        doc = nlp(text)
        result = ' '.join([token.text for token in doc if token.text.lower() not in stopwords])
    # open output file with write mode
    with open(output_file_path, 'w') as output_file:
        output_file.write(result)


# QUESTION NR 4
def tokenize_text(input_file_path, output_file_path):
    nlp = spacy.load('en_core_web_sm')
    with open(input_file_path, 'r') as input_file:
        text = input_file.read()
        # go through text with spacy
        doc = nlp(text)
        tokens = []
        for token in doc:
            tokens.append([token.text, token.pos_, token.tag_, token.dep_])
    with open(output_file_path, 'w') as output_file:
        for token in tokens:
            output_file.write('\t'.join(token) + '\n')


# QUESTION NR 5
import spacy
from spacy import displacy

def save_visualization(input_file_path, output_file_path):
    nlp = spacy.load('en_core_web_sm')
    # open input file with read mode
    with open(input_file_path, 'r') as input_file:
        text = input_file.read()
        doc = nlp(text)
    svg = displacy.render(doc, style='dep', jupyter=False)
    with open(output_file_path, 'w') as output_file:
        output_file.write(svg)
