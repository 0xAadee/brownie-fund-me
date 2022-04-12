from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"Current Entrance Fee: {entrance_fee}")
    print("Funding...")
    # The entranceFee function is a bit broken so give it the power of 2 to make it work properly
    fund_me.fund({"from": account, "value": entrance_fee**2})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()