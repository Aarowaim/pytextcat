# pytextcat
1. Write text in your favourite editor
2. Access the parts you need inside your program

## What is a "Text Catalog"?
Text storage is a very common problem and I needed a simple, portable format to manage walls of text without polluting my source code.
Python text catalogs are a simple way to edit, access, and keep track of all the text your program needs.
They're a UTF-8 file formatted into entries, which consist of a *label line* followed by *text data*.

Although there are many domain-specific formats for this purpose, few of them were generic, simple, and ported to a variety of languages. This format was designed to fill that niche by fulfilling three major goals:

* Easy to view and write
* Easy to access in a programming language
* Control characters should be visible only to a program

Text catalogs are **not** a library, they're just a portable container format for text. As a container format, no assumptions are made about the structure of *text data*. As long as it can be encoded in UTF-8 (and doesn't contain *label lines*), it can be placed in an entry. This allows any type of structured format to be embedded in an entry, such as csv, json, or yaml. A future objective is to ensure compatibility with `ini` formatted *text data*.

## How do I Install this Package?

Before you try these commands, make sure you have installed `git` and `pip` on your system by running these commands in your terminal:

```
git --version
pip --version
```

If you haven't received errors, you can install this package (which was developed on python 3.6.4) by running these commands:

```
git clone https://github.com/Aarowaim/pytextcat.git
cd pytextcat
pip install .
```

Make sure you were running the commands as an admin (`sudo` on linux), `Run as Administrator` on windows. You should be able to write your own text catalogs now!

Here's a simple example of using the package:

```python
from pytextcat import TextCatalog

my_catalog = TextCatalog('my_file.txt')
print(my_catalog['my_label'])
```

## How do I Write a Text Catalog?
Each text catalog consists of a series of entries. An entry has two parts: the *label line*, and the *text data*. *Label lines* always begin with `[` and end with a platform-specific newline. Everything after `[` until `]` is considered the *label*, and is the name an implementation uses to access the *text data*. The *text data* is everything that follows, and ends when the next *label line* occurs, or when the file ends.

Two features are provided for editing convenience.
* A *label line* can have whitespace characters following `]` until the end of the line,. If any characters aside from whitespace are encountered, then the line is interpreted as part of the previous entry's *text data*.
* If the platform-specific newline is the last character in *text data*, it is ignored. This means that you can leave 1 blank line after each entry so that the file is more readable. If you want more whitespace, consider using `.lstrip()` once the file is loaded in python.
An example catalog is provide below, and is compatible with the previous usage example:

```ini
[my_label]
Hello world,
here there be newlines!

```

## What are Some Usecases for Text Catalogs?
Text catalogs are a simple container format (intended for UTF-8 encoded plaintext) that removes the need for escape sequences (`\n`, `\t`) you would normally write within your program. You can write a text catalog easily in your favourite editor to preview how it will appear when it reaches the user interface of your program.

Being so simple makes them ideal for a variety of uses:
* Ascii art retains its formatting
* A text adventure's flavour text can be catalogued, retaining text formatting sequences (like `{}` in python or [printf strings](https://en.wikipedia.org/wiki/Printf_format_string))
* By using the same labels in different files, your program can quickly switch to alternate text. You can use this for primitive localization, to switch your game's theme, or to separate game data into scenes.
* Commandline interface help docs can be stored, formatted, and edited as it would appear in the terminal. Leveraging your text editor, you can preview monospace fonts and different tab-spacings.
* You can embed structured data. This allows markdown, testcases for codegolfing, comma separated values, html, and a variety of other plaintext data to coexist in the same text catalog.

## What Languages are Supported?
Currently, this python package provides a reference implementation.

You may freely port this package into other languages, but please call the format a "text catalog" so that it's easy for other programmers to find implementations. If you write an implementation, feel free to get in touch with me to add it to this section. There's a few things to consider when writing your own implementation.

To aid portability, a conforming implementation *must* detect whether `\n`, `\r`, `\n\r`, `\r\n` newlines are used in a file, and use those to split it into parts. Detecting newlines is a file-specific responsibility, not a platform-specific one. Programs should be confident that dumping *text data* from the catalog into stdout will render as expected. While a conforming implementation *must* provide *text data* as if it contained **platform-specific newlines** in the place of the file-specific ones (*via the natural calling convention of the implementation*), it may also optionally provide *text data* containing raw newlines through a secondary calling convention.

## What Formats weren't "Generic Enough"?

| Format        | Comments          |
| :------------- |:-------------|
| [IBM Cúram Message Files](https://www.ibm.com/support/knowledgecenter/SS8S5A_7.0.0/com.ibm.curam.content.doc/ServerDeveloper/r_SERDEV_Message1FormatMessageFiles1.html)     | xml-structured localization format. Because it's designed for localization and uses xml to define a structure, it's not very flexible |
| [Microsoft Message Files](https://msdn.microsoft.com/en-us/library/windows/desktop/dd996907(v=vs.85).aspx)     | A structured format for localized error/logging messages. Has a much more human-friendly structure, but like Cúram is not flexible |
| [Java `.properties` Files](https://www.mkyong.com/java/java-properties-file-examples/) | A structured key-value format. Similar to the venerable `.ini` format that inspired the `[label]` syntax of text catalogs. Sometimes used for localization, but is a generic way to associate text to a label, so it's flexible. The drawback is that "Characters not in Latin1, and certain special characters" must be represented using escape sequences, so it's not ideal for copy-pasting *text data* from external sources. |
| `csv` | A structured format with fields separated by a delimiter (commas usually). An optional header may denote names of each column. Tabular data is great and this format is as generic as it can be. Having an explicit structure with usage-specified delimiters means that this format does not play nicely with whitespace and punctuation. So while a human can write csv, embedding plaintext data is not simple. |
| `.ini` | A key-value format that can be separated into sections. Great for configuration data and associations, but many implementations are whitespace sensitive. So it's also not ideal for storing human-formatted text like cowsay. |
| Text Adventure Data | Text adventures frequently need to manage lots of text and game data. They often need their files to contain language-specific formatting sequences and serialized game-data. Text adventures were solving the problem of embeddable plaintext long before the luxury of github and python existed, so a common format was never formally specified. Examples can be found in [Colossal Cave Adventure](https://gitlab.com/esr/open-adventure/blob/master/adventure.yaml) and [Nethack](https://github.com/NetHack/NetHack/blob/NetHack-3.6.0/dat/quest.txt) where files contain a variety of embedded data, such as alternate text, format strings, game objects, and even game logic. The formats are often somewhat clunky because their primary role is to hold game data instead of plaintext data. |
