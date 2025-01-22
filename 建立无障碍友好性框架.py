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
    folder_path = r"D:\公交适老化\建立无障碍友好性框架"
    # 确保文件夹存在
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 收集车内无障碍设施信息
    accessibility_info = {}
    accessibility_info['车内是否有轮椅放置区'] = get_input("请输入车内是否有轮椅放置区的评分（0到1之间，数值越大表示越完善）：")
    accessibility_info['是否具备无障碍上下车方式'] = get_input("请输入是否具备无障碍上下车方式的评分（0到1之间，数值越大表示越便捷）：")
    accessibility_info['到站提醒是否及时'] = get_input("请输入到站提醒是否及时的评分（0到1之间，数值越大表示越及时）：")
    accessibility_info['车内是否有到站播报LED显示屏'] = get_input("请输入车内是否有到站播报LED显示屏的评分（0到1之间，数值越大表示越完善）：")
    accessibility_info['显示屏信息是否充足'] = get_input("请输入显示屏信息是否充足的评分（0到1之间，数值越大表示信息越充足）：")
    save_to_file(accessibility_info, "车内无障碍设施.txt", folder_path)

    # 收集语音播报系统信息
    announcement_system_info = {}
    announcement_system_info['站牌语音播报系统'] = get_input("请输入站牌语音播报系统的评分（0到1之间，数值越大表示越好）：")
    announcement_system_info['车内语音播报系统'] = get_input("请输入车内语音播报系统的评分（0到1之间，数值越大表示越好）：")
    announcement_system_info['播报音量与清晰度'] = get_input("请输入播报音量与清晰度的评分（0到1之间，数值越大表示越好）：")
    announcement_system_info['车辆到站播报及时性'] = get_input("请输入车辆到站播报及时性的评分（0到1之间，数值越大表示越好）：")
    announcement_system_info['语音播报智能化程度'] = get_input("请输入语音播报智能化程度的评分（0到1之间，数值越大表示越智能）：")
    save_to_file(announcement_system_info, "语音播报系统.txt", folder_path)

    # 收集服务人员信息
    service_staff_info = {}
    service_staff_info['司机驾驶习惯'] = get_input("请输入司机驾驶习惯的评分（0到1之间，数值越大表示越好）：")
    service_staff_info['驾驶员服务态度'] = get_input("请输入驾驶员服务态度的评分（0到1之间，数值越大表示越好）：")
    service_staff_info['咨询台服务态度'] = get_input("请输入咨询台服务态度的评分（0到1之间，数值越大表示越好）：")
    service_staff_info['是否有专业乘务员'] = get_input("请输入是否有专业乘务员的评分（0到1之间，数值越大表示服务越专业）：")
    service_staff_info['乘车服务质量'] = get_input("请输入乘车服务质量的评分（0到1之间，数值越大表示质量越高）：")
    save_to_file(service_staff_info, "服务人员.txt", folder_path)

if __name__ == "__main__":
    main()