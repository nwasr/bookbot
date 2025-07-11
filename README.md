#  Bookbot

Bookbot is a Python program that analyzes `.txt` files of novels — specifically those downloaded from **[Project Gutenberg](https://www.gutenberg.org/)** — and generates a statistical report on word and character usage.

## Features

* Analyzes word count and character frequency in any `.txt` book
* Designed for use with plain-text novels from Project Gutenberg
* Clean terminal output with frequency reports

## Sample Output

```text
--- Begin Report ---
The book contains 72,314 words.
Most common characters:
  e: 9273
  t: 8031
  a: 7021
  ...
--- End Report ---
```

## Project Structure

```
bookbot/
├── books/                
│   ├── frankenstein.txt
│   └── pride-and-prejudice.txt
├── main.py               
├── stats.py            
├── README.md             
```

## Usage

1. Download a `.txt` novel from [Project Gutenberg](https://www.gutenberg.org/)
2. Place it in the `books/` directory
3. Run the script:

```bash
python main.py book_path
```

You should see a statistical breakdown of the text in your terminal.


