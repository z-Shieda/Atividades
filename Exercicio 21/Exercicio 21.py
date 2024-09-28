from termcolor import colored
import subprocess
import os
nota1 = int(input("Digite a primeira nota"))
nota2 = int(input("Digite a segunda nota"))

media = nota1 + nota2 / 2

if media > 7:
  print(colored("APROVADO","green", "on_black"))
  input()
if media == 10:
  print((colored("APROVADO COM DISTINCÃO","yellow","on_black")))
  input()
if media < 7:
  print(colored("REPROVADO","red", "on_black"))
  input()