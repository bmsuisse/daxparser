from daxparser import get_columns_or_measures, ColumnOrMeasure
from daxparser.api import column_from_texts

def test_lexer():
    dax = " IF(COUNTROWS(VALUES('Scale'[Amount Scale]))=1,VALUES('Scale'[Amount Scale Rate]),1)"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 2
    assert c_m[0].table == 'Scale'
    assert c_m[0].col_name == 'Amount Scale'
    assert c_m[1].table == 'Scale'
    assert c_m[1].col_name == 'Amount Scale Rate'