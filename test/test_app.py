from app import calculate_results

def test_calculate_results():
    marks = [80, 90, 70]
    res = calculate_results(marks)
    assert res["total"] == 240
    assert res["average"] == 80.0
    
