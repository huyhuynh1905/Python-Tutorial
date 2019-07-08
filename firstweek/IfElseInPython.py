dtb = float(input("Nhập điểm trung bình của bạn: "))
if dtb<4:
    print("Bạn rớt môn!")
print("If...Elif...Else:")
if dtb>=4 and dtb<=6.5:
    pass #dùng pass để tránh lỗi và ghi nhớ bổ sung code sau
elif dtb>6.5 and dtb<8.5:
    print("Điểm khá")
elif dtb>=9.5:
    print("Điểm giỏi!")

print("m = 5" if 5!=4 else "m = 6")
