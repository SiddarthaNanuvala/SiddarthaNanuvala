"""
Kaprekar Number Game
--------------------
A fun mathematical puzzle implemented in Python. 
Starting from a 4-digit number (with at least two different digits), this game applies the Kaprekar routine 
to reach the mysterious constant 6174.

Author: Siddartha Nanuvala
"""

def kaprekar_step(num: int) -> int:
    """Perform one step of Kaprekar's routine and return the result."""
    num_str = f"{num:04d}"  # Ensure number is 4 digits with leading zeros
    asc = int("".join(sorted(num_str)))
    desc = int("".join(sorted(num_str, reverse=True)))
    result = desc - asc
    print(f"🔄 {desc:04d} - {asc:04d} = {result:04d}")
    return result

def is_valid_input(num_str: str) -> bool:
    """Check if the input is a valid 4-digit number with at least two different digits."""
    return (
        num_str.isdigit() and
        len(num_str) == 4 and
        len(set(num_str)) > 1
    )

def run_kaprekar_routine(start_num: int) -> int:
    """Run the full Kaprekar routine starting from the given number."""
    count = 0
    current = start_num
    print("\n🧮 Starting Kaprekar Routine...\n")

    while current != 6174:
        current = kaprekar_step(current)
        count += 1
        if current == 0:
            print("⚠️ Entered a number that leads to 0000. Try a different one.")
            return count
        if count > 10:
            print("❌ Too many steps. Possibly stuck in a loop.")
            return count

    print(f"\n✅ Reached 6174 in {count} steps!")
    return count

def main():
    print("==========================================")
    print("🔢  Welcome to the Kaprekar Number Game  🔢")
    print("==========================================")
    print("Enter any 4-digit number with at least two different digits.")
    print("The game will transform it step-by-step until it reaches 6174.\n")

    user_input = input("🔹 Enter your 4-digit number: ").strip()

    if not is_valid_input(user_input):
        print("\n❌ Invalid input. Please enter a 4-digit number with at least two different digits (e.g., 3524).")
        return

    start_number = int(user_input)
    run_kaprekar_routine(start_number)

    print("\n🎉 Thanks for playing the Kaprekar Number Game!\n")

if __name__ == "__main__":
    main()
