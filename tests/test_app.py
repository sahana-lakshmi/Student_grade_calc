from app import calculate_results

def test_calculate_results():
    marks = [70, 80, 90]
    res = calculate_results(marks)
    assert res["total"] == 240
    assert res["average"] == 80.0
    assert res["grade"] == 'B'
