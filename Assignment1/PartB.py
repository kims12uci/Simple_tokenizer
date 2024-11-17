import argparse
from PartA import tokenize

def getCommon(s1:set[str], s2:set[str]) -> None:
    """
    Takes in two sets of strings, print the common words and how many common words there are.
    The code takes n to process, where n is the number of strings in s1, as the code checks if each string in s1 is in
        s2 and sets utilize hash search.
    """
    common = []
    for word in s1:
        if word in s2:
            common.append(word)
    print(f"Common words: {common}\nNumber of common words: {len(common)}")

def run(input1:str, input2:str) -> None:
    """
    Takes in two file names, then calls tokenize and getCommon functions to display common words in the files.
    The code itself take O(1) to process, as it simply calls other functions to process input.
    """
    in1tok = set(tokenize(input1))
    in2tok = set(tokenize(input2))

    if len(in1tok) < len(in2tok):
        getCommon(in1tok, in2tok)
    else:
        getCommon(in2tok, in1tok)


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("input1")
        parser.add_argument("input2")
        args = parser.parse_args()

        run(args.input1, args.input2)

    except FileNotFoundError as e:
        print("not valid file path.")

    except TypeError as e:
        print("one or more arguments are missing.")
    except Exception as e:
        print(e)

