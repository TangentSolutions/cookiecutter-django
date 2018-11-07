# cookiecutter-django

A django cookie cutter template inspired by [cookiecutter-django](https://github.com/pydanny/cookiecutter-django).

# Installation & Usage

```bash
$ python -m venv env
$ source env/bin/activate

$ pip install --upgrade pip
$ pip install -r requirements.txt
$ cookiecutter https://github.com/TangentSolutions/cookiecutter-django
```

After generating the project cd into it and run the following.

```bash
$ npm install # This is for bootstrap
$ python ./copy_bootstrap.py
$ docker-compose -f local.yml up --build
```

# First steps

The project includes a small demo of the libraries it bundles. Once running open your browser on [localhost:8000](http://localhost:8000) and create an account. The mail hog server can be accessed on [localhost:8025](http://localhost:8025/) when you need to retrieve the confirmation email.

TODO:

- Add django channels support
- Add GraphQL support
- Investigate replacing allauth
