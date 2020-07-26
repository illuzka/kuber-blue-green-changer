import yaml
import io
import argparse


class BlueGreen:
    """

    """

    def __init__(self, files, new_image_name, version_label_key='role'):
        self.files = files
        self.version_label_key = version_label_key
        self.new_image_name = new_image_name

    def change_role(self, obj, file_name):
        """

        :param obj:
        :param file_name:
        :return:
        """

        if self.version_label_key in obj: return obj[self.version_label_key]
        for k, v in obj.items():
            if isinstance(v, dict):
                item = self.change_role(v, file_name)
                if item == 'blue':
                    v[self.version_label_key] = 'green'
                elif item == 'green':
                    v[self.version_label_key] = 'blue'


        with io.open(file_name, 'w', encoding='utf8') as f:
            yaml.dump(obj, f, default_flow_style=False, allow_unicode=True)

    def change_image_value(self, obj, file_name):
        """

        :param obj:
        :param file_name:
        :return:
        """

        if 'containers' in obj: return obj['containers']
        for k, v in obj.items():
            if isinstance(v, dict):
                item = self.change_image_value(v, file_name)
                if isinstance(item, list):
                    item[0]['image'] = self.new_image_name

        with io.open(file_name, 'w', encoding='utf8') as f:
            yaml.dump(obj, f, default_flow_style=False, allow_unicode=True)

    def change_versions(self):
        """

        :return:
        """

        for file in self.files:
            with open(file, 'r') as f:
                data = yaml.safe_load(f)
            self.change_role(data, file)
            self.change_image_value(data, file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', nargs="+", action='store', dest='files')
    parser.add_argument('-i', action='store', dest='new_image_name')
    parser.add_argument('-v', action='store', dest='version_label_key', default='role')
    args = parser.parse_args()
    BlueGreen(files=args.files, new_image_name=args.new_image_name,
              version_label_key=args.version_label_key).change_versions()
    print('Successfully changed.')