# Requisitos do Sistema Bancário

## Depósito - descrição:
### Deve receber os argumentos apenas por posição (positional only);
### Deve ser possível depositar valores positivos a conta bancária;
### Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato;

## Saque - descrição:
### Deve receber os argumentos apenas por nomes (keyword only);
### Deve ser permitido apenas 3 saques diários;
### Deve haver limite de R$ 500.00;
### Deve exibir uma mensagem quando saldo for menor que saque;
### Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato;

## Extrato - descrição:
### Deve receber os argumentos por posição e nome (positional only e keyword only);
### Deve listar todos os depósitos e saques realizados na conta;
### Deve ser exibido ao final da listagem o saldo atual da conta;
### Os valores devem ser exibidos utilizando o formato R$ xxx.xx;

## Criar usuário (cliente) - descrição:
### Deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, CPF e endereço;
### Deve ser armazenado os números do CPF;
### Deve ter CPFs únicos, ou seja, não deve haver o mesmo CPF para mais de um usuário;

## Criar conta corrente - descrição:
### Deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário;
### Deve ter somenete um usuário para uma conta;