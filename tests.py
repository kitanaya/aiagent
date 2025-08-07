from functions.get_files_info import get_files_info
from functions.get_files_content import get_file_content


def test():
    #print("Result for current directory:")
    #print(get_files_info("calculator", "."))
    #
    #print("Result for 'pkg' directory:")
    #print(get_files_info("calculator", "pkg"))
    #
    #print("Result for '/bin' directory:")
    #print(get_files_info("calculator", "/bin"))
    #
    #print("Result for '../' directory:")
    #print(get_files_info("calculator", "../"))

    #result = get_file_content("calculator", "lorem.txt")
    #print("File content of lorem:")
    #print(result)

    print("Result for main.py")
    print(get_file_content("calculator", "main.py"))
    print("")

    print("Result for pkg/calculator.py")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("")

    print("Result for /bin/cat")
    print(get_file_content("calculator", "/bin/cat"))
    print("")

    print("Result for pkg/does_not_exist.py")
    print(get_file_content("calculator", "does_not_exist.py"))
    print("")

if __name__ == "__main__":
    test()