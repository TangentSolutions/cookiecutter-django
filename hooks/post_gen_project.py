import os
import shutil
import secrets
import subprocess


# Globals
TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "
DEBUG_VALUE = "debug"


def remove_celery_app():
    """Helper function to remove celery files if project does not make use of celery."""

    shutil.rmtree(os.path.join("taskapp"))


def remove_dottravisyml_file():
    """Helper function to remove travis files if no travis integration is required."""

    os.remove(".travis.yml")


def append_to_gitignore_file(s):
    """Helper function to append paths to the .gitignore file."""

    with open(".gitignore", "a") as gitignore_file:
        gitignore_file.write(s)
        gitignore_file.write(os.linesep)


def set_flag(file_path, flag, length=None, value=None, formatted=None):
    """Helper function to replace variable placeholders in the project."""

    if value is None:
        random_string = secrets.token_urlsafe(length)

        if formatted is not None:
            random_string = formatted.format(random_string)

        value = random_string.strip()

    with open(file_path, "r+") as f:
        file_contents = f.read().replace(flag, value)
        f.seek(0)
        f.write(file_contents)
        f.truncate()

    return value


def set_django_secret_key(file_path):
    """Set the django secret key."""

    return set_flag(file_path, "!!!SET DJANGO_SECRET_KEY!!!", length=64)


def set_django_admin_url(file_path):
    """Set the django admin url."""

    return set_flag(file_path, "!!!SET DJANGO_ADMIN_URL!!!", length=32, formatted="{}/")


def generate_random_user():
    """Generate a random username using the secrets module."""

    return secrets.token_urlsafe(32)


def generate_postgres_user(debug=False):
    """Generate a random username for the postgres instance."""

    return DEBUG_VALUE if debug else generate_random_user()


def set_postgres_user(file_path, value):
    """Replace the postgres user placeholder in the .postgres env file."""

    return set_flag(file_path, "!!!SET POSTGRES_USER!!!", value=value)


def set_postgres_password(file_path, value=None):
    """Replace the postgres password placeholder in the .postgres env file."""

    return set_flag(file_path, "!!!SET POSTGRES_PASSWORD!!!", length=64, value=value)


def set_celery_flower_user(file_path, value):
    """Replace the celery/flower user placeholder in the .postgres env file."""

    return set_flag(file_path, "!!!SET CELERY_FLOWER_USER!!!", value=value)


def set_celery_flower_password(file_path, value=None):
    """Replace the celery/flower password placeholder in the .postgres env file."""

    return set_flag(
        file_path, "!!!SET CELERY_FLOWER_PASSWORD!!!", value=value, length=64
    )


def set_flags_in_envs(postgres_user, celery_flower_user, debug=False):
    """Replaces the placeholders in the environment files."""

    local_django_envs_path = os.path.join(".envs", ".local", ".django")
    production_django_envs_path = os.path.join(".envs", ".production", ".django")
    local_postgres_envs_path = os.path.join(".envs", ".local", ".postgres")
    production_postgres_envs_path = os.path.join(".envs", ".production", ".postgres")

    set_django_secret_key(production_django_envs_path)
    set_django_admin_url(production_django_envs_path)

    set_postgres_user(local_postgres_envs_path, value=postgres_user)
    set_postgres_password(
        local_postgres_envs_path, value=DEBUG_VALUE if debug else None
    )
    set_postgres_user(production_postgres_envs_path, value=postgres_user)
    set_postgres_password(
        production_postgres_envs_path, value=DEBUG_VALUE if debug else None
    )

    set_celery_flower_user(local_django_envs_path, value=celery_flower_user)
    set_celery_flower_password(
        local_django_envs_path, value=DEBUG_VALUE if debug else None
    )
    set_celery_flower_user(production_django_envs_path, value=celery_flower_user)
    set_celery_flower_password(
        production_django_envs_path, value=DEBUG_VALUE if debug else None
    )


def set_flags_in_settings_files():
    """Replaces the placeholders in the project settings files."""

    set_django_secret_key(os.path.join("config", "settings", "local.py"))
    set_django_secret_key(os.path.join("config", "settings", "test.py"))


def initialize_repo():
    """Initialize an empty git repo."""

    process = subprocess.Popen(["git", "init"], stdout=subprocess.PIPE)
    process.wait()
    return process.stdout.read()


def add_black_formatter_git_hook():
    """Adds the black formatter pre commit git hook."""

    # Setup an empty repo
    initialize_repo()

    # Ensure the pre commit hook is executable
    process = subprocess.Popen(["chmod", "+x", "Git-Hooks/Python/pre-commit"])
    process.wait()

    # Copy the pre commit hook
    shutil.copy("Git-Hooks/Python/pre-commit", ".git/hooks/pre-commit")


def apply_initial_black_formatting():
    """Applies the black formatter to the project."""

    try:
        print(INFO + "Applying black formatting" + TERMINATOR)

        process = subprocess.Popen(["black", ".", "-S", "--line-length=120"])
        process.wait()
    except:
        pass


def remove_envs_and_associated_files():
    """Docker specific function which removes environment files."""

    shutil.rmtree(".envs")
    os.remove("merge_production_dotenvs_in_dotenv.py")


def remove_celery_compose_dirs():
    """Remove the celery compose files."""

    shutil.rmtree(os.path.join("compose", "local", "django", "celery"))
    shutil.rmtree(os.path.join("compose", "production", "django", "celery"))


def remove_git_hooks_directory():
    """Remove the git hooks directory."""

    shutil.rmtree(os.path.join("Git-Hooks"))


def remove_copy_bootstrap_file():
    """Remove the package.json file."""

    os.remove("copy_bootstrap.py")


def remove_graphql_files():
    """Remove the package.json file."""

    path = os.path.join("accounts", "schema.py")
    os.remove(path)


def main():
    debug = "{{ cookiecutter.debug }}".lower() == "y"

    set_flags_in_envs(
        DEBUG_VALUE if debug else generate_random_user(),
        DEBUG_VALUE if debug else generate_random_user(),
        debug=debug,
    )

    set_flags_in_settings_files()

    append_to_gitignore_file(".env")
    append_to_gitignore_file(".envs/*")

    if "{{ cookiecutter.keep_local_envs_in_vcs }}".lower() == "y":
        append_to_gitignore_file("!.envs/.local/")

    if "{{ cookiecutter.use_celery }}".lower() == "n":
        remove_celery_app()
        remove_celery_compose_dirs()

    if "{{ cookiecutter.use_travisci }}".lower() == "n":
        remove_dottravisyml_file()

    if "{{ cookiecutter.use_graphql }}".lower() == "n":
        remove_graphql_files()

    add_black_formatter_git_hook()
    apply_initial_black_formatting()
    remove_git_hooks_directory()

    print(SUCCESS + "Project initialized, keep up the good work!" + TERMINATOR)


if __name__ == "__main__":
    main()
