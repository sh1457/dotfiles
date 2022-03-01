from pathlib import Path

import click


def view(path: Path):
    with open(path, 'r') as fp:
        for line in fp.readlines():
            print(line.rstrip())


def build(path: Path):
    with open(path, 'r') as fp:
        code_flag = False
        for line in fp.readlines():
            if line.strip().startswith("```"):
                code_flag = not code_flag
                continue

            if code_flag:
                print(line.rstrip())


def ls():
    path = Path(__file__).parent / 'dotfiles'
    print(path)
    for i in path.glob("*.md"):
        print(i)
        view(i)
        build(i)


def main():
    print("MAIN")
    ls()


if __name__ == '__main__':
    main()

