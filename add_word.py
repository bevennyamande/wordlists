import click

# generate word permutation from given word
# spider a shona/ ndebele dictionary and split the words into 
# useful names

@click.command()
@click.argument("word")
@click.argument("lang")
def main(word, lang):
    ''' Simple application for adding words to the wordlists 

        Example usage:

        python3 add_word.py WORD LANG

        lang: the language option its either nd for ndebele or sh for shona

    '''

    word = word
    lang = lang

    if lang == "nd":
        with open('ndebele.txt', 'r+') as f:
            if word in f.readlines():
                print(f'{word} already in wordlist. Thank you')

            f.write(word+'\n')
            print(f'{word} successfully added to wordlist')

    elif lang == "sh":
        with open('shona.txt', 'r+') as f:
            if word in f.readlines():
                print(f'{word} already in wordlist. Thank you')

            f.write(word+'\n')
            print(f'{word} successfully added to wordlist')
    else:
        print('Your provided an invalid language')


if __name__ == '__main__':
    main()

