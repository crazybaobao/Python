# 遍历json字串

import json
import re

count = 0


def dict_generator(indict):
    global count
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                count += 1
                print(value)
                print("子节点个数是：" + str(count))
                return dict_generator(value)
            else:
                count = 0
                return dict_generator(value)

    #
    #             if len(value) == 0:
    #                 yield pre + [key, '{}']
    #             else:
    #                 count = count + 1
    #                 print("子节点深度为", count)
    #                 for d in dict_generator(value, pre + [key]):
    #                     yield d
    #         elif isinstance(value, list):
    #             if len(value) == 0:
    #                 yield pre + [key, '[]']
    #             else:
    #                 for v in value:
    #                     for d in dict_generator(v, pre + [key]):
    #                         yield d
    #         elif isinstance(value, tuple):
    #             if len(value) == 0:
    #                 yield pre + [key, '()']
    #             else:
    #                 for v in value:
    #                     for d in dict_generator(v, pre + [key]):
    #                         yield d
    #         else:
    #             yield pre + [key, value]
    # else:
    #     yield indict


if __name__ == "__main__":
    sJOSN = {
        "A的第一层": {
            "A的第二层-1": {
                "A的第三层-1": "苹果",
                "A的第三层-2": "香蕉",
                "A的第三层-3": {
                    "A的第四层-1": "嘿嘿嘿"
                },
            },
            "A的第二层-2": {
                "value": "白色",
                "inherit": "红色",
                "global": "蓝色"
            }
        },
        "B的第一层": {
            "B的第二层": [{
                "gid": "0",
            }]
        }
    }
    JOSN = re.sub('\'', '\"', str(sJOSN))
    sValue = json.loads(str(JOSN))
    dict_generator(sValue)
