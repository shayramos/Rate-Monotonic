def main():
    f = open("archiveProcess.txt", 'r')
    if not f:
        print("O arquivo está vazio!")
    else:
        print("encontrei o arquivo")
    f.close()
