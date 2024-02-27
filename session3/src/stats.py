def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_std(numbers):
    mean = calculate_mean(numbers)
    variance = sum([(x - mean) ** 2 for x in numbers]) / len(numbers)
    return variance ** 0.5

def calculate_median(numbers):
    numbers.sort()
    mid = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]
