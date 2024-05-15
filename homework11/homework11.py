import csv
import json
import logging


def main():
    task1()
    task2()
    task3()


def task1():
    with open(r'D:\Automation\HillelPython\hw2\PythonAutoTest\homework11\r-m-c.csv') as fileObject1:
        reader_obj1 = csv.reader(fileObject1)
        for row1 in reader_obj1:
            with open(r'D:\Automation\HillelPython\hw2\PythonAutoTest\homework11\rmc.csv') as fileObject2:
                reader_obj2 = csv.reader(fileObject2, delimiter=";")
                for row2 in reader_obj2:
                    if row1 == row2:
                        with open(r'D:\Automation\HillelPython\hw2\PythonAutoTest\homework11\result_task1.csv',
                                  'w') as writeObj:
                            writeObj.write(str(row2))


def task2():
    with open('localizations_en.json', 'r') as f:
        try:
            data = json.load(f)
        except Exception as e:
            with open(r'json__task2.log', 'a') as writeObj:
                writeObj.write(f'Error in localizations_en.json {e}\n')

    with open('localizations_ru.json', 'r') as f:
        try:
            data = json.load(f)
        except Exception as e:
            with open(r'json__task2.log', 'a') as writeObj:
                writeObj.write(f'Error in localizations_ru.json {e}\n')

    with open('swagger.json', 'r') as f:
        try:
            data = json.load(f)
        except Exception as e:
            with open(r'json__task2.log', 'a') as writeObj:
                writeObj.write(f'Error in swagger.json {e}\n')

    with open('login.json', 'r') as f:
        try:
            data = json.load(f)
        except Exception as e:
            with open(r'json__task2.log', 'a') as writeObj:
                writeObj.write(f'Error in login.json {e}\n')


def log_event(message):
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(message)s'
    )
    logger = logging.getLogger("log_event")
    logger.info(message)


def task3():
    import xml.etree.ElementTree as ET
    tree = ET.parse("groups.xml")
    root = tree.getroot()
    for child in root.findall("group"):
        element_incom = child.find("timingExbytes")
        if element_incom is not None:
            elem = element_incom.find("incoming")
            log_event(elem.text)


if __name__ == "__main__":
    main()
