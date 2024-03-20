# -*- coding: utf-8 -*-

import os
import sys
import tempfile

sys.path.insert(
    1,
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "DisplayCAL"
    ),
)


from DisplayCAL.meta import author, description, DOMAIN, name, version, version_tuple


def mktempver(
    version_template_path, name_=name, description_=description, encoding="UTF-8"
):
    version_template = open(version_template_path, "rb")
    tempver_str = version_template.read().decode(encoding, "replace") % {
        "filevers": str(version_tuple),
        "prodvers": str(version_tuple),
        "CompanyName": DOMAIN,
        "FileDescription": description_,
        "FileVersion": version,
        "InternalName": name_,
        "LegalCopyright": "© " + author,
        "OriginalFilename": name_ + ".exe",
        "ProductName": name_,
        "ProductVersion": version,
    }
    version_template.close()
    tempdir = tempfile.mkdtemp()
    tempver_path = os.path.join(tempdir, "winversion.txt")
    if not os.path.exists(tempdir):
        os.makedirs(tempdir)
    tempver = open(tempver_path, "wb")
    tempver.write(tempver_str.encode(encoding, "replace"))
    tempver.close()
    return tempver_path
