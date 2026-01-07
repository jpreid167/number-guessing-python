import random

def get_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        if raw.lower() in {"q", "quit", "exit"}:
            raise SystemExit
        try:
            return int(raw)
        except ValueError:
            print("Please enter a whole number (or type 'q' to quit).")

def play():
    print("=== Number Guessing Game ===")
    print("I pick a number, you guess it. Type 'q' to quit.\n")

    low = get_int("Enter the lowest number (ex: 1): ")
    high = get_int("Enter the highest number (ex: 100): ")

    if low >= high:
        print("Lowest must be less than highest. Try again.")
        return

    secret = random.randint(low, high)
    attempts = 0

    while True:
        guess = get_int(f"Guess a number between {low} and {high}: ")
        attempts += 1

        if guess < secret:
            print("Too low!\n")
        elif guess > secret:
            print("Too high!\n")
        else:
            print(f"Correct! The number was {secret}.")
            print(f"You got it in {attempts} attempt(s).")
            break

def main():
    while True:
        try:
            play()
        except SystemExit:
            print("\nGoodbye!")
            break

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
        print()

if __name__ == "__main__":
    main()
