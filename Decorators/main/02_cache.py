import time
from functools import cache


@cache
def count_vowels(text: str) -> int:
    vowel_count: int = 0
    # Pretend it's an expensive operations
    print(f'Bot: Counting vowels in: "{text}"...')
    time.sleep(2)

    # Count those damn vowels
    for letter in text:
        if letter in 'aeiouAEIOU':
            vowel_count += 1

    return vowel_count

def main() -> None:
    # Create a cache for the count_vowels function
    print(count_vowels('Shuxriddin'))
    print(count_vowels('Shuxriddin'))
    print(count_vowels('Muhammadali'))
    print(count_vowels.cache_info())
    count_vowels.cache_clear()
    print(count_vowels("Shuxriddin"))


if __name__ == "__main__":
    main()