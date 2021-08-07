import json
import os

class Setting():
    ful_path_setting = os.path.join(os.getcwd() + '/setting/', 'setting.json')
    setting = open(ful_path_setting, 'r')
    get_json = json.load(setting)

    full_path_first = os.path.join(os.getcwd() + '/setting/', 'first.json')
    setting_first = open(full_path_first, 'r')
    get_json_data = json.load(setting_first)

    def get_width(self):
        width = Setting.get_json['width']
        return int(width)

    def get_height(self):
        height = Setting.get_json['height']
        return int(height)
    
    def get_first_start(self):
        first_start = Setting.get_json_data['first_start']
        return int(first_start)

    def set_first_start(self):
        set_yes = {"first_start": 0}
        json_file = json.dumps(set_yes)
        file_setting = open(Setting.full_path_first, 'w')
        file_setting.write(json_file)
