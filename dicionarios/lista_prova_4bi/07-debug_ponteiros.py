def modificar_valor(valor):
    print("Dentro da função (antes da modificação):", valor)
    print("ID do objeto (antes da modificação):", id(valor))

    valor += 10

    print("Dentro da função (após a modificação):", valor)
    print("ID do objeto (após a modificação):", id(valor))


numero = 5

print("Antes da chamada da função:")
print("Valor:", numero)
print("ID do objeto:", id(numero))

modificar_valor(numero)

print("\nDepois da chamada da função:")
print("Valor:", numero)
print("ID do objeto:", id(numero))


# O que é impresso antes e depois da chamada da função modificar_valor no código principal?

# r: a mesma coisa duas vezes, não há alteração nos prints.


# Explique por que, após a chamada da função, o valor de numero no código principal
# permanece inalterado, mesmo que a função tenha modificado o valor dentro dela.

# r: porque o parâmetro utilizado dentro da função não é o mesmo item do código principal (têm IDs diferentes)


# Qual é a função da função id() no contexto deste exemplo?

# r: mostrar que tipos imutáveis (nesse caso, o int) não mantêm o mesmo endereço de memória ao serem alterados,
#    e que parâmetros não têm o mesmo ID de seus correspondentes fora da função


# O que podemos concluir sobre objetos imutáveis em Python com base nos resultados observados?

# r: que tipos imutáveis não podem ser modificados, então, ao mudar o valor de um int, na verdade um novo objeto int
#    está sendo criado, com um novo endereço de memória