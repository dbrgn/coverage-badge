# Release process

Signing key: 3578F667F2F3A5FA (https://keybase.io/dbrgn)

Used variables:

    export VERSION={VERSION}
    export GPG=3578F667F2F3A5FA

Update version number:

    vim -p setup.py coverage_badge/__main__.py

Do a signed commit and signed tag of the release:

    git add setup.py coverage_badge/__main__.py
    git commit -S${GPG} -m "Release v${VERSION}"
    git tag -u ${GPG} -m "Release v${VERSION}" v${VERSION}

Build source and binary distributions:

    python3 setup.py sdist
    python3 setup.py bdist_wheel

Sign files:

    gpg --detach-sign -u ${GPG} -a dist/coverage-badge-${VERSION}.tar.gz
    gpg --detach-sign -u ${GPG} -a dist/coverage_badge-${VERSION}-py2.py3-none-any.whl

Upload package to PyPI:

    twine3 upload dist/coverage[-_]badge-${VERSION}*
    git push
    git push --tags
