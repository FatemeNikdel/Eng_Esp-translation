


def load_doc_of_dataset (path):
    with open(path, encoding='UTF-8') as f:
        lines = f.read().split("\n")[:-1]   # the last line is empty in dataset
    return lines

# We consider [start], [end] as tokens for start and end. they are in brackets to be distinguish from other words.

def create_pairs(lines):
    text_pairs = []    # Pairs are like this: (English, Spanish)
    for i in lines:
        English, Spanish = lines.split("\t")     # English and Spanish words in dataset are seprate by Tab
        Spanish = "[start]" + Spanish + "[end]"
        text_pairs.append((English,Spanish))
    print("[INFO]: printing sample data ...")
    print(random.choice(text_pairs))
    return text_pairs


