import subprocess


def install_packages(source, packages):
    for package in packages:
        subprocess.run([source, 'install', package])


def install_flatpak_packages(packages):
    install_packages("flatpak", packages)


def install_snap_packages(packages):
    install_packages("snap", packages)


def install_apt_packages(packages):
    install_packages("apt", packages)


def install_gnome_extensions(extensions):
    install_packages("gnome-extensions", extensions)