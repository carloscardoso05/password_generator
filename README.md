[Português](#Gerador-de-senha-em-Python)

[English](#Password-generator-in-Python)

# Gerador de senha em Python
1. Primeiro definimos quais tipos de caracteres (maiúsculos, minúsculos, números e caracteres especiais) o usuário deseja ter na senha e seu tamanho.
2. Em seguida, criamos uma string que contém todos esses caracteres.
  - Ex.: o usuário deseja letras maiúsculas e números, então será criada a seguinte string, "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".
3. Em seguida, uma string vazia é criada, que será nossa senha.
4. Por fim, vamos iterar sobre a string de caracteres ("ABC...789") um número de vezes igual ao tamanho definido e adicionar um caractere aleatório à string da nossa senha, 
usando a função choise() da biblioteca "Random" do Python (random.choice()).

# Password generator in Python
1. First we define wich types of characters (uppercase, lowercase, numbers and special characters) the user wants in the password and it's length.
2. Then we create a string that contains all of these characters.
    - E.g.: the user wants uppercases and numbers, so it'll be created the following string, "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".
3. Then a empty string is created, which will be our password.
4. Finally, we're going to iterate over the character string ("ABC...789") a number of times equals to the defined length and add a random character to our password string,
using the choise() function of the "Random" python library (random.choice()).
