# coding=utf8
from trie import WordCountTrie


if __name__ == '__main__':
    text = (
        "My name is Arthur and I am twenty years old. "
        "My wife is Cyriele, she is twenty one years old "
        "and sometimes I wish I had more wifes."
    )

    dictionnary = WordCountTrie()
    for word in text.replace(".", "").replace(",", "").split(" "):
        dictionnary.add(word)

    print dictionnary.get_all_words()
