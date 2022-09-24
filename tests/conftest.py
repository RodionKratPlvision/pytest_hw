import pytest
import ifcfg
import os
import shutil


@pytest.fixture(scope='module')
def get_ifconfig_lo_interface():
    lo_interface = ifcfg.interfaces()['lo']

    return lo_interface


@pytest.fixture()
def get_path():
    return os.getcwd(), 'test_dir', 'test_file'


@pytest.fixture()
def get_text():
    return 'Я люблю пайтест'


@pytest.fixture()
def teardown_file_create(get_path):

    yield

    cur_path, dir_name, *_ = get_path
    shutil.rmtree(os.path.join(cur_path, dir_name))
