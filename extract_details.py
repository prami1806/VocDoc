import spacy
def extract_details(text):
    med7=spacy.load("en_core_med7_lg")
    col_dict={}
    seven_colours=['#e6194B', '#3cb44b', '#ffe119', '#ffd8b1', '#f58231', '#f032e6', '#42d4f4']
    for label,colour in zip(med7.pipe_labels['ner'],seven_colours):
        col_dict[label]=colour
    options={'ents':med7.pipe_labels['ner'],'colors':col_dict}
    doc=med7(text)
    return [(ent.text,ent.label_) for ent in doc.ents]
        
