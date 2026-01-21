# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Minr Docs'
author = 'Minr'

release = '0.1'
version = '2.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

# -- MSC Syntax Highlighting

from pygments.lexer import RegexLexer, Lexer, bygroups
from pygments.token import Comment, Keyword, Text, Name, String, Number, Operator, Punctuation, Token, _TokenType
from sphinx.highlighting import lexers

# Minecraft color codes mapping
MC_COLORS = {
    '0': '#000000',  # Black
    '1': '#0000AA',  # Dark Blue
    '2': '#00AA00',  # Dark Green
    '3': '#00AAAA',  # Dark Aqua
    '4': '#AA0000',  # Dark Red
    '5': '#AA00AA',  # Dark Purple
    '6': '#FFAA00',  # Gold
    '7': '#AAAAAA',  # Gray
    '8': '#555555',  # Dark Gray
    '9': '#5555FF',  # Blue
    'a': '#55FF55',  # Green
    'b': '#55FFFF',  # Aqua
    'c': '#FF5555',  # Red
    'd': '#FF55FF',  # Light Purple
    'e': '#FFFF55',  # Yellow
    'f': '#FFFFFF',  # White
}

# Create custom token types for Minecraft formatting
# Access Token.Mc0, Token.Mc0l, etc. to auto-create them as proper Pygments tokens
MC_TOKENS = {}
for color in '0123456789abcdef':
    for fmt in ['', 'l', 'o', 'n', 'lo', 'ln', 'on', 'lon']:
        token_name = f'Mc{color}{fmt}'
        # Accessing Token.X auto-creates a new token type
        MC_TOKENS[token_name] = getattr(Token, token_name)


class MinecraftOutputLexer(Lexer):
    """Lexer for Minecraft chat output with formatting codes."""
    name = 'Minecraft Output'
    aliases = ['output', 'mcoutput']

    def get_tokens_unprocessed(self, text):
        color = 'f'  # Default white
        bold = False
        italic = False
        underline = False

        i = 0
        buf = ''
        buf_start = 0

        while i < len(text):
            # Newlines reset formatting (each line is independent in MC chat)
            if text[i] == '\n':
                if buf:
                    token = self._get_token(color, bold, italic, underline)
                    yield buf_start, token, buf
                    buf = ''
                yield i, Text, '\n'
                color = 'f'
                bold = italic = underline = False
                i += 1
                buf_start = i
            elif text[i] == '&' and i + 1 < len(text):
                code = text[i + 1].lower()

                # Flush buffer with current formatting
                if buf:
                    token = self._get_token(color, bold, italic, underline)
                    yield buf_start, token, buf
                    buf = ''

                if code in MC_COLORS:
                    # Color resets all formatting
                    color = code
                    bold = italic = underline = False
                    i += 2
                    buf_start = i
                elif code == 'l':
                    bold = True
                    i += 2
                    buf_start = i
                elif code == 'o':
                    italic = True
                    i += 2
                    buf_start = i
                elif code == 'n':
                    underline = True
                    i += 2
                    buf_start = i
                elif code == 'r':
                    color = 'f'
                    bold = italic = underline = False
                    i += 2
                    buf_start = i
                else:
                    buf += text[i]
                    i += 1
            else:
                buf += text[i]
                i += 1

        # Flush remaining buffer
        if buf:
            token = self._get_token(color, bold, italic, underline)
            yield buf_start, token, buf

    def _get_token(self, color, bold, italic, underline):
        name = f'Mc{color}'
        if bold:
            name += 'l'
        if italic:
            name += 'o'
        if underline:
            name += 'n'
        return MC_TOKENS.get(name, Text)

lexers['output'] = MinecraftOutputLexer()

class MSCLexer(RegexLexer):
    name = 'MSC'
    aliases = ['msc']
    filenames = ['*.msc']

    tokens = {
        'root': [
            # Comments (lines starting with #)
            (r'#.*$', Comment.Single),
            # Operators at start of line (@word)
            (r'^(\s*)(@\w+)', bygroups(Text.Whitespace, Keyword)),
            # Expressions in {{ }}
            (r'\{\{', Punctuation, 'expression'),
            # Strings
            (r'"[^"]*"', String),
            # Everything else
            (r'.', Text),
            (r'\n', Text.Whitespace),
        ],
        'expression': [
            (r'\}\}', Punctuation, '#pop'),
            # Numbers
            (r'\b\d+(\.\d+)?[DdFf]?\b', Number),
            # Namespace functions (namespace::function)
            (r'(\w+)(::)(\w+)', bygroups(Name.Namespace, Operator, Name.Function)),
            # Method calls (.method)
            (r'\.(\w+)', bygroups(Name.Function)),
            # Operators
            (r'[+\-*/%<>=!&|]+', Operator),
            # Parentheses, brackets
            (r'[(),\[\]]', Punctuation),
            # Identifiers
            (r'\w+', Name),
            # Whitespace
            (r'\s+', Text.Whitespace),
        ],
    }

lexers['msc'] = MSCLexer()

# -- Custom RST roles for Minecraft formatting
from docutils import nodes
from docutils.parsers.rst import roles

def underline_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.inline(rawtext, text, classes=['underline'])
    return [node], []

def strikethrough_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.inline(rawtext, text, classes=['strikethrough'])
    return [node], []

def obfuscated_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.inline(rawtext, text, classes=['obfuscated'])
    return [node], []

roles.register_local_role('underline', underline_role)
roles.register_local_role('strike', strikethrough_role)
roles.register_local_role('obfuscated', obfuscated_role)

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['minecraft.css']

# -- Options for EPUB output
epub_show_urls = 'footnote'