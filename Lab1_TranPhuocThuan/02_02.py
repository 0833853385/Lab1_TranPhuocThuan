def tinh_dien_tich_hinh_tron(ban_kinh):
    pi = 3.14
    dien_tich = pi * (ban_kinh ** 2)
    return dien_tich

def main():
    ban_kinh = float(input("Nhập bán kính của hình tròn: "))
    dien_tich = tinh_dien_tich_hinh_tron(ban_kinh)
    print("Diện tích của hình tròn là:", dien_tich)

if __name__ == "__main__":
    main()
