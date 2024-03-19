# Copyright 2024 Open Source Robotics Foundation, Inc.
# Licensed under the Apache License, Version 2.0

from pathlib import Path
import sys
import sysconfig

from colcon_core.location import get_relative_package_index_path
from colcon_core.package_descriptor import PackageDescriptor
from colcon_installed_package_information.package_augmentation.colcon_index \
    import ColconIndexPackageAugmentation
from colcon_installed_package_information.package_augmentation.python \
    import InstalledPythonPackageAugmentation
import pytest


@pytest.fixture
def mock_egg_package(tmp_path):
    lib_dir = Path(sysconfig.get_path('purelib', vars={'base': str(tmp_path)}))
    pkg_dir = lib_dir / 'egg_pkg-4.5.6.egg-info'

    pkg_dir.mkdir(parents=True)
    (pkg_dir / 'PKG-INFO').write_text(
        'Metadata-Version: 2.1\n'
        'Name: egg-pkg\n'
        'Version: 4.5.6\n'
    )
    (pkg_dir / 'requires.txt').write_text(
        'wheel-pkg\n'
    )

    desc = PackageDescriptor(str(tmp_path))
    desc.name = 'egg-pkg'
    desc.type = 'installed'
    yield desc


@pytest.fixture
def mock_wheel_package(tmp_path):
    lib_dir = Path(sysconfig.get_path('purelib', vars={'base': str(tmp_path)}))
    pkg_dir = lib_dir / (
        'wheel_pkg-1.2.3.'
        f'py{sys.version_info.major}.{sys.version_info.minor}.dist-info'
    )

    pkg_dir.mkdir(parents=True)
    (pkg_dir / 'METADATA').write_text(
        'Metadata-Version: 2.1\n'
        'Name: wheel-pkg\n'
        'Version: 1.2.3\n'
    )

    desc = PackageDescriptor(str(tmp_path))
    desc.name = 'wheel-pkg'
    desc.type = 'installed'
    yield desc


@pytest.fixture
def mock_colcon_index_package(tmp_path):
    index_dir = tmp_path / get_relative_package_index_path()

    index_dir.mkdir(parents=True)
    (index_dir / 'colcon-index-pkg').write_text(
        'some-other-pkg',
    )

    desc = PackageDescriptor(str(tmp_path))
    desc.name = 'colcon-index-pkg'
    desc.type = 'installed'
    yield desc


def test_colcon_index(mock_colcon_index_package):
    augmentation_extension = ColconIndexPackageAugmentation()

    augmentation_extension.augment_packages([
        mock_colcon_index_package,
    ])

    assert mock_colcon_index_package.name == 'colcon-index-pkg'
    assert mock_colcon_index_package.type == 'installed.colcon'
    assert 'some-other-pkg' in mock_colcon_index_package.dependencies['run']


@pytest.mark.parametrize('augmentation_extension_class', [
    ColconIndexPackageAugmentation,
    InstalledPythonPackageAugmentation,
])
def test_no_installed(tmp_path, augmentation_extension_class):
    augmentation_extension = augmentation_extension_class()

    desc = PackageDescriptor(str(tmp_path))
    desc.name = 'cmake-package'
    desc.type = 'cmake'

    augmentation_extension.augment_packages([desc])

    assert desc.name == 'cmake-package'
    assert desc.type == 'cmake'


@pytest.mark.parametrize('augmentation_extension_class', [
    ColconIndexPackageAugmentation,
    InstalledPythonPackageAugmentation,
])
def test_not_found(tmp_path, augmentation_extension_class):
    augmentation_extension = augmentation_extension_class()

    desc = PackageDescriptor(str(tmp_path))
    desc.name = 'no-such-package'
    desc.type = 'installed'

    augmentation_extension.augment_packages([desc])

    assert desc.name == 'no-such-package'
    assert desc.type == 'installed'


def test_python(mock_egg_package, mock_wheel_package):
    augmentation_extension = InstalledPythonPackageAugmentation()

    augmentation_extension.augment_packages([
        mock_egg_package,
        mock_wheel_package,
    ])

    assert mock_egg_package.name == 'egg-pkg'
    assert mock_egg_package.type == 'installed.python'
    assert mock_egg_package.metadata.get('version') == '4.5.6'
    assert 'wheel-pkg' in mock_egg_package.dependencies['run']

    assert mock_wheel_package.name == 'wheel-pkg'
    assert mock_wheel_package.type == 'installed.python'
    assert mock_wheel_package.metadata.get('version') == '1.2.3'
    assert not any(mock_wheel_package.dependencies.items())
