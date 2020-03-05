import zipf1


def main():

   
    try:

        f = open("output.txt", "r")
        text = f.read()
        f.close()

        zipf_table = zipf1.generate_zipf_table(text, 135)

        zipf1.print_zipf_table(zipf_table)

    except IOError as e:

        print(e)


main()

