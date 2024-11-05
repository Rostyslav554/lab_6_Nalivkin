def is_a_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

print(is_a_triangle(3, 4, 5))
print(is_a_triangle(1, 10, 12))

