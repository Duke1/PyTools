#! python3
# coding=utf-8

__author__ = 'Duke'

import getopt
import sys

import os

from decimal import Decimal


class MonthRepayment:
    # 本息和
    principalAndInterest = 0.0
    # 每月利息
    interestAmount = 0.0
    # 月本金
    principalAmount = 0.0
    # 剩余本金
    remaining = 0.0

    def toString(self):
        return "月还款：%f ， 本金：%f ， 利息：%f ， 剩余本金：%f" % (
            self.principalAndInterest, self.principalAmount, self.interestAmount, self.remaining)


# 贷款本金，是当前剩余未还本金，不是贷款总额
# 利率，为当前银行利率，不是贷款签约时的利率
# 还款月数，为剩下未还期数，不是总贷款期数
class CalcFactor:
    # 贷款期数（单位：月）
    period = 0.0
    # 贷款金额（单位：CNY元）
    amount = 0.0
    # 利率（年化利率.例如：4.8%--0.048）
    interestRate = 0.0

    def getMonthInterestRate(self):
        return self.interestRate / 12.0


class LoanCalculator:

    def __init__(self):
        print("__init__")

    @staticmethod
    def create():
        return LoanCalculator()

    # 等额本息计算公式：〔贷款本金×月利率×（1＋月利率）＾还款月数〕÷〔（1＋月利率）＾还款月数－1〕
    def calcEqualInstallments(self, calcFactor):
        monthRepayment = MonthRepayment()
        # 月利率
        monthInterestRate = calcFactor.getMonthInterestRate()
        # 月还款本息
        monthRepayment.principalAndInterest = (calcFactor.amount * monthInterestRate * pow((1 + monthInterestRate),
                                                                                           calcFactor.period)) / \
                                              (pow((1 + monthInterestRate), calcFactor.period) - 1)

        # 每月利息
        monthRepayment.interestAmount = calcFactor.amount * monthInterestRate
        # 月本金
        monthRepayment.principalAmount = monthRepayment.principalAndInterest - monthRepayment.interestAmount
        # monthPrice = (Decimal(principalAndInterest).quantize(Decimal('0.00')))
        return monthRepayment

    def calcEqualInstallmentsPlan(self, calcFactor):
        list = []
        while calcFactor.period >= 1:
            monthRepayment = self.calcEqualInstallments(calcFactor)
            monthRepayment.remaining = calcFactor.amount - monthRepayment.principalAmount
            list.append(monthRepayment)
            calcFactor.amount = monthRepayment.remaining
            calcFactor.period -= 1
        return list

    # 等额本金计算公式：每月还款金额=（贷款本金÷还款月数）+（本金—已归还本金累计额）×每月利率
    def calcEqualInstallmentsOfPrincipal(self, calcFactor):
        monthRepayment = MonthRepayment()
        # 月利率
        monthInterestRate = calcFactor.getMonthInterestRate()
        # 每月利息
        monthRepayment.interestAmount = calcFactor.amount * monthInterestRate
        # 月本金
        monthRepayment.principalAmount = calcFactor.amount / calcFactor.period
        # 月还款本息
        monthRepayment.principalAndInterest = monthRepayment.principalAmount + monthRepayment.interestAmount

        return monthRepayment

    def calcEqualInstallmentsOfPrincipalPlan(self, calcFactor):
        list = []
        while calcFactor.period >= 1:
            monthRepayment = self.calcEqualInstallmentsOfPrincipal(calcFactor)
            monthRepayment.remaining = calcFactor.amount - monthRepayment.principalAmount
            list.append(monthRepayment)
            calcFactor.amount = monthRepayment.remaining
            calcFactor.period -= 1
        return list


def main():
    calcFactor = CalcFactor()
    calcFactor.period = float(input('贷款期数（单位：月）: '))
    calcFactor.amount = float(input('贷款金额（单位：CNY元）: '))
    calcFactor.interestRate = float(input('利率（年化利率.例如：4.8%--0.048）: '))
    type = int(input('选择类型（1、等额本息；2、等额本金）: '))

    loanCalculator = LoanCalculator.create()
    list = []
    if 1 == type:
        list = loanCalculator.calcEqualInstallmentsPlan(calcFactor)
    elif 2 == type:
        list = loanCalculator.calcEqualInstallmentsOfPrincipalPlan(calcFactor)

    for rp in list:
        print(rp.toString())
    print('\r\nComplete~~~')


if __name__ == "__main__":
    main()
