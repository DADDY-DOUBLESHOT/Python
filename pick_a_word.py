import random

file_open=open("sowpods.txt","r")
whole_words=file_open.read()
List=whole_words.split("\n")
print("\nRandom word :",random.choice(List))