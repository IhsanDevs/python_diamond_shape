# function main yang berfungsi untuk menjalankan program
# dan membuat diamond shape

def main():

    # Atur jumlah karakter
    n = int(input("Enter a number: "))

    # Atur jenis karakter
    char = "+"

    for i in range(1, n * 2):
        if i <= n:
            print(" " * (n - i) + char * (i * 2 - 1))
        else:
            print(" " * (i - n) + char * ((n * 2 - i) * 2 - 1))


if __name__ == "__main__":
    main()
