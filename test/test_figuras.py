from assertpy.assertpy import assert_that
from gopredict.figuras import matriz_confusion, curva_roc

def test_curva_roc(data_test_roc):
    assert_that(curva_roc(data_test_roc)).is_not_none

def test_matriz_confusion(data_test_matriz_confusion):
    assert_that(matriz_confusion(data_test_matriz_confusion)).is_not_none