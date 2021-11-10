# assignment
Assurity assignment

# Assurity Assignment
Assignment given to me by Assurity consulting

# Setup

To setup the test you need to have Python3.9 installed. On Ubuntu 20.04 this is
as easy as:

`sudo apt install python3.9`

On Ubuntu 18.04 you will need to install the deadsnakes PPA first.

`sudo add-apt-repository ppa:deadsnakes/ppa`

`sudo apt update`

`sudo apt install python3.9`

`sudo apt install python3.9-distutils`

You will also need to setup a python virtual environment. Install virtualenv
and virtualenvwrapper

`sudo apt install virtualenv`

`sudo apt install virtualenvwrapper`

After installing these packages you will need to source the virtualenvwrapper.sh
file

`source /usr/share/virtualenvwrapper/virtualenvwrapper.sh`

You may want to add this command to your .bashrc (or .zshrc) to ensure that you
always have access to these commands.

This will give you access to the virtualenvwrapper commands needed to create a
virtual environment and to exit the environment.

Now create your environment and install the required Python packages

`mkvirtualenv blackbrad-assignment-39 --python /usr/bin/python3.9`

Make sure you are inside of the assignment directory and install the packages
specified in requirements.txt using pip

`pip install -r requirements.txt`

To leave your environment when you're done with the test, just use the command
`deactivate`

To get back onto the environment later on you can use the `workon` command

`workon blackbrad-assignment-39`

# How to run the test

I used the pytest testing framework to write the test. As such running the
test is as simple as passing the file into pytest in a terminal.

`pytest test.py`
