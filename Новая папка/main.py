from libree_html import prices, names

price = prices()
name = names()

while True:
    try:
        print(next(price), next(name))
    except StopIteration:
        break
