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
    folder_path = r"D:\公交适老化\建立经济性框架"
    # 确保文件夹存在
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 收集票制水平信息
    fare_system_level_info = {}
    fare_system_level_info['票制水平'] = get_input("请输入票制水平的评分（0到1之间，数值越大表示水平越高）：")
    save_to_file(fare_system_level_info, "票制水平.txt", folder_path)

    # 收集票制策略信息
    fare_system_strategy_info = {}
    fare_system_strategy_info['票制策略'] = get_input("请输入票制策略的评分（0到1之间，数值越大表示策略越合理）：")
    save_to_file(fare_system_strategy_info, "票制策略.txt", folder_path)

    # 收集特殊人群补贴信息
    special_group_subsidy_info = {}
    special_group_subsidy_info['特殊人群补贴'] = get_input("请输入特殊人群补贴的评分（0到1之间，数值越大表示补贴越充分）：")
    save_to_file(special_group_subsidy_info, "特殊人群补贴.txt", folder_path)

if __name__ == "__main__":
    main()