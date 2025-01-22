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
    folder_path = r"D:\公交适老化\建立安全性框架"
    # 确保文件夹存在
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 收集车辆运行安全性信息
    vehicle_safety_info = {}
    vehicle_safety_info['车辆行驶时速'] = get_input("请输入车辆行驶时速的评分（0到1之间，数值越大表示越安全）：")
    vehicle_safety_info['司机驾驶习惯'] = get_input("请输入司机驾驶习惯的评分（0到1之间，数值越大表示习惯越好）：")
    vehicle_safety_info['公交优先通行优先'] = get_input("请输入公交优先通行优先的评分（0到1之间，数值越大表示越优先）：")
    vehicle_safety_info['转弯播报'] = get_input("请输入转弯播报的评分（0到1之间，数值越大表示播报越及时）：")
    vehicle_safety_info['车辆行驶是否跟车过近'] = get_input("请输入车辆行驶是否跟车过近的评分（0表示过近，1表示安全距离）：")
    save_to_file(vehicle_safety_info, "车辆运行安全性.txt", folder_path)

    # 收集站台候车安全性信息
    platform_safety_info = {}
    platform_safety_info['站台距离机动车道距离'] = get_input("请输入站台距离机动车道距离的评分（0到1之间，数值越大表示越安全）：")
    platform_safety_info['站台距离非机动车道距离'] = get_input("请输入站台距离非机动车道距离的评分（0到1之间，数值越大表示越安全）：")
    platform_safety_info['站台是否高于车道'] = get_input("请输入站台是否高于车道的评分（0表示不高于，1表示高于）：")
    platform_safety_info['站台距离路侧的距离'] = get_input("请输入站台距离路侧的距离的评分（0到1之间，数值越大表示越安全）：")
    platform_safety_info['站台是否明显'] = get_input("请输入站台是否明显的评分（0表示不明显，1表示明显）：")
    save_to_file(platform_safety_info, "站台候车安全性.txt", folder_path)

    # 收集上下车安全性信息
    boarding_safety_info = {}
    boarding_safety_info['发车加速度'] = get_input("请输入发车加速度的评分（0到1之间，数值越大表示越平稳）：")
    boarding_safety_info['停车加速度'] = get_input("请输入停车加速度的评分（0到1之间，数值越大表示越平稳）：")
    boarding_safety_info['停车位置与站台距离'] = get_input("请输入停车位置与站台距离的评分（0到1之间，数值越大表示越接近）：")
    boarding_safety_info['转弯加速度'] = get_input("请输入转弯加速度的评分（0到1之间，数值越大表示越平稳）：")
    boarding_safety_info['上下车是否便捷'] = get_input("请输入上下车是否便捷的评分（0到1之间，数值越大表示越便捷）：")
    save_to_file(boarding_safety_info, "上下车安全性.txt", folder_path)

if __name__ == "__main__":
    main()