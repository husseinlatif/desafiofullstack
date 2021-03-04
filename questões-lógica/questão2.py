bracketSequence = input("Digite a sequência de brackets:")

    ###Função recursiva que define se dada sequência de brackets é balanceada ou não.
    ###Seu funcionamento consiste em tratar a sequência como uma pilha, de maneira a buscar o primeiro fechamento de bracket '), ] ou }'.
    ###Caso o elemento anterior ao primeiro fechamento de bracket seja correspondente a seu par balanceado, a sub-string balanceada é retirada da pilha.
    ###Após isto, o passo recursivo é executado até que não hajam mais elementos na pilha, ou seja encontrado um desbalanceamento.

def isBalanced(sequence):
    ###Caso o número de elementos na string seja ímpar, a mesma NÃO é balanceada.
    if (len(sequence)%2 != 0): return 'NÃO'

    ###Busca pelo primeiro fechamento de bracket na pilha.
    for i in range(len(sequence)):
        if (sequence[i] == ']'):
            if sequence[i-1] == '[':
                sequence = sequence[:i-1] + sequence[i+1:]
                return isBalanced(sequence)
            else: return 'NÃO'

        elif(sequence[i] == ')'):
            if sequence[i-1] == '(':
                sequence = sequence[:i-1] + sequence[i+1:]
                return isBalanced(sequence)
            else: return 'NÃO'

        elif(sequence[i] == '}'):
            if sequence[i-1] == '{':
                sequence = sequence[:i-1] + sequence[i+1:]
                return isBalanced(sequence)
            else: return 'NÃO'
    
    return 'SIM'

print(isBalanced(bracketSequence))