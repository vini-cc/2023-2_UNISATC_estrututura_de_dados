import numpy as np

class vetor_nao_ordenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.elementos = np.empty(self.capacidade, dtype = int)

    # Big-O: O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('Vetor vazio.')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f"{i} - {self.elementos[i]}")

    # Big-O: O(1)
    def insere(self, elemento):
        if self.ultima_posicao == self.capacidade - 1:
            print('Vetor cheio.')
        else:
            self.ultima_posicao += 1
            self.elementos[self.ultima_posicao] = elemento

    # Big-O: O(n)
    def pesquisar(self, elemento):
        for i in range(self.ultima_posicao + 1):
            if elemento == self.elementos[i]:
                return i
        return -1
    
    # Big-O: O(n)
    def excluir(self, elemento):
        posicao = self.pesquisar(elemento)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.elementos[i] = self.elementos[i + 1]
            
            self.ultima_posicao -= 1

vetor = vetor_nao_ordenado(5)

vetor.insere(5)
vetor.insere(6)
vetor.insere(1)
vetor.insere(3)
vetor.insere(9)

vetor.imprime()

vetor.pesquisar(5)

vetor.excluir(5)

vetor.imprime()
