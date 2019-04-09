from subprocess import Popen

import os
import shutil


js_libraries = [
    "node_modules/bootstrap/dist/js/bootstrap.bundle.min.js",
    "node_modules/jquery/dist/jquery.min.js",
    "node_modules/lodash/lodash.min.js",
]

css_libraries = [
    "node_modules/bootstrap/dist/css/bootstrap.min.css",
    "node_modules/bootstrap/dist/css/bootstrap.min.css.map",
]


def copy_client_side_dependencies():
    """Copy bootstrap files to the project static directory."""

    JS_ROOT = "node_modules/bootstrap/dist/js/"
    CSS_ROOT = "node_modules/bootstrap/dist/css/"

    for path in js_libraries:
        shutil.copy(path, os.path.join("static/js/"))

    for path in css_libraries:
        shutil.copy(path, os.path.join("static/css/"))

    if not os.path.exists("static/sass/bootstrap/"):
        os.mkdir("static/sass/bootstrap/")

    process = Popen(
        [
            "cp",
            "-a",
            "node_modules/bootstrap/scss/.",
            os.path.join("static/sass/bootstrap/"),
        ]
    )
    process.wait()


if __name__ == "__main__":

    try:
        copy_client_side_dependencies()

        print(f"{len(js_libraries + css_libraries)} files copied.")
    except Exception as e:
        print(e)
