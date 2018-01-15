# Cookiecutter Kotlin
[![Build Status](https://travis-ci.org/Seik/cookiecutter-kotlin.svg?branch=master)](https://travis-ci.org/Seik/cookiecutter-kotlin)

A [cookiecutter](https://github.com/audreyr/cookiecutter) template for [Gradle](http://gradle.org) based [Kotlin](http://kotlinlang.org) projects.
## Usage

First, get Cookiecutter. Trust me, it's awesome:
```bash
$ pip install cookiecutter
```

You can also install it with homebrew:

```bash
$ brew install cookiecutter
```

Now run cookiecutter against this repo:

```bash
cookiecutter https://github.com/seik/cookiecutter-kotlin
```

Answer the prompts with your own desired options. For example:
```console
name [kotlin_project]: projectname
repo_name [projectname]: projectname
package_name [me.ivmg.projectname]: my.package.projectname
package_path [my/package/projectname]: my/package/projectname
group [my.package.projectname]: my.package.projectname
version [0.0.1-SNAPSHOT]: 0.0.1-SNAPSHOT
kotlin_version [1.2.10]: 1.2.10
gradle_version [3.5-rc-2]: 3.5-rc-2
use_git [y]: y
```

Your project has been generated!:

```bash
$ cd projectname/
$ ls
```

Push it to your repo (If you have already selected git option on the generation there is no need to init and commit ✨):
```console
$ git init
$ git add .
$ git commit -m "Initial commit"
$ git remote add origin git@github.com:seik/projectname.git
$ git push -u origin master
```

See the [cookiecutter documentation](http://cookiecutter.readthedocs.org/en/latest/usage.html) for full details.
