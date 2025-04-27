import spacy

# Load the medium model (has word vectors)
nlp = spacy.load("en_core_web_md")

def check_plagiarism(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    similarity = doc1.similarity(doc2)
    print(f"Accurate similarity: {similarity:.1%}")
    return similarity

check_plagiarism("The cat sits on the mat", "A kitten is sitting on the rug")