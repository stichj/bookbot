# BookBot - Text Analysis Tool

**BookBot**  is a Python-based text analysis tool that reads a text file (e.g., a book) and generates a statistical report on the frequency of characters and words within the text. The tool is designed to process large text files and provide insights such as the frequency of each letter in the alphabet. 

In this project I have learn't to:
- read and modify the file tree
- read files from directories
- manipulate strings

## Tech Stack

-   **Python 3**
    

## Getting Started

### Prerequisites

Ensure you have Python 3 installed. You can verify by running:

```bash
python3 --version
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/stichj/bookbot.git 
cd bookbot
``` 
2. Download the textfile containing the book [frankenstein](https://www.gutenberg.org/cache/epub/41445/pg41445.txt).
3. Rename it to frankenstein.txt and move it into `bookbot/books/frankenstein.txt`

### Running the BookBot

1.  Make sure you have the textfile in `bookbot/books/frankenstein.txt`
    
2.  Run the following command:
    
```bash
python bookbot.py books/frankenstein.txt
```


### Output

The program will generate a statistical report like the following:

```bash
--- Begin report of books/frankenstein.txt ---
77986 words found in the file
Character 'e' was found 46043 times Character 't' was found 30365 times Character 'a' was found 26743 times ...
```

The report will include:

-   Total word count in the file
-   Frequency of each letter in the alphabet 
    
### Notes

-   **BookBot**  only processes the  **characters**  in the text and ignores case.
    
-   The  **book**  (text file) is  **not**  included in this repository. You will need to provide your own text files for analysis.
