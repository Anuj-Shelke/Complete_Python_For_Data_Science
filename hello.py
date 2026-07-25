#Write a program to print multiplication table from 2 to 20 and store it in different files place this foler in files 

def table_writer(n):
    table =""
    for i in range(1,11):
        table +=(f"{i}X{n} = {i*n}\n")

    with open(f"table/table_{n}", "w") as f:
        f.write(table)



for i in range(1,21):
    table_writer(i)






    


