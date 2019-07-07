#Código inspirado no vídeo https://www.youtube.com/watch?v=zHi5v78W1f0
CAPACIDADE_TOTAL=100



class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.prox= None

class HashTable:                             #chave:valor chave:valor
    def __init__(self,NomeArq):
        self.capacidade= CAPACIDADE_TOTAL
        self.size = 0
        self.nome = NomeArq
        self.arq = open(NomeArq,"w+")
        
        numIndex = 0
        while numIndex < self.capacidade:
            line= str(numIndex) + " \n"
            self.arq.write(line)
            numIndex +=1

        self.arq.close()

    def hashIndex(self, chave):
        i = hash(chave)
        index = i % self.capacidade
        return index

    def insere(self, chave, valor):
        self.size += 1
        index = 2
        #index = self.hashIndex(chave)
        f=open(self.nome,"r+")
        line = f.readline()
        tam=len(line)
        print(tam)
        while tam != 0:
            x = line.split(" ")
            if x[0] == str(index): 
                for elemento in x:
                    if elemento != "\n":
                        f.write("{} ".format(elemento))
                        f.truncate()
                
                f.write("{}:{}".format(str(chave),str(valor)))
            line = f.readline()
            tam=len(line)
        f.close()
        
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
    
    a = HashTable("teste.txt")
    a.insere("Caio","teste")