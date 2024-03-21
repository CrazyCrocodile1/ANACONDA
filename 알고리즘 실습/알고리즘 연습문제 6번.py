def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def test_gcd():
    assert gcd(60, 28) == 4
    print("테스트 통과!")

if __name__ == "__main__":
    test_gcd()
