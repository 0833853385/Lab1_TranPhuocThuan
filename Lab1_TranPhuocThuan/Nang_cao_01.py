from itertools import permutations

# Danh sách ban đầu
danh_sach = [1, 2, 3]

# Sinh ra tất cả các hoán vị
cac_hoan_vi = list(permutations(danh_sach))

# In tất cả các hoán vị
for hoan_vi in cac_hoan_vi:
    print(hoan_vi)
