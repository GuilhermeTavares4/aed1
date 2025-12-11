def add_product(stock, product, quantity):
    if not product in stock:
        stock[product] = quantity
    else:
        stock[product] += quantity


def sell_product(stock, product, quantity):
    if not product in stock:
        print('O produto não está no estoque.')
        return
    if quantity > stock[product]:
        print('Não é possível realizar a venda por falta de estoque.')
        return
    stock[product] -= quantity


def stock_report(stock):
    report = 'Relatório de estoque:\n'
    for product, quantity in stock.items():
        report += f'{product}: {quantity}\n'
    return report


def main():
    stock = dict()
    add_product(stock, 'apple', 5)
    add_product(stock, 'banana', 10)
    sell_product(stock, 'banana', 3)
    sell_product(stock, 'apple', 6)
    report = stock_report(stock)
    print(report)


main()