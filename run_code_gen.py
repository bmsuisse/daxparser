import os
import requests
import subprocess

if not os.path.exists("antlr4.jar"):
    r = requests.get("https://www.antlr.org/download/antlr-4.13.0-complete.jar")
    r.raise_for_status()
    with open("antlr4.jar", "wb") as f:
        f.write(r.content)
if not os.path.exists("DAXLexer.g4"):
    r = requests.get(
        "https://raw.githubusercontent.com/TabularEditor/TabularEditor/master/AntlrGrammars/DAXLexer.g4"
    )
    r.raise_for_status()
    with open("DAXLexer.g4", "wb") as f:
        f.write(r.content)

# we work on a copy of the Lexer grammer because we need to adjust it minimally:
# add options { caseInsensitive = true; }
# remove backslash on line 413:30
# remove { } replaces which are in C#
subprocess.check_call(
    "java -jar ../antlr4.jar -Dlanguage=Python3 DAXLexer.g4", cwd="daxparser"
)
