import re

# تعريف أنواع التوكنز
token_specification = [
    ('COMMENT_BLOCK', r'/\*[\s\S]*?\*/'),
    ('COMMENT_SINGLE', r'//.*'),
    ('KEYWORD', r'\b(int|float|char|if|else|for|while|return|main)\b'),
    ('CHAR_CONSTANT', r"'(\\.|[^\\'])'"),
    ('IDENTIFIER', r'\b[a-zA-Z_]\w*\b'),
    ('NUMERIC_CONSTANT', r'\b\d+(\.\d+)?\b'),
    ('OPERATOR', r'==|!=|<=|>=|\+|-|\*|/|=|<|>'),
    ('SPECIAL_CHAR', r'[{}()\[\];,]'),
    ('WHITESPACE', r'[ \t]+'),
    ('NEWLINE', r'\n'),
]

# دمج الأنماط
tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
print(tok_regex)

# قراءة الكود من ملف
with open('code.c', 'r', encoding='utf-8') as f:
    code = f.read()

# استخراج التوكنز
tokens = []
for match in re.finditer(tok_regex, code):
    kind = match.lastgroup
    value = match.group()
    tokens.append((kind, value))

# كتابة النتائج في ملف
with open('tokens.txt', 'w', encoding='utf-8') as out:
    for kind, value in tokens:
        line = f"{kind:18}: {repr(value)}"
        print(line)
        out.write(line + "\n")

print("\nTokens written to tokens.txt successfully.")
