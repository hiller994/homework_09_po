import os
import homework_9_selene_po.tests

def path(file_name):
    return os.path.abspath(
        os.path.join(os.path.dirname(homework_9_selene_po.tests.__file__), f'../test_file/{file_name}')
    )