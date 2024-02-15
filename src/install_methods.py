from os import walk
import os
import subprocess


def install_packages(source, packages):
    for package in packages:
        subprocess.run([source, 'install', package, '-y'])


def install_flatpak_packages(packages):
    install_packages("flatpak", packages)


def install_snap_packages(packages):
    install_packages("snap", packages)


def install_apt_packages(packages):
    install_packages("apt", packages)


def install_gnome_extensions(extensions):
    install_packages("gnome-extensions", extensions)

def install_files_from_bytes(files, write_mode):
    for file in files:
        with open(file, write_mode) as filename:
            filename.write(file[1])
            filename.close()


def install_git_repos(repos):
    for repo in repos:
        subprocess.run([f'git clone {repo[1]} {repo[0]}'], stdout=subprocess.PIPE)

