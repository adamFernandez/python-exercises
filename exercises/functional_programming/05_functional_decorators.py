def functional_decorator(func):
  def wrapper(*args):
    print(f"function: {func.__name__}")
    print(f"arguments: {args}")
    result=func(*args)

    print(f"function: {func.__name__}")
    print(f"arguments: {args}")
    return result

  return wrapper

@functional_decorator
def square(n):
  return n*n

sq_4 = square(5)
print(f"5 square: {sq_4}")