#!/usr/bin/env python3

class CashRegister:
  
  total = 0
  def __init__(self, discount=0):
    self.discount = discount
    self.items = []
    self.last_transaction = []

  def add_item(self, item, price, quantity = 1):
    self.total += (price * quantity)
    for x in range(quantity):
      self.items.append(item)
    self.last_transaction = [item, price, quantity]

  def apply_discount(self):
    if self.discount == 0:
      print('There is no discount to apply.')
    else:
      self.total = self.total - (self.total * (self.discount / 100))
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    self.total = self.total - (self.last_transaction[1] * self.last_transaction[2])
    self.items.pop()