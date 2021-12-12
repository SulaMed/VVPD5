from op4.late_list import late_list
import pytest


@pytest.mark.parametrize("x,y,z", [({'Ernar': '09-11-2011'}, '12-11-2011', ['Ernar']),
                                   ({'Ernur': '21-11-2011'}, '12-11-2012', []),
                                   ({'Veronika': '11-12-2012'}, '11-12-2012', ['Veronika'])])
def test_list(x, y, z):
    assert late_list(x, y) == z


def test_error():
    with pytest.raises(AttributeError):
        assert late_list('11-11-2011', '11-11-2011')


def test_error_2():
    with pytest.raises(AttributeError):
        assert late_list('11.11.2011', '12.11.2012')
