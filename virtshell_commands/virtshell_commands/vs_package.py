#! /usr/local/bin/python
import os
import io
import platform
import subprocess
from optparse import OptionParser

################################################################################
# build_command function
################################################################################
def build_command(option, args):
    packages_names = ""
    for name in args:
        packages_names = packages_names + name + ' '
    id_distribution, release_distribution, name_distribution = platform.dist()
    if id_distribution == 'Ubuntu':
        if option == 'install':
            command = ['apt-get','install','-y', packages_names.strip()]
        else:
            command = ['apt-get','remove','--purge', '-y', packages_names.strip()]
    else:
        if option == 'install':
            command = ['yum', 'install', '-y', packages_names.strip()]
        else:
            command = ['yum', 'remove', '-y', packages_names.strip()]
    return command

################################################################################
# execute_command function
################################################################################
def execute_command(command):
    lines=""
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    for line in io.TextIOWrapper(process.stdout, encoding="utf-8"):
        lines = lines + line
    return lines

################################################################################
# Process function
################################################################################
def process(options, args):
    if options.install_package:
        command = build_command('install', args)
    elif options.remove_package:
        command = build_command('remove', args)
    print (execute_command(command))

################################################################################
# Usage function
################################################################################
def main():    
    # command line options
    usage = "Usage %prog [options] packagename"
    version = "%prog 1.0"

    parser = OptionParser(usage=usage, version=version)
    parser.add_option("-i", "--install",
                      action="store_true",
                      dest="install_package",
                      help="Install package.")
    parser.add_option("-r", "--remove",
                      action="store_true",
                      dest="remove_package",
                      help="Remove package")
    (options, args) = parser.parse_args()

    if len(args) < 1:
        parser.error("incorrect number of arguments")

    process(options, args)

if __name__=="__main__":
    main()