import argparse


class Tok:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.count < other.count if self.count != other.count else self.name < other.name


def process_lines(line:str) -> list[str]:
    """
    Takes in one line of input text file and return a list of lowercase alphanumeric strings split by non-alphanumeric
        characters.
    When the line as n alphanumeric characters, m non-alphanumeric characters, and x alphanumeric words, the code takes
        from n + x upto (n+m)^m + x to process, as it has to check each character if it is alphanumeric, and if it not,
        replace function goes through every character and change the character to space, then append split words into list.
    """
    words = []
    line = line.strip()
    for char in line:
        if not char.isalnum():
            line = line.replace(char, ' ')
    for word in line.split():
        words.append(word.lower())
    return words


def tokenize(p:str) -> list[str]:
    """
    Takes in a text file name and returns a list of alphanumeric strings split by non-alphanumeric characters.
    The code takes n to process, where n is the number of lines in the file, as the function simply adds all lists
        returned by process_lines.
    """
    ret = []
    with open(p, encoding='utf-8') as f:
        for line in f:
            ret += process_lines(line)
    return ret

def computeWordFrequencies(l:list[str]) -> dict[str, int]:
    """
    Takes in a list of all alphanumeric words and convert it into a dictionary that maps each word to its frequency.
    The function takes n to process, where n is the size of the list, as the function simply adds each word
        in the list to the dictionary.
    """
    d = {}
    for tok in l:
        if tok not in d.keys():
            d[tok] = 1
        else:
            d[tok] += 1
    return d

def Frequencies(d:dict[str, int]) -> None:
    """
    Takes in a dictionary and create a token for each key, sort them based on their frequency,
        then print them in sorted order.
    The code takes n log(n) + n to process, where n is the size of the dictionary, taking n to convert each word into
        a token, and taking n log(n) to sort the created tokens.
    """
    l = []
    for word in d.keys():
        l.append(Tok(word, d[word]))
    l.sort(reverse=True)
    for token in l:
        print(f"{token.name} : {token.count}")


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("input")
        args = parser.parse_args()

        Frequencies(computeWordFrequencies(tokenize(args.input)))
    except FileNotFoundError as e:
        print("not valid file path.")
    except TypeError as e:
        print("one or more arguments are missing.")
    except Exception as e:
        print(e)

