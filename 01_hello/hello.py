"""File for greeting"""
import argparse


def get_args():
    """Getting args from he command line"""
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n',
                        '--name',
                        metavar='name',
                        default='World',
                        help='Name to greet')
    return parser.parse_args()


def main():
    """Main function"""
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
