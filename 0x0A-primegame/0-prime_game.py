#!/usr/bin/python3
"""
Module for prime game logic.
"""

def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the upper limit of each round.

    Returns:
        str: Name of the player with the most wins or None if it's a tie.
    """
    def sieve(n):
        """
        Generates a list of prime numbers up to n using the Sieve of Eratosthenes.

        Args:
            n (int): The upper limit for generating prime numbers.

        Returns:
            list: A list of prime numbers up to n.
        """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """
        Simulates the prime game for a given n.

        Args:
            n (int): The upper limit of the set of consecutive integers.

        Returns:
            bool: True if Maria wins, False if Ben wins.
        """
        primes = sieve(n)
        moves = 0
        while primes:
            prime = primes.pop(0)
            primes = [p for p in primes if p % prime != 0]
            moves += 1
        return moves % 2 == 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

if __name__ == "__main__":
    print("Winner: {}".format(isWinner(3, [4, 5, 1])))

