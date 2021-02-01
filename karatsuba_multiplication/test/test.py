from karatsuba_multiplication.task.implementation import compute_length, karatsuba_multiplication


def test_compute_length():
    assert compute_length(1234) == 4, "Wrong length"
    assert compute_length(-1000) == 4, "Wrong length"
    assert compute_length(0) == 1, "Wrong length"
    assert compute_length(10) == 2, "Wrong length"


def test_karatsuba_multiplication():
    assert 12 * 12 == karatsuba_multiplication(12, 12)
    assert 2 * 2 == karatsuba_multiplication(2, 2)
    assert 2 * 13 == karatsuba_multiplication(2, 13)
    assert 1234 * 5678 == karatsuba_multiplication(1234, 5678)

