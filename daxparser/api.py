import sys
from antlr4 import InputStream
from daxparser.DAXLexer import DAXLexer
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class ColumnOrMeasure:
    orig_string: str
    col_name: str
    orig_table_string: Optional[str]
    table: Optional[str]

def column_from_texts(*, col_text: str, table_text: Optional[str]):
    return ColumnOrMeasure(orig_string= col_text, col_name= col_text[1:-1].replace("]]", "]"), orig_table_string= table_text, table= table_text[1:-1].replace("''", "'") if table_text else None)

def get_columns_or_measures(dax: str) -> list[ColumnOrMeasure]:
    input_stream = InputStream(dax) #FileStream("test.dax")
    lexer = DAXLexer(input_stream)
    tokens = lexer.getAllTokens()
    ls: list[ColumnOrMeasure] = list()
    table_text: Optional[str] = None
    for tk in tokens:
        if tk.type == DAXLexer.TABLE:
            table_text = tk.text
        elif tk.type == DAXLexer.TABLE_OR_VARIABLE:
            table_text = tk.text            
        elif tk.type == DAXLexer.COLUMN_OR_MEASURE:
            ls.append(column_from_texts(col_text=tk.text, table_text=table_text))
            table_text = None
        else:
            table_text = None
    return ls