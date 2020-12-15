import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
# print(packages)
for i in packages:
    print('INSTALLING =>', i)
    call("pip install --upgrade " + i, shell=True)
