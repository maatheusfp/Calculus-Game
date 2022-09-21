from models.calculate import Calculate

def main() -> None:
    score: int = 0
    play(score)

def play(score: int) -> None:
    difficulty: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3, 4]: '))

    calc: Calculate = Calculate(difficulty)

    print('Informe o resultado para a seguinte operação: ')
    calc.show_operation()

    result: int = int(input())

    if calc.check_result(result):
        score += 1
        print(f'Você tem {score} ponto(s). ')

    continuing: int = int(input('Deseja continuar no jogo? Sim - 1 | Não - 0 '))

    if continuing: 
        play(score)
    else: 
        print(f'Você finalizou o jogo com {score} ponto(s)!')
    
if __name__ == '__main__':
    main()
