import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_use_ansible_var_from_get_variables(host):
    all_variables = host.ansible.get_variables()
    assert all_variables['httpd_port'] == 80


def test_use_ansible_var_from_debug_var(host):
    result = host.ansible("debug", "var=httpd_port")
    assert result['httpd_port'] == 80


def test_use_ansible_var_from_debug_msg(host):
    result = host.ansible("debug", "msg={{ httpd_port }}")
    assert result['msg'] == 80


def test_use_ansible_var_from_role_defaults(host):
    ansible_vars = host.ansible(
        "include_vars", "file=../../roles/web/defaults/main.yml"
    )["ansible_facts"]
    assert ansible_vars['httpd_port'] == 8000
