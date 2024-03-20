#  Copyright (c) 2020-2024 Sine Nomine Associates
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

"""Robot Framework Verifier Module."""

import os
import json

try:
    from shlex import join as join_args
    assert join_args  # hush pyflakes
except ImportError:
    from subprocess import list2cmdline as join_args

from molecule import logger
from molecule import util
from molecule.provisioner import ansible_playbook, ansible_playbooks
from molecule.api import Verifier


LOG = logger.get_logger(__name__)


def as_boolean(data):
    if isinstance(data, bool):
        return data
    if hasattr(data, 'lower'):
        return data.lower() in ('yes', 'true', '1', 1, 'on')
    return False


def dict2args(data):
    """
    Convert a dictionary of options to command like arguments.

    Note: This implementation supports arguments with multiple values.
    """
    result = []
    for k, v in data.items():
        if v is not False:
            prefix = "-" if len(k) == 1 else "--"
            flag = f"{prefix}{k}".replace("_", "-")
            if v is True:
                result.append(flag)
            elif isinstance(v, (tuple, list)):
                for x in v:
                    result.extend([flag, str(x)])
            else:
                result.extend([flag, str(v)])
    return result


def dict2lines(data, getlines=False):
    """
    Convert a dictionary of options to a list of lines for robot
    --argumentfile.
    """
    result = []
    for k, v in data.items():
        if v is not False:
            prefix = "-" if len(k) == 1 else "--"
            flag = f"{prefix}{k}".replace("_", "-")
            if v is True:
                result.append(flag + '\n')
            elif isinstance(v, (tuple, list)):
                for x in v:
                    result.append(join_args([flag, str(x)]) + '\n')
            else:
                result.append(join_args([flag, str(v)]) + '\n')
    return result


class Robotframework(Verifier):
    """
    `Robotframework`_ is not default test verifier.

    The robotframework test verifier runs the verify playbook to install Robot
    Framework, external Robot Framework libraries, and the test data sources to
    the test instances, then runs the ``robot`` command, showing the live test
    output. Finally, the optional ``verify_fetch_report`` playbook is executed
    to retrieve the test logs.

    Bundled ``verify.yml`` and ``verify_fetch_report.yml`` playbooks are
    provided by the plugin. You can customize these plays by creating
    ``verify.yml`` and/or ``verify_fetch_report.yml`` in your scenario
    directory.

    The testing can be disabled by setting ``enabled`` to False.

    .. code-block:: yaml

        verifier:
          name: molecule-robotframework
          enabled: False

    Options to ``robot`` can be passed to through the options dict. See the
    ``robot`` command help for a complete list of options.

    .. code-block:: yaml

        verifier:
          name: molecule-robotframework
          options:
            robot:
              dryrun: yes
              exitonerror: yes
              include: mytag

    Environment variables can be passed to the verifier.

    .. code-block:: yaml

        verifier:
          name: molecule-robotframework
          env:
            ROBOT_SYSLOG_FILE: /tmp/syslog.txt

    Paths to the test sources to be copied to the test instance(s).  Provide a
    list of fully qualified paths to directories on the controller.

    .. code-block:: yaml

        verifier:
          name: molecule-robotframework
          options:
            tests:
              - name: uploaded-from-directory
                type: dir
                source: /path/to/my/tests/on/the/controller
              - name: downloaded-from-git-repo
                type: git
                source: "https://gitrepo-url"
                version: branch-name

    The test source 'name' specifies the destination path to install files on
    the test instance(s). The directory will be created on the instance if it
    does not already exist.

    The test paths to be based to robot can be set with the execute keyword.
    This can be a single string or list of strings.

    .. code-block:: yaml

        verifier:
          name: molecule-robotframework
          options:
            tests:
              - name: mytests
                source: /path/to/my/tests/on/the/controller
                execute:
                  - first.robot
                  - more/second.robot
                  - yet-more-tests

    The version of Robot Framwork to be installed may be specified with
    the 'requirements' keyword, which accepts a list of pip requirement
    specifications.

    .. code-block:: yaml

        verifier:
          name: molecule-robotframework
          options:
            requirements:
              - robotframework==6.1.1

    External Robot Framework libraries to install on the test instances with
    pip.

    .. code-block:: yaml

        verifier:
          name: molecule-robotframework
          options:
            libraries:
              - robotframework-sshlibrary
              - robotframework-openafslibrary

    The inventory group name of the test instances. Defaults to 'all'.

    .. code-block:: yaml

        verifier:
          name: molecule-robotframework
          options:
            group: testers

    .. _`Robotframework`: https://robotframework.org
    """

    def __init__(self, config=None):
        super(Robotframework, self).__init__(config)
        self._robot_command = None
        self._playbooks = None

    @property
    def name(self):
        return 'molecule-robotframework'

    @property
    def default_options(self):
        return {}

    @property
    def default_env(self):
        return util.merge_dicts(os.environ.copy(), self._config.env)

    @property
    def playbooks(self):
        if not self._playbooks:
            # Inject a default verify_fetch_report playbook filename.
            if 'verify_fetch_report' not in self._config.config['provisioner']['playbooks']:   # noqa: E501
                self._config.config['provisioner']['playbooks']['verify_fetch_report'] = 'verify_fetch_report.yml'  # noqa: E501
            self._playbooks = ansible_playbooks.AnsiblePlaybooks(self._config)
        return self._playbooks

    def execute_playbook(self, name):
        """Excute the named playbook."""
        # First look for the user provided playbook in the scenario directory.
        # If not found, use the playbook bundled with the plugin.
        playbook = self.playbooks._get_playbook(name)
        if not playbook or not os.path.isfile(playbook):
            playbook = self._get_bundled_playbook(name)
        pb = ansible_playbook.AnsiblePlaybook(playbook, self._config)
        # Target just the testers (all by default.)
        pb.add_cli_arg('extra_vars', f'molecule_robotframework_hosts={self.group}')  # noqa: E501
        pb.execute()

    @property
    def ansible_args(self):
        return self._config.config['provisioner']['ansible_args']

    @property
    def options(self):
        return self._config.config['verifier'].get('options', {})

    @property
    def group(self):
        return self.options.get('group', 'all')

    @property
    def robot_options(self):
        return self.options.get('robot', {})

    @property
    def tests(self):
        return self.options.get('tests', {})

    @property
    def data_sources(self):
        data_sources = []
        for test in self.tests:
            name = test.get('name', 'tests')
            enabled = as_boolean(test.get('enabled', 'yes'))
            if not enabled:
                continue
            execute = test.get('execute', [''])
            if not isinstance(execute, list):
                execute = [execute]
            for e in execute:
                ds = os.path.join(name, e)
                if ds not in data_sources:
                    data_sources.append(ds)
        LOG.debug("data_sources=%s", data_sources)
        return data_sources

    @property
    def test_hosts(self):
        inventory = self._config.provisioner.inventory
        return inventory.get(self.group,
                             inventory.get('all', {})).get('hosts', {})

    @property
    def argumentfile(self):
        return os.path.join(self._config.scenario.ephemeral_directory,
                            'robotrc')

    @property
    def hostvars(self):
        """
        The verify playbook saves the collected host variables
        to a json file in the ephemeral directory.
        """
        directory = self._config.scenario.ephemeral_directory
        filename = os.path.join(directory, 'hostvars.json')
        with open(filename) as f:
            hostvars = json.load(f)
        return hostvars

    def bake(self, name, host):
        """
        Prepare a command to run robot on a test instance.
        """

        # The robot command line.
        home = self.hostvars[name]['ansible_env']['HOME']
        robot_cmd = [
            os.path.join(home, '.robotframework_venv/bin/robot'),
            *dict2args(self.robot_options),
            *self.data_sources  # last
        ]
        LOG.info('robot command: %s' % ' '.join(robot_cmd))

        ansible_connection = host.get('ansible_connection', 'ssh')
        if 'docker' in ansible_connection:
            cmd = ['docker', 'exec', name, *robot_cmd]
        elif 'ssh' in ansible_connection or 'smart' in ansible_connection:
            ssh_host = host.get('ansible_host', name)
            ssh_user = host.get('ansible_user', None)
            ssh_port = host.get('ansible_port', None)
            ssh_ident = host.get('ansible_private_key_file', None)
            ssh_args = host.get('ansible_ssh_common_args', '').split()
            if ssh_port:
                ssh_args.extend(['-p', str(ssh_port)])
            if ssh_ident:
                ssh_args.extend(['-i', ssh_ident])
            if ssh_user:
                ssh_dest = '@'.join([ssh_user, ssh_host])
            else:
                ssh_dest = ssh_host
            LOG.info('ssh command: %s' % ' '.join(
                ['ssh', *ssh_args, ssh_dest]))

            cmd = ['ssh', *ssh_args, ssh_dest, *robot_cmd]
        else:
            util.sysexit_with_message(
                'Unsupported connection %s' % (ansible_connection,), 1)

        self._robot_command = cmd

    def execute(self, action_args=None):
        """
        Execute the robotframework verifier.

        First run the verify playbook (if provided) to install
        robotframework, libraries, and test data. Next, run ``robot`` on each
        host in the test group (``all`` by default). Show the live output of
        the ``robot`` command. Finally, run an optional playbook called
        ``verify_fetch_report`` to retrieve the ``robot`` output files.
        """
        if not self.enabled:
            LOG.warning('Skipping, verifier is disabled.')
            return

        # Save the robot args to a file in our ephemeral directory before
        # running the verify playbook.
        with open(self.argumentfile, 'w') as fh:
            fh.writelines(dict2lines(self.robot_options))

        LOG.info('Prepare for verification.')
        self.execute_playbook('verify')

        LOG.info('Running robotframework verifier tests.')
        verified = None
        for name, host in self.test_hosts.items():
            self.bake(name, host)
            LOG.info(f'Running robotframework tests on instance {name}.')
            result = util.run_command(
                self._robot_command,
                debug=self._config.debug,
                cwd=self._config.scenario.directory,
                env=self.env
            )
            LOG.info(f"robot return code: {result.returncode}")
            if result.returncode == 0:
                verified = True
            else:
                verified = False
                LOG.error(f"Failed to run command: {result.args}")

        LOG.info('Download report files.')
        self.execute_playbook('verify_fetch_report')

        if verified:
            LOG.info('Verifier completed successfully.')
        else:
            LOG.error('Verification failed.')

    def schema(self):
        return {
            "verifier": {
                "type": "dict",
                "schema": {
                    "name": {"type": "string", "allowed": ["robotframework"]},
                },
            }
        }

    def _get_bundled_playbook(self, name):
        """
        Lookup our bundled playbook.
        """
        playbooks = os.path.abspath(
                      os.path.join(os.path.dirname(__file__), "playbooks"))
        path = os.path.join(playbooks, f"{name}.yml")
        if not os.path.isfile(path):
            raise AssertionError(
                'Failed to lookup bundled %s.yml playbook.' % name)
        return path
