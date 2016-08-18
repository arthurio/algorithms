# coding=utf8
from trie import WordCountTrie


def find_k_most_frequent_word(words, k):
    ''' Return the kth most frequent word in a text.
    This version is naive and will consider I'm and I am as two different words.
    It replaces all punctuations and line breaks with spaces.
    It lowercases all the letters.

    Args:
        words (list(str)): List of words, it can contain duplicates.
        k (int): Integer indicating the occurrence rank of the word to be returned.

    Returns:
        word: The kth most frequent word in the list.
    '''


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
