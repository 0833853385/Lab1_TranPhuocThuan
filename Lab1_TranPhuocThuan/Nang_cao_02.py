def tinh_tong_so(chuoi):
    so_nguyen_duong = 0
    so_nguyen_am = 0
    so_tam = ''

    for ky_tu in chuoi:
        if ky_tu.isdigit():
            so_tam += ky_tu
        elif ky_tu == '-' and so_tam == '':
            so_tam += ky_tu
        else:
            if so_tam:
                so = int(so_tam)
                if so > 0:
                    so_nguyen_duong += so
                elif so < 0:
                    so_nguyen_am += so
                so_tam = ''

    return so_nguyen_duong, so_nguyen_am

chuoi = "-100#^sdfkj8902w3ir021@swf-20"

tong_nguyen_duong, tong_nguyen_am = tinh_tong_so(chuoi)

print("Giá trị dương:", tong_nguyen_duong)
print("Giá trị âm:", tong_nguyen_am)
