def maximumWealth():
    accounts = input("Give me a list of lists: ")
    print(accounts)
    moneySum = []
    money = 0
    for account in list(accounts):
        for wealth in list(account):
            money += wealth
        moneySum.append(money)
        money -= money

        print(max(moneySum) + "is the maximum wealth.")

class Solution:
    maximumWealth()