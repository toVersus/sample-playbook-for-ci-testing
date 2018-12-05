# Building a simple LAMP stack and deploying Application using Ansible Playbooks.

[![CircleCI](https://circleci.com/gh/toVersus/sample-playbook-for-ci-testing.svg?style=svg)](https://circleci.com/gh/toVersus/sample-playbook-for-ci-testing)
[![TravisCI](https://travis-ci.org/toVersus/sample-playbook-for-ci-testing.svg?branch=master)](https://travis-ci.org/toVersus/sample-playbookfor-ci-testing)
[![AppVeyor](https://ci.appveyor.com/api/projects/status/bagbu5l6qvvqtnso?svg=true)](https://ci.appveyor.com/project/toVersus/sample-playbookfor-ci-testing)
[![Azure Pipelines](https://dev.azure.com/toversus/sample-role-for-ci-testing/_apis/build/status/toVersus.sample-playbook-for-ci-testing)](https://dev.azure.com/toversus/sample-role-for-ci-testing/_build/latest?definitionId=2)
[![shippable](https://api.shippable.com/projects/5bf2d1d73038210700d6b38f/badge?branch=master)](https://app.shippable.com/github/toVersus/sample-playbook-for-ci-testing/dashboard)


These playbooks require Ansible 1.2.

These playbooks are meant to be a reference and starter's guide to building Ansible Playbooks. These playbooks were tested on CentOS 6.x so we recommend that you use CentOS or RHEL to test these modules.

You can test this playbook on your local machine installing [Pipenv](https://github.com/pypa/pipenv), python package and virtualenv manager.

Once done, you just run the following commands:

```bash
$ git clone https://github.com/toVersus/sample-playbook-for-ci-testing.git
$ cd ./sample-playbook-for-ci-testing
$ pipenv sync
$ pipenv run test
```

This LAMP stack can be on a single node or multiple nodes. The inventory file 'hosts' defines the nodes in which the stacks should be configured.

```ini
[webservers]
localhost

[dbservers]
bensible
```

Here the webserver would be configured on the local host and the dbserver on a
server called "bensible". The stack can be deployed using the following
command:

```bash
$ ansible-playbook -i hosts site.yml
```

Once done, you can check the results by browsing to http://localhost/index.php. You should see a simple test page and a list of databases retrieved from the database server.
