# G. verbing
# Dada uma string, caso seu comprimento seja pelo menos 3,
# adiciona 'ing' no final
# Caso a string já termine em 'ing', acrescentará 'ly'.
# dica use s.endswith('ing')
def verbing(s):
    if len(s) <= 3:
        return s
    elif s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'


# H. not_bad
# Dada uma string, procura a primeira ocorrência de 'not' e 'bad'
# Se 'bad' aparece depois de 'not' troca 'not' ... 'bad' por 'good'
# Assim 'This dinner is not that bad!' retorna 'This dinner is good!'
# dica use s.find('not') e s.find('bad') para ver
# as posições 
def not_bad(s):
  no = s.find('not')
  bad = s.find('bad')
  if bad < no:
      return s
  else:
      return s.replace(s[no:],'good!')


# I. inicio_final
# Divida cada string em dois pedaços.
# Se a string tiver um número ímpar de caracteres
# o primeiro pedaço terá um caracter a mais,
# Exemplo: 'abcde', divide-se em 'abc' e 'de'.
# Dadas 2 strings, a e b, retorna a string
# a_inicio + b_inicio + a_final + b_final
def inicio_final(a, b):
    a_inicio = ''
    b_inicio = ''
    a_final = ''
    b_final = ''
    qt = len(a)//2
    if len(a) % 2 == 0:
      a_inicio = a[:qt]
      a_final = a[qt:]
    else:
      a_inicio = a[:qt+1]
      a_final = a[qt+1:]
    qt = len(b) // 2
    if len(b) % 2 == 0:
      b_inicio = b[:qt]
      b_final = b[qt:]
    else:
      b_inicio = b[:qt+1]
      b_final = b[qt+1:]
    return a_inicio + b_inicio + a_final + b_final


# J. zeros finais
# Verifique quantos zeros há no final de um número inteiro positivo
# Exemplo: 10010 tem 1 zero no fim e 908007000 possui três
# dica transforme para texto e inverta
# n = str(n)
# n = n[::-1]
def zf(n):
    cont = 0
    n = str(n)
    n = n[::-1]
    for k in n:
        if k == '0':
            cont += 1
        else:
            break
    return cont
        

# K. conta 2
# Verifique quantas vezes o dígito 2 aparece entre 0 e n-1
# Exemplo: para n = 20 o dígito 2 aparece duas vezes entre 0 e 19
def conta2(n):
    cont = 0
    for k in range(n-1):
        cont += str(k).count('2')
    return cont


# L. inicio em potencia de 2
# Dado um número inteiro positivo n retorne a primeira potência de 2
# que tenha o início igual a n
# Exemplo: para n = 65 retornará 16 pois 2**16 = 65536
# dica transforme para texto a potencia de 2
# e use .starswith(str(n))
def inip2(n):
    k = 0
    while k > -1:
        if str(2**k).startswith(str(n)):
            break
        else:
            k += 1
    return k


def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))


def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')


  print ()
  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good!')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")


  print ()
  print ('inicio_final')
  test(inicio_final('abcd', 'xy'), 'abxcdy')
  test(inicio_final('abcde', 'xyz'), 'abcxydez')
  test(inicio_final('Kitten', 'Donut'), 'KitDontenut')


  print ()
  print ('zeros finais')
  test(zf(10100100010000), 4)
  test(zf(90000000000000000010), 1)


  print ()
  print ('conta 2')
  test(conta2(20), 2)
  test(conta2(999), 300)
  test(conta2(555), 216)


  print ()
  print ('inicio p2')
  test(inip2(7), 46)
  test(inip2(133), 316)
  test(inip2(1024), 10)
  
if __name__ == '__main__':
  main()