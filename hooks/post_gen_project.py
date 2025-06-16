# Shell commands via python to be platform-independent
import subprocess as sp


def init_git_repo():
    sp.check_call(["git", "init", "."])
    sp.check_call(["git", "branch", "-m", "main"])


def add_git_remote():
    sp.check_call(
        [
            "git",
            "remote",
            "add",
            "origin",
            "git@github.com:MaMMoS-project/{{ cookiecutter.project_name }}.git"
        ]
    )

def install_pre_commit_hooks():
    sp.check_call(["pre-commit", "install"])


if __name__ == "__main__":
    init_git_repo()
    add_git_remote()
    install_pre_commit_hooks()
