from utils import factorial, is_pow_2

if __name__ == '__main__':
	n = int(input("Введіть число: "))
	print(f"\nФакторіал {n} = {factorial(n)}\n")
	print(f"{n} is {"not "*not(is_pow_2(n))}of 2")
