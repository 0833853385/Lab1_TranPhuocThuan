def kiem_tra_so_chan(so):
    if so % 2 == 0:
        return True
    else:
        return False

def main():
    so = int(input("Nhập một số nguyên: "))
    if kiem_tra_so_chan(so):
        print(f"{so} là số chẵn.")
    else:
        print(f"{so} không phải là số chẵn.")

if __name__ == "__main__":
    main()
