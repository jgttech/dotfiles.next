from src.pm import PackageManager
from src.conf import conf

def install_packages() -> None:
    package_manager = PackageManager()

    for package in conf.packages:
        package_manager.add(package)

    package_manager.install()
