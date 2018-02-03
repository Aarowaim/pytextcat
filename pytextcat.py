import re


class TextCatalog(dict):

    def __init__(self, fname):

        with open(fname, 'U', encoding='utf-8') as f:
            # Add a newline to the text for convenience
            # beginning the file with a key becomes possible
            text = '\n' + str(f.read())

            # parse out the entries and their text
            data = re.split('\n\[(.+?)\]\s*\n', text)

            # trim empty string by starting at 1
            for i in range(1, len(data) - 1, 2):
                entry_text = data[i+1]
                if entry_text[-1] == '\n':
                    entry_text = entry_text[:-1]
                self[data[i]] = entry_text
