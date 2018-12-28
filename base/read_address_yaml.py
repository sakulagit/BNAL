import yaml


class ReadYaml():

    def getData(self):
        with open("../data/address.yaml", "r", encoding="utf-8") as f:
            yaml.load(f).get()


if __name__ == '__main__':
    ReadYaml().getData()
