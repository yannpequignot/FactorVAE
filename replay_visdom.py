import os
import argparse
import visdom


def main(args):
    viz_filename = os.path.join(args.viz_dir, args.name + '.log')
    viz = visdom.Visdom(port=args.viz_port)
    viz.replay_log(viz_filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Replay Visdom logs')

    parser.add_argument('--name', default='main', type=str, help='name of the experiment')
    parser.add_argument('--viz_port', default=8097, type=int, help='visdom port number')
    parser.add_argument('--viz_dir', default='visdom', type=str, help='visdom log directory')

    args = parser.parse_args()

    main(args)
