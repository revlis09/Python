words=["apple", "orange", "banana", "grape", "umbrella", "kiwi","avocado","egg"]
a=[n for n in words if len(n)>=5 and n[0]=="a" or n[0]=="e" or n[0]=="i" or n[0]=="o" or n[0]=="u"]
print(a)