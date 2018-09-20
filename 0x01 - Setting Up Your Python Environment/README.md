# 1. Setting Up Your Python Environment

The first thing we are going to do is ensure that the correct version od Python is installed (2.7), execute the following:

```
root@kali:~# python --version
Python 2.7.x
root@kali:~#
```

Now let's add some useful pieces of Python package management in the form of **easy_install** and **pip**. These are much like **apt** package manager because they allow you to
directly install Python libraries, without having to manually download, unpack, and install them. Let's install both of these package managers by issuing the following commands:

```
root@kali:~# apt-get install python-setuptools python-pip
```

When the packages are installed, we can do a quick test and install the module that we'll use in **Chapter 7** to build a 
GitHub-based trojan. Enter the following into your terminal:

```
root@kali:~# pip install github3.py
```

Then drop into python shell and validate that it was installed correctly:

```
root@kali:~# python
Python 2.7.15 (default, Jul 28 2018, 11:29:29) 
[GCC 8.1.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import github3
>>> exit()
root@kali:~# 
```
