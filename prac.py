def write_document():
    with open('data.txt', 'rt', encoding='UTF8') as file:
        data = file.readline()
        with open('data2.txt','w', encoding='UTF8') as file2:
            while data:            
                if(data[0].isalpha()):
                    file2.write(data)
                elif(data[0]=='-'):
                    file2.write(data)
                elif(data[0]=='"'):
                    file2.write(data)

                data = file.readline()

if __name__ == "__main__":
    write_document()