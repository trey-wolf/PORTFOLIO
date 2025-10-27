f_year = input("type in your freshmen gpa")
f_year_int = int(f_year)
so_year = input("type in your sophomore gpa")
so_year_int = int(so_year)
j_year = input("type in your junior gpa")
j_year_int = int(j_year)
s_year = input("type in your senior gpa")
s_year_int = int(s_year)

average_gpa = (f_year_int + so_year_int + j_year_int + s_year_int) / 4

can_graduate = False
if average_gpa >= 2.0:
    can_graduate = True

award = ""
if can_graduate and average_gpa >= 5.2:
    award = "Summa Cum Laude"
elif can_graduate and average_gpa < 5.2 and average_gpa >= 4.6:
    award = "Magna Cum Laude"
elif can_graduate and average_gpa < 4.6 and average_gpa >= 4.0:
    award = "Cum Laude"

if not award == "" and can_graduate:
    print(f"Congratulations on graduating! ({award})")
elif not can_graduate:
    print("Sorry you dont get to graduate")

