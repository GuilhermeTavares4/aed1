def add_medals(medals: dict, country, value):
    if not country in medals:
        medal_info = {value: 1}
        medals[country] = medal_info
    else:
        if not value in medals[country]:
            medals[country][value] = 1
        else:
            medals[country][value] += 1

def medals_report(medals: dict):
    report = 'Relatório de medalhas:\n'
    for country, medal_info in medals.items():
        report += f'{country}:\n'
        for medal_type, quantity in medal_info.items():
            report += f'    {medal_type}: {quantity}\n'
        report += '\n'
    return report


def main():
    medals = {}
    for i in range(10):
        add_medals(medals, 'BRAZILLLLLL', 'OURO PORRAAAAAAA')

    for i in range(5):
        add_medals(medals, 'BRAZILLLLLL', 'PRATA')

    add_medals(medals, 'Argentina', 'bronze')
    add_medals(medals, 'BRAZILLLLLL', 'OURO PORRAAAAAAA')

    print(medals_report(medals))

main()