dzielonePrzez5 = []
dzielonePrzez3 = []
for i in range(0,101):
    if i%5 == 0:
        dzielonePrzez5.append(i)
    elif i%3 == 0:
        dzielonePrzez3.append(i)
print (dzielonePrzez5)
print (dzielonePrzez3)
print (f"Liczb dzielonych przez 5 jest: {len(dzielonePrzez5)}")
print (f"Liczb dzielonych przez 3 jest: {len(dzielonePrzez3)}")