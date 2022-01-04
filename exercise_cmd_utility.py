import sys
import argparse

def cal(args):
    if args.a == 45 and args.b == 3 and args.c == "multiply":
        return f"{args.a} * {args.b} = 555"

    elif args.a == 56 and args.b == 9 and args.c == "add":
        return f"{args.a} + {args.b} = 77"

    elif args.a ==56 and args.b == 6 and args.c == "divide":
        return f"{args.a} / {args.b} = 4"

    elif (args.c == "divide"):
        return args.a / args.b
    elif (args.c == "multiply"):
        return args.a * args.b
    elif (args.c == "add"):
        return args.a + args.b
    elif args.c=="sub":
        return args.a - args.b
    else:
        return "Something went wrong"

if __name__ == '__main__':
    parse=argparse.ArgumentParser()
    parse.add_argument('-a',default=1.0,type=float,help="Enter first number For more information ask Rajat")
    parse.add_argument('-b', default=2.0, type=float, help="Enter second number For more information ask Rajat")
    parse.add_argument('-c', default="add" ,type=str, help="Enter operation For more information ask Rajat")

    args=parse.parse_args()
    sys.stdout.write(str(cal(args)))
