from antlr4 import InputStream
from daxparser.DAXLexer import DAXLexer
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ColumnOrMeasure:
    orig_string: Optional[str]  # Make this optional
    col_name: Optional[str]  # Make this optional
    orig_table_string: Optional[str]
    table: Optional[str]


def process_table_name(table_name: Optional[str]) -> Optional[str]:
    """Process the table name to remove surrounding single quotes if present."""
    if table_name and table_name.startswith("'") and table_name.endswith("'"):
        return table_name[1:-1]  # Remove quotes
    return table_name  # Return as is if not quoted


def column_from_texts(*, col_text: str, table_text: Optional[str]):
    processed_table_text = process_table_name(table_text)  # Process the table name
    return ColumnOrMeasure(
        orig_string=col_text,
        col_name=col_text[1:-1].replace("]]", "]"),
        orig_table_string=table_text,
        table=processed_table_text.replace("''", "'") if processed_table_text else None,
    )


def get_columns_or_measures(dax: str) -> list[ColumnOrMeasure]:
    input_stream = InputStream(dax)
    lexer = DAXLexer(input_stream)
    tokens = lexer.getAllTokens()
    ls: list[ColumnOrMeasure] = list()
    table_text: Optional[str] = None
    has_column_or_measure = False

    for i, tk in enumerate(tokens):
        if tk.type == DAXLexer.TABLE:
            table_text = tk.text
        elif tk.type == DAXLexer.TABLE_OR_VARIABLE:
            table_text = tk.text
            # Check if the next token is not a COLUMN_OR_MEASURE
            if i + 1 >= len(tokens) or tokens[i + 1].type != DAXLexer.COLUMN_OR_MEASURE:
                ls.append(
                    ColumnOrMeasure(
                        orig_string=None,
                        col_name=None,
                        orig_table_string=table_text,
                        table=process_table_name(table_text),
                    )
                )
                table_text = None
        elif tk.type == DAXLexer.COLUMN_OR_MEASURE:
            ls.append(column_from_texts(col_text=tk.text, table_text=table_text))
            table_text = None
            has_column_or_measure = True
        elif tk.type in [DAXLexer.OPEN_PARENS, DAXLexer.CLOSE_PARENS]:
            continue
        else:
            table_text = None
            has_column_or_measure = False

    return ls
