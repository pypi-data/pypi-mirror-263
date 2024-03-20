import argparse
from .build_module import make_module

def main():
    parser = argparse.ArgumentParser(description='Create a new module')
    parser.add_argument('name', type=str, help='Module name')
    parser.add_argument('desc', type=str, help='Module description')
    parser.add_argument('version', type=str, help='Module version')
    args = parser.parse_args()
    make_module(args.name, args.desc, args.version)

if __name__ == '__main__':
    main()
