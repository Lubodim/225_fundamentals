def stepen(numb, expo):
    powers = numb ** expo
    return powers


number, exponent = list(map(int, input().split(', ')))
power = stepen(number, exponent)
print(f"{number} to the power {exponent} is {power}")
