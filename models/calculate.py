from random import randint

class Calculate: 

    def __init__(self: object, difficulty: int, /) -> None:
        self.__difficulty: int = difficulty
        self.__value1: int = self._generate_value
        self.__value2: int = self._generate_value
        self.__operator: int = randint(1,3)
        self.__result: int = self._generate_result

    @property
    def difficulty(self: object) -> int: 
        return self.__difficulty

    @property
    def value1(self: object) -> int:
        return self.__value1

    @property
    def value2(self: object) -> int:
        return self.__value2

    @property
    def operator(self: object) -> int:
        return self.__operator

    @property
    def result(self: object) -> int: 
        return self.__result

    def __str__(self: object) -> str:
        op: str = ''

        if self.operator == 1: 
            op = 'Somar'

        elif self.operator == 2:
            op = 'Subtrair'

        elif self.operator == 3: 
            op = 'Multiplicar'

        else: 
            op = 'Operação desconhecida'
        
        return f'Valor 1:{self.value1} \nValor 2:{self.value2} \nDificuldade: {self.difficulty} \nOperação:{op}'

    @property
    def _generate_value(self: object) -> int: 
        pass

    @property
    def _generate_result(self: object) -> int:
        pass

    def check_result(self: object, response: int) -> bool:
        pass

    def show_operator(self: object) -> None: 
        pass
    