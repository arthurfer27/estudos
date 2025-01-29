"""Functions for creating, transforming, and adding prefixes to strings."""

def add_prefix_un(word):
    return "un" + word


def make_word_groups(vocab_words):  
    return " :: ".join([vocab_words[0]] + [vocab_words[0]+word for word in vocab_words[1:]])

def remove_suffix_ness(word):
    new_word = word.replace(word[-4:], "")
    if new_word[-1] == "i":
        return new_word.replace(new_word[-1], "y")
    return new_word


def adjective_to_verb(sentence, index):
    sentence_splited = sentence.split()
    sentence_splited[index] = sentence_splited[index] + "en"
    if "." in sentence_splited[index]:
        sentence_splited[index] = sentence_splited[index].replace(".", "")
    return sentence_splited[index]