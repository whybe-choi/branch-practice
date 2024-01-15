from random import randint

def get_luckies() -> list:
	return [randint(1, 45+1) for _ in range(6)]


if __name__ == '__main__':
	print(get_luckies())
