# -*- coding: utf-8 -*-

import enum
import json
import os


class AutomaticEnum(enum.Enum):

    def __new__(cls):
        value = len(cls.__members__) + 1
        object_ = object.__new__(cls)
        object_._value_ = value
        return object_


class Environment(AutomaticEnum):

    Production = ()
    Staging = ()
    Testing = ()
    Development = ()


# TODO (duyn): Change this into a singleton.
def get_configuration(application_name, _configuration_file=None):

    """
    Get the configuration file.

    The application name is standardized. The convention is to use
    uppercase without delimiters. The configuration file's contents
    **must** be formatted as JSON with the top-level objects specifying
    the environment. For example:

    ```
    {
      "Production": {},
      "Staging": {},
      ...,
    }
    ```

    Parameters
    ----------
    application_name : str
        Application name.
    _configuration_file : File, optional
        Used for testing. Defaults to None.

    Returns
    -------
    dict
        Parsed configuration.

    Raises
    ------
    EnvironmentError
        If the application's environment has not been set.
    EnvironmentError
        If the application's configuration file path has not been set.
    KeyError
        If the configuration file does not have a top-level object
        corresponding to the environment.
    """

    message = """
One of the application's required environment variables could not be
found in the shell environment.

As an example, to set the environment variable for the current shell
session, from the terminal run

    export {environment_variable_name}="{environment_variable_value}"

Note the lack of spaces (" ") between the assignment operator ("=").

On the other hand, to set the environment variable for the current and
all future shell sessions, from the terminal run

    echo 'export {environment_variable_name}="{environment_variable_value}"' >> ~/.bashrc
    source ~/.bashrc

"""

    processed_application_name = application_name.replace('_', '')
    environment_variable_name = processed_application_name.upper() + '_ENVIRONMENT'

    try:
        environment = getattr(Environment, os.environ[environment_variable_name])
    except (AttributeError, KeyError):
        extension = """
Below is the list of acceptable values. Note they are case-sensitive.
    - Production
    - Staging
    - Testing
    - Development

"""
        raise EnvironmentError(
            message.format(
                environment_variable_name=environment_variable_name,
                environment_variable_value=Environment.Production.name)
            + extension)

    if _configuration_file is None:
        environment_variable_name = (
            processed_application_name.upper() + '_CONFIGURATION_FILE_PATH')

        try:
            configuration_file_path = os.environ[environment_variable_name]
        except KeyError:
            environment_variable_value = '/opt/{}/application.config'.format(
                processed_application_name.lower())
            raise EnvironmentError(message.format(
                environment_variable_name=environment_variable_name,
                environment_variable_value=environment_variable_value))

        with open(configuration_file_path, 'r') as file:
            raw_configuration = file.read()
    else:
        raw_configuration = _configuration_file.read()

    try:
        parsed_configuration = json.loads(raw_configuration)[environment.name]
    except KeyError:
        message = (
            """The configuration file does not have a top-level object """
            """corresponding to the environment (i.e. """
            """"{environment_name}").""")
        raise KeyError(message.format(environment_name=environment.name))

    return parsed_configuration
