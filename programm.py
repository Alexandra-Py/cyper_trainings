import pickle

with open("text.txt", encoding="utf-8") as file_in:
    with open("out_text.txt", "w", encoding="utf-8") as file_out:
        for line in file_in:
            file_out.write(line.strip()+"\n")
            print(line.strip())

num=int(input("Введите числовой ключ:"))
with open("key.bin","wb") as key:
    pickle.dump(num,key)

with open("key.bin","rb") as bit_file:
    NK=pickle.load(bit_file)
print("Считан ключ из файла:", NK)



