from zkyutils.logger import log


# 批量获取用户输入 留空结束
@log.log_decorator('批量获取用户输入')
def get_input_list(msg, end_tag=''):
    input_list = []
    data = input(msg)
    while data != end_tag:
        input_list.append(data)
        data = input('')
    return input_list


@log.log_decorator('用户输入选项')
def get_input_options(msg: str, options: list):
    print(msg)
    for index, option in enumerate(options):
        print(f'{index + 1}. {option}')
    data = input('请输入序号：')
    while True:
        if not data.isdigit():
            data = input('输入内容非序号，请重新输入：')
            continue
        data = int(data)
        if data < 1 or data > len(options):
            data = input('输入的序号不在选项范围中，请重新输入：')
            continue
        break
    return data - 1


@log.log_decorator('用户输入bool')
def get_input_bool(msg, true_str='是', false_str='否'):
    options = [true_str, false_str]
    index = get_input_options(msg, options)
    if index == 0:
        return True
    else:
        return False
