'''
This example demonstrates the use of a text catalog as a very primitive
translation system. By using a common set of tags between multiple files,
it becomes possible to swap out text simply by loading a different file.
'''

from pytextcat import TextCatalog
import os


def hello_world(language_code):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    fname = os.path.join(current_dir, '{}.trans'.format(language_code))
    cat = TextCatalog(fname)

    name = input(cat['prompt'])
    print(cat['greeting'].format(name))


for code in ['en', 'ja']:
    hello_world(code)
