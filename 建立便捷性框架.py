import os

def get_input(prompt):
    """获取用户输入的浮点数值，并确保其在0到1之间"""
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 1:
                return value
            else:
                print("输入的数值不在0到1的范围内，请重新输入。")
        except ValueError:
            print("输入的不是数值，请输入一个0到1之间的浮点数。")

def save_to_file(data, file_name, folder_path):
    """将字典数据保存到指定路径下的txt文件中"""
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "w", encoding="utf-8") as file:
        for key, value in data.items():
            file.write(f"{key}：{value}\n")
    print(f"{file_name}信息已成功写入到文件中，文件路径为：{file_path}")

def main():
    # 指定文件夹路径
    folder_path = r"D:\公交适老化\建立便捷性框架"
    # 确保文件夹存在
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 收集接驳便捷性信息
    connectivity_info = {}
    connectivity_info['站台与目的地之间的间距是否小于400米'] = get_input("请输入站台与目的地之间的间距是否小于400米的评分（0到1之间，数值越大表示越便捷）：")
    connectivity_info['相邻换乘站之间的间距'] = get_input("请输入相邻换乘站之间的间距的评分（0到1之间，数值越大表示越便捷）：")
    connectivity_info['线路设置合理性(重点站之间换乘次数是否小于两次)'] = get_input("请输入线路设置合理性(重点站之间换乘次数是否小于两次)的评分（0到1之间，数值越大表示越合理）：")
    connectivity_info['换乘查询系统'] = get_input("请输入换乘查询系统的评分（0到1之间，数值越大表示系统越好）：")
    connectivity_info['换乘等待时间'] = get_input("请输入换乘等待时间的评分（0到1之间，数值越大表示等待时间越短）：")
    save_to_file(connectivity_info, "接驳便捷性.txt", folder_path)

    # 收集定制服务信息
    custom_service_info = {}
    custom_service_info['电话约车业务'] = get_input("请输入电话约车业务的评分（0到1之间，数值越大表示服务越好）：")
    custom_service_info['爱心专列公交'] = get_input("请输入爱心专列公交的评分（0到1之间，数值越大表示服务越好）：")
    save_to_file(custom_service_info, "定制服务.txt", folder_path)

    # 收集信息获取信息
    info_retrieval_info = {}
    info_retrieval_info['首末班车时间查询'] = get_input("请输入首末班车时间查询的评分（0到1之间，数值越大表示信息越容易获取）：")
    info_retrieval_info['车辆改线信息更新及时性'] = get_input("请输入车辆改线信息更新及时性的评分（0到1之间，数值越大表示更新越及时）：")
    info_retrieval_info['公交卡充值通知及时性'] = get_input("请输入公交卡充值通知及时性的评分（0到1之间，数值越大表示通知越及时）：")
    info_retrieval_info['车内拥挤程度获取'] = get_input("请输入车内拥挤程度获取的评分（0到1之间，数值越大表示信息越容易获取）：")
    info_retrieval_info['车辆到站信息获取'] = get_input("请输入车辆到站信息获取的评分（0到1之间，数值越大表示信息越容易获取）：")
    save_to_file(info_retrieval_info, "信息获取.txt", folder_path)

if __name__ == "__main__":
    main()