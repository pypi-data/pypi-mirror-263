from importlib import import_module
import inspect
import os
import sysconfig


def traverse_files(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isdir(file_path):
            for i in traverse_files(file_path):
                yield i
        else:
            # 在这里可以对文件进行操作
            if file_path.endswith(".py"):
                yield file_path


def get_import(f):
    imports = []
    for line in f.split("\n"):
        if "".join(list(line)[0:5]) == "from " and "import " in line:
            line = (
                line.replace("from", "")
                .split("import")[0]
                .replace(" ", "")
                .split(".")[0]
            )
            imports.append(line)
        elif "".join(list(line)[0:7]) == "import ":
            line = line.replace("import", "")
            for item in line.split(","):
                item = item.split(" as ")[0].replace(" ", "").split(".")[0]
                imports.append(item)
    return list(set(imports))


def get(
    BASE_PATH="./",
    FORMAT_LIST={
        "PIL": "pillow",
        "cv2": "opencv-python",
        "bs4": "beautifulsoup4",
        "sqlalchemy": "SQLAlchemy",
        "execjs": "PyExecJS",
        "yaml": "pyyaml",
        "Crypto": "pycryptodome",
    },
    IGNORE_LIST=[],
):
    self = __file__.split("\\")
    self = self[self.__len__() - 1]
    self = self.split("/")
    self = self[self.__len__() - 1]
    lib_path = sysconfig.get_paths()["purelib"]
    global_imports = []
    for i in traverse_files(BASE_PATH):
        if self in i:
            continue
        with open(i, "r", encoding="utf-8") as f:
            global_imports += get_import(f.read())
            global_imports = list(set(global_imports))
    with open(BASE_PATH + "requirements.txt", "a+", encoding="utf-8") as requirements:
        requirements.truncate(0)
        for item in global_imports:
            if item in IGNORE_LIST:
                continue
            if os.path.exists(BASE_PATH + item):
                continue
            if os.path.exists(BASE_PATH + item + ".py"):
                continue
            if not os.path.exists(lib_path + "/" + item) and not os.path.exists(
                lib_path + "/" + item + ".py"
            ):
                continue

            try:
                item = f"{FORMAT_LIST.get(item) or item}=={inspect.getmodule(import_module(item)).__version__}"
            except:
                item = FORMAT_LIST.get(item) or item
            requirements.write(item + "\n")
