import yaml


def base_data_text(data, key):
    # with open(r"E:\工作\个人\Python学习资料\移动端测试\项目实战_百年奥莱\data\%s.yaml"% data, "r", encoding="utf-8")as f:
    with open(r"./data/%s.yaml" % data, "r", encoding="utf-8")as f:
        case_data = yaml.load(f, Loader=yaml.FullLoader)[key]
    arrs=[]
    for i in case_data.values():
        arrs.append(tuple(i.values()))
    return arrs


if __name__ == '__main__':
    ios = base_data_text('search_data', "test_search")
    print(ios)

