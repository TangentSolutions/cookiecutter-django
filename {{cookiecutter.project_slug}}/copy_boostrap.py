import os
import shutil


def copy_bootstrap_locally():
    """Copy bootstrap files to the project static directory."""

    shutil.copy(
        'node_modules/bootstrap/dist/js/bootstrap.bundle.min.js',
        os.path.join('{{ cookiecutter.project_slug }}', 'static/js/'),
    )

    shutil.copy(
        'node_modules/bootstrap/dist/css/bootstrap.min.css',
        os.path.join('{{ cookiecutter.project_slug }}', 'static/css/'),
    )

    shutil.copy(
        'node_modules/bootstrap/dist/css/bootstrap.min.css.map',
        os.path.join('{{ cookiecutter.project_slug }}', 'static/css/'),
    )

    shutil.copy(
        'node_modules/jquery/dist/jquery.min.js',
        os.path.join('{{ cookiecutter.project_slug }}', 'static/js/'),
    )


if __name__ == '__main__':

    try:
        copy_bootstrap_locally()
    except:
        pass
