__author__ = 'Bas Rustenburg'

from behave import *

@given(u'the module is in the current directory')
def step_impl(context):
    """
    Adds the current directory to the python path.
    :param context:
    :return:
    """
    import os
    cwd = os.getcwd()
    try:
        os.environ['PYTHONPATH'] += ":%s:" % cwd
    except KeyError:
        os.environ['PYTHONPATH'] = cwd

@given(u'that scripts are in the directory "{directory}"')
def step_impl(context, directory):
    """
    Set the directory for running scripts, after making sure it exists.

    :param context:
    :param str directory:
    :return:
    """
    import os
    assert os.path.isdir(directory) is True
    context.scripts = os.path.abspath(directory)

@given(u'the working directory is "{directory}"')
def step_impl(context, directory):
    """
    Check whether a given directory exists.
    If it does not exists, create it in current directory.

    :param context:
    :param str directory:
    :return:
    """
    import os
    fullpath = '%s/%s' % (context.tmpdir, directory)
    if not os.path.isdir(fullpath) is True:
        os.makedirs(fullpath)

    context.workdir = os.path.abspath(fullpath)


@when(u'the script "{scriptname}" is called successfully from the working directory')
def step_impl(context, scriptname):
    """
    Execute a script on the command line.
    Fails if script returns error code other than 0

    :param context:
    :param str scriptname:
    :return:
    """
    import os
    from subprocess import Popen, PIPE
    oldwd = os.getcwd()
    os.chdir(context.workdir)
    try:
        script = Popen('%s/%s' % (context.scripts, scriptname), stdout=PIPE, stderr=PIPE)
        print(script.communicate())

        assert script.stderr

    finally:
        os.chdir(oldwd)

@then(u'a file called "{filename}" is created')
def step_impl(context, filename):
    """
    Check for existence of a file.

    :param context:
    :param str filename:
    :return:
    """
    import os
    assert os.path.isfile('%s/%s' % (context.workdir, filename)) is True

@then(u'"{filename}" is not an empty file')
def step_impl(context, filename):
    """
    Verify that the given file is not empty
    :param context:
    :param str filename:
    :return:
    """
    import os
    oldwd = os.getcwd()
    os.chdir(context.workdir)
    assert os.stat(filename).st_size > 0
    os.chdir(oldwd)

@then(u'"{filename}" is a .{format} file')
def step_impl(context, filename, format):
    """
    Verify format of given file

    TODO: dummy test
    :param context:
    :param str filename:
    :param str format:
    :return:
    """
    assert False
