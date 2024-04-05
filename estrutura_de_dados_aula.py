valores = [2,3,8,6,5,1,9,7]
def selection (lista):
  i = 0
  while (i<len(lista)-1):
    minimo = lista[i]
    ind_minimo = i
    #calcula quem é o mínimo na região de i até o fim da lista
    for j in range (i+1, len(lista)):
      if (lista[j] < minimo):
       minimo = lista[j]
       ind_minimo = j
    lista[ind_minimo] = lista[i]
    lista[i] = minimo
    i += 1
  return lista

selection(valores)
print(valores)


# Criar uma Classe tipo Pilha
class Pilha:
  def __init__(self):
    self.pilha = []
    self.tamanho = 0

  def insere(self,novo):
    self.pilha.append(novo)
    self.tamanho += 1
  
  def remove(self):
    self.tamanho -= 1
    return self.pilha.pop()

  def topo(self):
    return self.pilha[-1]

  def __len__(self):
    return self.tamanho

p=Pilha()
p.insere(101)
p.insere(102)
p.insere(103)
print(p.remove())