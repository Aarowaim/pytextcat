# pytextcat
The idea is simple:
1. Write text in your favourite editor
2. Open it in python using a label

## What is a "Text Catalog"?
Text storage is a very common problem and I needed a simple, portable format to manage walls of text without polluting my source code.
Python text catalogs are a simple way to edit, access, and keep track of all the text your program needs.
They're utf-8 plaintext files formatted into entries, and each entry consists of a *label line* which is followed by *text*. the entry ends when a new *label line* is encountered.

Although there are many domain-specific libraries for this purpose, very few of them are generic, simple, and ported to a variety of languages. This format was designed to fill that niche, and it's handy enough to share. It's also simple enough to port.

It should be noted that text catalogs are **not** a library, such as this one. They are a utf-8 plaintext file format designed to be easy to write, and easy to port between languages. **A conforming implementation must detect whether `\n`, `\r`, `\n\r`, `\r\n` newlines are used in a file** (observing platform convention is not enough to make a file portable). The library must present **platform-specific newline sequences** so that programs can be confident that dumping *text* from the catalog into stdout will render as expected.

## How do I Install this Package?

Using the commandline may be unfamiliar and new to some programmers. Before you try these commands, make sure you have installed `git` and `pip` on your system by running these commands in your terminal:

    git --version
    pip --version
    
If you haven't received errors, you can install this package (which was developed on python 3.6.4) by running these commands:

    git clone https://github.com/Aarowaim/pytextcat.git
    cd pytextcat
    pip install .
    
Make sure you were running the commands as an admin (`sudo` on linux), `Run as Administrator` on windows. You should be able to write your own text catalogs now!

Here's a simple example of using the package:

    from pytextcat import TextCatalog

    my_catalog = TextCatalog('my_file.txt')
    print(my_catalog['my_label'])

## How do I Write a Text Catalog?
Lines with labels always begin with `[` and end with `\n` (an auto-detected newline). Everything until `]` is considered the *label*, and is the name used to access the text.

It's okay to forget whitespace at the end of a label's line, but any other type of text after `]` means the line __has no label__

Then everything after the label's line is considered the *text*, until a new label line appears. There's one feature that was added for convenience. If the `\n` (auto-detected newline) is the __last character in *text*__, it is ignored. This means that you can leave 1 blank line after each entry so that the file is more readable. If you want more whitespace, consider using `.lstrip()` once the file is loaded in python.
An example catalog is provide below, and is compatible with the previous usage example:

    [my_label]        
    Hello world,
    Look at these newlines!

## What are Some Usecases for Text Catalogs?
Text catalogs are a very simple format that removes the need for `\n` and `\t` in strings you write for your program. You can write one in your favourite text editor.

Being so simple makes them ideal for many common situations:
* Ascii art is easy to make, store, and use
* In a text adventure, flavour text can be catalogued and you can use text-formatting sequences compatible with your language (like `{}` in python)
* By using the same labels in different files, you can easily switch the text in your program. You can use this for primitive localization to other languages, or to theme your commandline game differently.
* Commandline interface help docs can be stored, formatted, and edited as it would appear in the terminal. Your text editor can preview it in different fonts and different tab spacings.
* You can include newline separate lists, markdown, codegolf input/output, or csv data under a label and parse it later once it's in your program

## What Languages are Supported?
Currently, there only seems to be this package written for python.

You may freely port this package into any other language, but please name the format a "text catalog" so that it's easy for other programmers to find packages for this particular file format. If you write an implementation, feel free to get in touch with me and I'll add it to this section.
