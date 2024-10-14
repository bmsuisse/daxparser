from daxparser import get_columns_or_measures


def test_dax_expression_1():
    dax = " IF(COUNTROWS(VALUES('Dimension'[Metric Scale]))=1,VALUES('Dimension'[Metric Scale Rate]),1)"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 2
    assert c_m[0].table == "Dimension"
    assert c_m[0].col_name == "Metric Scale"
    assert c_m[1].table == "Dimension"
    assert c_m[1].col_name == "Metric Scale Rate"


def test_dax_expression_2():
    dax = " IF(COUNTROWS(VALUES(Dimension[Metric Scale]))=1,VALUES(Dimension[Metric Scale Rate]),1)"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 2
    assert c_m[0].table == "Dimension"
    assert c_m[0].col_name == "Metric Scale"
    assert c_m[1].table == "Dimension"
    assert c_m[1].col_name == "Metric Scale Rate"


def test_dax_expression_3():
    dax = "CALCULATE(DISTINCTCOUNT('Fact Table'[Entity ID]), 'Fact Table'[Category] = \"Type A\")"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 2
    assert c_m[0].table == "Fact Table"
    assert c_m[0].col_name == "Entity ID"
    assert c_m[1].table == "Fact Table"
    assert c_m[1].col_name == "Category"


def test_dax_expression_4():
    dax = "CALCULATE(DISTINCTCOUNT('Fact Table'[Entity ID]), 'Fact Table'[Category] = \"Type B\")"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 2
    assert c_m[0].table == "Fact Table"
    assert c_m[0].col_name == "Entity ID"
    assert c_m[1].table == "Fact Table"
    assert c_m[1].col_name == "Category"


def test_dax_expression_5():
    dax = "CALCULATE(DISTINCTCOUNT('Fact Table'[User_Identifier]), 'Fact Table'[Category]=\"Type A\")"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 2
    assert c_m[0].table == "Fact Table"
    assert c_m[0].col_name == "User_Identifier"
    assert c_m[1].table == "Fact Table"
    assert c_m[1].col_name == "Category"


def test_dax_expression_6():
    dax = "CALCULATE(DISTINCTCOUNT('Fact Table'[User_Identifier]), 'Fact Table'[Category]=\"Type B\")"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 2
    assert c_m[0].table == "Fact Table"
    assert c_m[0].col_name == "User_Identifier"
    assert c_m[1].table == "Fact Table"
    assert c_m[1].col_name == "Category"


def test_dax_expression_7():
    dax = "CONCATENATEX(DISTINCT(Dimension[Control ID]), Dimension[Control ID], UNICHAR(10))"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 2
    assert c_m[0].table == "Dimension"
    assert c_m[0].col_name == "Control ID"
    assert c_m[1].table == "Dimension"
    assert c_m[1].col_name == "Control ID"


def test_dax_expression_8():
    dax = "COUNT(FactA[Identifier_A])"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 1
    assert c_m[0].table == "FactA"
    assert c_m[0].col_name == "Identifier_A"


def test_dax_expression_9():
    dax = "COUNT(FactB[Entity_ID])"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 1
    assert c_m[0].table == "FactB"
    assert c_m[0].col_name == "Entity_ID"


def test_dax_expression_10():
    dax = "COUNT(DimC[Unique_Identifier])"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 1
    assert c_m[0].table == "DimC"
    assert c_m[0].col_name == "Unique_Identifier"


def test_dax_expression_11():
    dax = "COUNTROWS(DimA)"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 1
    assert c_m[0].table == "DimA"
    assert c_m[0].col_name is None


def test_dax_expression_12():
    dax = "COUNTROWS(fact_time)"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 1
    assert c_m[0].table == "fact_time"
    assert c_m[0].col_name is None


def test_dax_expression_13():
    dax = "COUNTROWS(Fact_Usage)"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 1
    assert c_m[0].table == "Fact_Usage"
    assert c_m[0].col_name is None


def test_dax_expression_14():
    dax = "COUNTROWS(DimB)"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 1
    assert c_m[0].table == "DimB"
    assert c_m[0].col_name is None


def test_dax_expression_15():
    dax = "DISTINCTCOUNT(FactB[Entity_ID])"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 1
    assert c_m[0].table == "FactB"
    assert c_m[0].col_name == "Entity_ID"


def test_dax_expression_16():
    dax = "DISTINCTCOUNT('Fact_Historical'[Entity_ID])"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 1
    assert c_m[0].table == "Fact_Historical"
    assert c_m[0].col_name == "Entity_ID"


def test_dax_expression_17():
    dax = "DISTINCTCOUNT(Fact_Current[Entity_ID])"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 1
    assert c_m[0].table == "Fact_Current"
    assert c_m[0].col_name == "Entity_ID"


def test_dax_expression_18():
    dax = "DISTINCTCOUNT(Fact_Current[Entity_ID])+0"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 1
    assert c_m[0].table == "Fact_Current"
    assert c_m[0].col_name == "Entity_ID"


def test_dax_expression_19():
    dax = "DISTINCTCOUNT(Fact_Usage[ID])"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 1
    assert c_m[0].table == "Fact_Usage"
    assert c_m[0].col_name == "ID"


def test_dax_expression_20():
    dax = "DISTINCTCOUNT('Fact Table'[Event ID]) & \" Events Open\""
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 1
    assert c_m[0].table == "Fact Table"
    assert c_m[0].col_name == "Event ID"


def test_dax_expression_21():
    dax = "DIVIDE([Metric1-Compliant],[Metric1-Count])"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 2
    assert c_m[0].table is None
    assert c_m[0].col_name == "Metric1-Compliant"
    assert c_m[1].table is None
    assert c_m[1].col_name == "Metric1-Count"


def test_dax_expression_22():
    dax = 'DIVIDE([Metric1-Compliant],[Metric1-Count],"-")'
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 2
    assert c_m[0].table is None
    assert c_m[0].col_name == "Metric1-Compliant"
    assert c_m[1].table is None
    assert c_m[1].col_name == "Metric1-Count"


def test_dax_expression_23():
    dax = 'DIVIDE([Metric1-NonCompliant],[Metric1-Count],"-")'
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 2
    assert c_m[0].table is None
    assert c_m[0].col_name == "Metric1-NonCompliant"
    assert c_m[1].table is None
    assert c_m[1].col_name == "Metric1-Count"


def test_dax_expression_24():
    dax = 'DIVIDE([Metric1-NonCompliant],[Metric1-Count],"0")'
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 2
    assert c_m[0].table is None
    assert c_m[0].col_name == "Metric1-NonCompliant"
    assert c_m[1].table is None
    assert c_m[1].col_name == "Metric1-Count"


def test_dax_expression_25():
    dax = "DIVIDE([Metric2-Compliant],[Metric2-Count])"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 2
    assert c_m[0].table is None
    assert c_m[0].col_name == "Metric2-Compliant"
    assert c_m[1].table is None
    assert c_m[1].col_name == "Metric2-Count"


def test_lexer():
    dax = " IF(COUNTROWS(VALUES('Scale'[Amount Scale]))=1,VALUES('Scale'[Amount Scale Rate]),1)"
    c_m = get_columns_or_measures(dax)
    assert len(c_m) == 2
    assert c_m[0].table == "Scale"
    assert c_m[0].col_name == "Amount Scale"
    assert c_m[1].table == "Scale"
    assert c_m[1].col_name == "Amount Scale Rate"
