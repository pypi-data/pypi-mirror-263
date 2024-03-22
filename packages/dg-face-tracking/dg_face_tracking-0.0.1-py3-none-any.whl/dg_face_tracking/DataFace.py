import argparse

from controller import DataFaceController


def main(config_name):
    ctl = DataFaceController()
    if not ctl.config(config_name):
        print("DataFace: main: Failed to Config controller")
        ctl.stop()
        return
    # Start all Services
    ctl.run()


if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("config")
    try:
        args = argParser.parse_args()
        config_name = args.config
    except:
        config_name = "face_tracker.cfg"

    main(config_name)
