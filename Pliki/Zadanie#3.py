# $ python clean_emails.py emails.txt cleaned_emails.txt
# sys.argv is a list in Python, which contains the command-line arguments passed to the script

# zbiór - unikalność nazw
# strip - wyczyszczenie pustych znaków
# wywolanie funkcji x() - czyli tego co ona robi, ale samo x to przywolanie funkcji - samej funkcji, jej definicji

import sys

if len(sys.argv) != 3:  # 1- nazwa modułu 2-plik otwierany, 3-pliko nowy, zwraca ile jest argumentów wpisanych n konsoli
    print("Podałeś złą liczbę argumentów")
    exit()

_, file_in, file_out = sys.argv  # trzy zmienne - samo podkreślenie może być nazwą zmiennej

print(file_in)

with open(file_in) as f:
    unique_emails = set()
    for line in f:
        line = line.strip().lower()  # usunie niepotrzebne spacje
        if line.count("@") == 1:
            unique_emails.add(line)
emails = sorted(unique_emails)  #posortuje

with open(file_out, "w") as f:
    for email in emails:
        f.write(email + "\n")
    # lub:
    # out = "\n".join(emails)
    # f.write(out)

print(file_out)
