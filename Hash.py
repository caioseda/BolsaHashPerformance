#Código inspirado no vídeo https://www.youtube.com/watch?v=zHi5v78W1f0
CAPACIDADE_TOTAL=10

class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.prox= None

class HashTable:
    def __init__(self):
        self.capacidade= CAPACIDADE_TOTAL
        self.size = 0
        self.linha = [None] * self.capacidade

    def hashIndex(self, chave):
        i = hash(chave)
        index = i % self.capacidade
        return index
        
    def insere(self, chave, valor):
        self.size += 1
        index = self.hashIndex(chave)
        no = self.linha[index]
        if no is None:
            self.linha[index]= No(chave, valor)
            return
        prev = no
        while no is not None:
            prev = no
            no = no.prox
        prev.prox = No(chave, valor)

    def procura(self,chave):
        index = self.hashIndex(chave)
        no = self.linha[index]
        while no is not None and no.chave != chave:
            no = no.prox
        if no is None:
            return None
        return no.valor

    def remove(self,chave):
        index = self.hashIndex(chave)
        no = self.linha[index]
        while no is not None and no.chave != chave:
            prev = no
            no = no.prox
        if no is None:
            return None
        else:
            self.size -= 1
            result = no.valor
            if prev is None:
                no = None
            else:
                prev.prox = prev.prox.prox
            return result
            
    def show(self):
        for x in self.linha:
            if x is None:
                print(".")
            else:
                no = x
                while no is not None:
                    print(no.chave,end='-> ')
                    no = no.prox
                print(" ")

if __name__ == "__main__":
    
    a = HashTable()
    a.insere("Caio","Seda")
    a.insere("Caio",15)
    a.insere("leticia","Bit")
    a.insere("le","Bittenc")
    a.show()