from functions.get_files_info import get_files_info
from functions.get_files_content import get_file_content
from functions.write_file_content import write_file
from functions.run_python_file import run_python_file


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

    #print("Result for main.py")
    #print(get_file_content("calculator", "main.py"))
    #print("")

    #print("Result for pkg/calculator.py")
    #print(get_file_content("calculator", "pkg/calculator.py"))
    #print("")

    #print("Result for /bin/cat")
    #print(get_file_content("calculator", "/bin/cat"))
    #print("")

    #print("Result for pkg/does_not_exist.py")
    #print(get_file_content("calculator", "does_not_exist.py"))
    #print("")

    #result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    #print(result)

    #result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    #print(result)

    #result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    #print(result)

    result = run_python_file("calculator", "main.py")
    print(result)

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)

    result = run_python_file("calculator", "tests.py")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print(result)


if __name__ == "__main__":
    test()