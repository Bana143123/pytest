def merge_file(file1,file2,output_file):
    try:
        with open(file1, "r") as f1:
            data1 = f1.read()

        with open(file2,"r") as f2:
            data2 = f2.read()

        with open(output_file,"w") as out_file:
            out_file.write(data1 + "\n")
            out_file.write(data2)
        print(f"files {file1} and {file2} have been merged into {output_file}")
    except FileNotFoundError as e:
        print(f"error: {e}")
    except Exception as e:
        print(f"unknown error {str(e)}")


def main():
    file1 = "checking_j/ga.txt"
    file2 = "checking_j/na.txt"
    output_file = "checking_j/merged.txt"
    merge_file(file1,file2,output_file)


if __name__ == "__main__":
    main()