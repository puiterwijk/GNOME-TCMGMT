# GNOME-TCMGMT

GNOME Travel Committee Management

[![Build Status](https://travis-ci.org/puiterwijk/GNOME-TCMGMT.svg?branch=master)](https://travis-ci.org/puiterwijk/GNOME-TCMGMT)

[![Coverage Status](https://coveralls.io/repos/puiterwijk/GNOME-TCMGMT/badge.svg?branch=master&service=github)](https://coveralls.io/github/puiterwijk/GNOME-TCMGMT?branch=master)

## Quick Start

### Basics

1. Activate a virtualenv
1. Install the requirements

### Set Environment Variables

Update *config.py*, and then run:

```sh
$ export APP_SETTINGS="tcmgmt.config.DevelopmentConfig"
```

or

```sh
$ export APP_SETTINGS="tcmgmt.config.ProductionConfig"
```

### Create DB

```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py create_admin
$ python manage.py create_data
```

### Run the Application

```sh
$ python manage.py runserver
```

### Testing

Without coverage:

```sh
$ python manage.py test
```

With coverage:

```sh
$ python manage.py cov
```
