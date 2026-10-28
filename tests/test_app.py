from app import calculate_results

def test_calculate_results():
    marks = [75, 85, 80] # Total = 240, Average = 80.0
    res = calculate_results(marks)
    assert res["total"] == 240
    assert res["average"] == 80.0
    assert res["grade"] == 'B' # Active grade verification for Push 2
