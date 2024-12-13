#!/usr/bin/python3
def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Parameters:
    x (int): Number of rounds.
    nums (list): List of integers representing the upper limit of the range for each round.

    Returns:
    str: Name of the player who won the most rounds ("Maria" or "Ben").
         Returns None if there is no clear winner.
    """
    def is_prime(num):
        """
        Checks if a number is prime.

        Parameters:
        num (int): The number to check.

        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime_count(n):
        """
        Counts the number of prime numbers up to n using the Sieve of Eratosthenes.

        Parameters:
        n (int): The upper limit of the range to check for prime numbers.

        Returns:
        int: The count of prime numbers up to n.
        """
        primes = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return sum(primes[2:])

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count(n) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

