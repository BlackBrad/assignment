# assignment

# Disclaimer
I do not have a machine running Windows. Therefore all the instructions below
are only valid for machines running Ubuntu 20.04 or Ubuntu 18.04. I do not
know how to setup the enviroment on Windows based machines.

# Setup

To setup the test you need to have Python3.9 installed. On Ubuntu 20.04 this is
as easy as:

`sudo apt install python3.9`

On Ubuntu 18.04 you will need to install the deadsnakes PPA first.

`sudo apt install software-properties-common`

`sudo add-apt-repository ppa:deadsnakes/ppa`

`sudo apt update`

`sudo apt install python3.9 python3.9-distutils`

You will also need to setup a python virtual environment. Install virtualenv
and virtualenvwrapper

`sudo apt install virtualenv virtualenvwrapper`

After installing these packages you will need to source the
virtualenvwrapper.sh file

`source /usr/share/virtualenvwrapper/virtualenvwrapper.sh`

This will give you access to the virtualenvwrapper commands needed to create a
virtual environment and to exit the environment. You may want to add this
command to your .bashrc (or .zshrc) to ensure that you always have access to
these commands.

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

# Other Information
## PEP8

This test has been written to be pep8 complient. It meets the pep8 guidelines
and has been verified using the flake8 tool, which is installed as part of
`requirements.txt`. If you want to check this you can run the `flake8` command,
passing in the file

`flake8 test.py`

If everything is okay then flake8 will produce no output.

## Logging to a file

The logs are not only written to the console but a file as well. After running
the tests there should be a `log.txt` file in the directory. If you open it
then you'll see all the logs are output to there as well. This is the reason
that every test starts with `log.info(Staring TEST_NAME)`, this is so we can
differentiate the logs for each test in `log.txt`.

If you wanted to change the output file then all you'd need to do is change the
`log_file` parameter in pytest.ini to whatever you wanted.

`log_file = some_file_name.txt`
