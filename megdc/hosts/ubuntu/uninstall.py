
def uninstall(distro, packages, purge=True):
    extra_remove_flags = []
    if purge:
        extra_remove_flags.append('--purge')
    distro.packager.remove(
        packages,
        extra_remove_flags=extra_remove_flags
    )



