import os
import re
import json
from operator import itemgetter

# 获取所有JSON文件列表
json_files = [f for f in os.listdir('members') if f.endswith('.json')]

# 读取JSON文件并排序
data_list = []
for json_file in json_files:
    with open(os.path.join('members', json_file), 'r', encoding='utf-8') as file:
        data = json.load(file)
        data_list.append(data)

# 按created_at字段升序排序
sorted_data = sorted(data_list, key=itemgetter('created_at'))

# 在单独出现的换行前面补空格
def add_space_before_newline(s):
    return re.sub(r'(?<!(  |\r\n))\r\n(?![\r\n])', '  \r\n', s)

# 生成README.md文件
with open('README.md', 'w', encoding='utf-8') as readme:
    # 读取模板文件内容
    with open('.github/scripts/template.md', 'r', encoding='utf-8') as template:
        readme.write(template.read())
    
    for item in sorted_data:
        # 写入分页符和内容
        readme.write('\n---\n\n')
        readme.write(add_space_before_newline(item['content']) + '\n')
