from op4.score import deadline_score
import pytest


@pytest.mark.parametrize("pass_date, deadline_date, score", [('11-11-2011', '12-11-2011', 5),
                                                             ('13-11-2012', '12-11-2012', 4),
                                                             ('21-11-2012', '11-11-2012', 3),
                                                             ('31-11-2012', '01-11-2012', 1),
                                                             ('19-11-2012', '01-11-2012', 2)])
def test_deadline_score(pass_date, deadline_date, score):
    assert deadline_score(pass_date, deadline_date) == score


def test_of_error():
    with pytest.raises(AssertionError):
        assert deadline_score('11.11.2012', '12.11.2011')

