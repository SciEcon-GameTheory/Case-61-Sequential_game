class sequential:
    def __init__(self, utility, rate, beta, number):
        self.utility = utility
        self.rate = rate
        self.beta = beta
        self.number = number

    def generate_NE(self):
        comparison = self.rate * self.number / self.beta
        if self.utility > comparison:
            print("The nash equilibrium equals to 1, which means agent 0 buys strictly more than"
                  "half of the coins and kills CC.")
        elif self.utility < comparison:
            print("The nash equilibrium equals to 1, which means agent 0 will have no incentive to"
                  "cross the 50% threshold.")

if __name__ == "__main__":
    utility = input("Please enter the utility: ")
    rate = input("Please enter the monetary interest rate: ")
    beta = input("Please enter the time discount factor: ")
    number = input("Please enter the number of the total agents: ")
    game = sequential(utility=utility, rate=rate, beta=beta, number=number)
    game.generate_NE()