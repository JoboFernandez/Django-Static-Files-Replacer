import os


def get_file_paths(directory: str):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        relative_path = os.path.relpath(root, directory)
        for file in files:
            path = os.path.join(relative_path, file).replace("\\", "/")
            file_paths.append(path)
    return file_paths


def replace_with_static(static_directory: str, input_file: str, output_file: str):
    # import html file
    with open(input_file, "r") as file:
        html = file.read()

    # revise html file
    html = f"{{% load static %}}\n\n" + html
    for file_path in get_file_paths(static_directory):
        html = html.replace(file_path, f"{{% static '{file_path}' %}}")
        print(file_path)

    # export html file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html)
        print(f"[/] Exported to {output_file}")


if __name__ == "__main__":
    static_directory = input("Enter absolute path of static directory: ")
    input_file = input("Enter input html file: ")
    output_file = input("Enter output html file: ")
    # static_directory = "C:\\Users\\Hp\\Documents\\Working\\OnlineJob\\WebDevelopment\\django_static_file_replacer\\travello\\static"
    # input_file = "index_original.html"
    # output_file = "index.html"

    replace_with_static(static_directory=static_directory, input_file=input_file, output_file=output_file)
