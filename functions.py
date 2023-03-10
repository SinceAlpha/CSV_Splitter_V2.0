# author Darwin Borsato

from tkinter.filedialog import askopenfilename


def split_csv():
    print("open the input file")
    inputfile = askopenfilename()
    # print("select the output file")
    # filename = askopenfilename()
    main_keyword = input("what is the main keyword would you like to split on?: ")
    secondary_keyword = input("what is the secondary keyword would you like to split on?: ")

    with open(inputfile) as finput:
        for line in finput:
            if main_keyword in line:
                output = open("output.csv", 'a')
                output.write(line)
            elif secondary_keyword in line:
                output = open("output.csv", 'a')
                output.write(line)
            elif "TEL PED" in line:
                peds = open("output_peds.csv", 'a')
                peds.write(line)
            elif "#" in line:
                print(line, "Header Skipped!")
            else:
                print(line, "Skipped!")
                file = open("skipped.csv", 'a')
                file.write(line)

#
# def fix_csv():
#     with open("output.csv", 'a') as file:
#         for line in file:
#             if ",," in line:
#



def main():
    pass


if __name__ == '__main__':
    main()
