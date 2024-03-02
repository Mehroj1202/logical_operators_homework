def main(a):
    """Given a five-digit integer a, check the following statement "All digits of the number are in descending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a//100000>a//1000%10>a//100%100%10>a//10%10>a%10
print(main(54321))