import sys
import argparse
path = sys.path[0]
parser=argparse.ArgumentParser(description='model')
parser.add_argument('input1',type=str,help='input id')
args=parser.parse_args()
input1=args.input1
def test_run(input1):
    if input1 == 'll':
        print('Hello World')
    else:
        print('!')
    # print('Hello World')

if __name__ == '__main__':
    test_run(input1)
