import subprocess


def execute_shell_command(command):
    """Executes a shell command"""
    process = subprocess.Popen([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,
                               shell=True)
    stdout, stderr = process.communicate()
    return stdout.strip(), stderr.strip(), process.returncode


def execute_shell_commands(commands, continue_on_failure=False):
    """Executes multiple shell commands with the option to continue execution if one of them failed"""
    output = []
    error = []
    return_code = []
    if type(commands) is not list:
        commands = [commands]

    for command in commands:
        stdout, stderr, rc = execute_shell_command(command)
        output.append(stdout)
        error.append(stderr)
        return_code.append(rc)
        if rc is not 0 and continue_on_failure is False:
            break

    if len(commands) is 0:
        output = output[0]
        error = error[0]
        return_code = return_code[0]
    output, error, return_code

