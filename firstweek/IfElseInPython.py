dtb = float(input("Nhập điểm trung bình của bạn: "))
if dtb<4:
    print("Bạn rớt môn!")
print("If...Elif...Else:")
if dtb>=4 and dtb<=6.5:
    print("Điểm trung bình")
elif dtb>6.5 and dtb<8.5:
    print("Điểm khá")
elif dtb>=9.5:
    print("Điểm giỏi!")
