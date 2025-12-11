def change_points(players, player, points):
    players[player] += points


def player_report(players):
    report = 'Relatório dos jogadores:\n'
    for player, points in players.items():
        report += f'  {player}: {points} pts\n'

    return report


def main():
    players = {
        'guilherme': 500,
        'juan': 500,
        'murillo': 500,
        'breno': 499
    }

    while True:
        player = input('Digite o nome do jogador que terá a pontuação alterada: ')

        if player == 'relatorio':
            print(player_report(players))
            continue
        
        if player == 'fim':
            break

        if not player in players:
            print('Essa pessoa não está na partida.')
            continue

        points = int(input('Digite a pontuação a ser somada: '))

        change_points(players, player, points)

    print(player_report(players))
        

main()