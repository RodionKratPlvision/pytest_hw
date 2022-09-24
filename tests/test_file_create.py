import os


def create_dir(path, dir_name):
    os.mkdir(os.path.join(path, dir_name))


def create_file(path, file_name):
    with open(os.path.join(path, file_name), 'w') as file:
        return


def write_test_to_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)


def test_file_create(get_path, get_text, teardown_file_create):
    cur_path, dir_name, file_name = get_path
    create_dir(cur_path, dir_name)
    assert dir_name in os.listdir(cur_path)

    dir_path = os.path.join(cur_path, dir_name)
    create_file(dir_path, file_name)
    assert file_name in os.listdir(dir_path)

    file_path = os.path.join(dir_path, file_name)
    write_test_to_file(file_path, get_text)
    with open(file_path, 'r') as file:
        assert file.read() == get_text
