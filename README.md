#  C Scanner in Python

##  Overview

This is a simple **lexical analyzer (scanner)** written in Python.
It reads a C source code file, extracts **tokens**, and categorizes them into standard token types such as **keywords**, **identifiers**, **operators**, **numeric constants**, **character constants**, **special characters**, **comments**, **whitespace**, and **newlines**.

The scanner writes all extracted tokens to a file named `tokens.txt` and also prints them on the screen.

---

##  How It Works

1. The C source code is read from a file (e.g., `code.c`).
2. Regular expressions (`re` module) are used to detect patterns for each token type.
3. Each matched token is stored as a `(TYPE, VALUE)` pair.
4. The results are:

   * Printed to the terminal.
   * Saved into a `tokens.txt` file in the same directory.

---

##  Token Categories

| Token Type             | Description                                                    |
| ---------------------- | -------------------------------------------------------------- |
| **KEYWORDS**           | Reserved words like `int`, `if`, `else`, `return`, etc.        |
| **IDENTIFIERS**        | Variable and function names (e.g., `x`, `y`, `main`).          |
| **OPERATORS**          | Arithmetic and logical operators (`+`, `-`, `==`, `!=`, etc.). |
| **NUMERIC_CONSTANTS**  | Numbers (e.g., `42`, `3.1`).                                   |
| **CHAR_CONSTANTS**     | Character literals like `'a'`.                                 |
| **SPECIAL_CHARACTERS** | Symbols like `{}`, `()`, `;`, `,`.                             |
| **COMMENTS**           | Single-line (`//`) or block (`/* ... */`) comments.            |
| **WHITESPACE**         | Spaces and tabs.                                               |
| **NEWLINE**            | Line breaks `\n`.                                              |

---

##  Example

### Input (`code.c`)

```c
int main() {
    int x,y;
    // This is a single-line comment
    if (x == 42) {
        /* This is
           a block
           comment */
        x = x-3;
    } else {
        y = 3.1; // Another comment
    }
    return 0;
}
```

### Output (printed and saved to `tokens.txt`)

```
KEYWORD           : 'int'
IDENTIFIER        : 'main'
SPECIAL_CHAR      : '('
SPECIAL_CHAR      : ')'
SPECIAL_CHAR      : '{'
...
COMMENT_SINGLE    : '// This is a single-line comment'
...
```

---

##  Usage

1. Save the scanner code as `scanner.py`.
2. Place your C file (e.g., `code.c`) in the same directory.
3. Run in terminal:

   ```bash
   python scanner.py
   ```
4. Check the terminal output and the generated file `tokens.txt`.

---

##  Requirements

* **Python 3.7+**
* No external libraries required (uses only the built-in `re` module).

---

##  Notes

* This version does **not** handle complex string literals, hexadecimal or scientific numbers.
* Line numbers are not recorded.
* It only performs **lexical analysis**, not parsing or syntax validation.
