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
    folder_path = r"D:\公交适老化\建立舒适性框架"
    # 确保文件夹存在
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # 收集站台环境信息
    station_info = {}
    station_info['是否有港湾式站台'] = get_input("请输入是否有港湾式站台的评分（0表示没有，1表示有）：")
    station_info['是否有符合坡度条件的无障碍坡道'] = get_input("请输入是否有符合坡度条件的无障碍坡道的评分（0表示没有，1表示有）：")
    station_info['重点站台有无人工咨询台'] = get_input("请输入重点站台有无人工咨询台的评分（0表示没有，1表示有）：")
    station_info['站台宽度与利用率'] = get_input("请输入站台宽度与利用率的评分（0到1之间，数值越大表示越宽或利用率越高）：")
    station_info['站台卫生状况'] = get_input("请输入站台卫生状况的评分（0到1之间，数值越大表示卫生状况越好）：")
    save_to_file(station_info, "站台环境.txt", folder_path)

    # 收集遮阳棚与座椅设施信息
    shelter_seat_info = {}
    shelter_seat_info['是否有遮阳棚'] = get_input("请输入是否有遮阳棚的评分（0表示没有，1表示有）：")
    shelter_seat_info['是否有座椅'] = get_input("请输入是否有座椅的评分（0表示没有，1表示有）：")
    shelter_seat_info['遮阳棚的顶棚宽度是否能对重点时间段进行有效遮挡'] = get_input("请输入遮阳棚的顶棚宽度是否能对重点时间段进行有效遮挡的评分（0到1之间，数值越大表示遮挡效果越好）：")
    shelter_seat_info['顶棚是否具备有效的遮雨效果'] = get_input("请输入顶棚是否具备有效的遮雨效果的评分（0到1之间，数值越大表示遮雨效果越好）：")
    shelter_seat_info['重点站台是否有轮椅等候区'] = get_input("请输入重点站台是否有轮椅等候区的评分（0表示没有，1表示有）：")
    save_to_file(shelter_seat_info, "遮阳棚与座椅设施.txt", folder_path)

    # 收集站牌设施信息
    sign_info = {}
    sign_info['站牌字体大小'] = get_input("请输入站牌字体大小的评分（0到1之间，数值越大表示字体越大）：")
    sign_info['站牌高度是否合理'] = get_input("请输入站牌高度是否合理的评分（0到1之间，数值越大表示高度越合理）：")
    sign_info['站牌能否显示车辆到站'] = get_input("请输入站牌能否显示车辆到站的评分（0表示不能，1表示能）：")
    sign_info['线路变化时站牌能否及时更新'] = get_input("请输入线路变化时站牌能否及时更新的评分（0表示不能，1表示能）：")
    sign_info['站牌损坏程度'] = get_input("请输入站牌损坏程度的评分（0到1之间，数值越大表示损坏程度越低）：")
    save_to_file(sign_info, "站牌设施.txt", folder_path)

    # 收集车内设施信息
    interior_info = {}
    interior_info['车内座椅方向是否合理'] = get_input("请输入车内座椅方向是否合理的评分（0到1之间，数值越大表示方向越合理）：")
    interior_info['车内座椅高度合理程度'] = get_input("请输入车内座椅高度合理程度的评分（0到1之间，数值越大表示高度越合理）：")
    interior_info['车内是否配有低矮扶手，使老年人便于抓扶'] = get_input("请输入车内是否配有低矮扶手，使老年人便于抓扶的评分（0表示没有，1表示有）：")
    interior_info['是否有便于放置行李的置物架或挂钩'] = get_input("请输入是否有便于放置行李的置物架或挂钩的评分（0表示没有，1表示有）：")
    interior_info['车内是否有路线显示，站点信息是否清晰'] = get_input("请输入车内是否有路线显示，站点信息是否清晰的评分（0表示没有或不清晰，1表示有且清晰）：")
    save_to_file(interior_info, "车内设施.txt", folder_path)

    # 收集车内环境信息
    interior_env_info = {}
    interior_env_info['车内卫生状况'] = get_input("请输入车内卫生状况的评分（0到1之间，数值越大表示卫生状况越好）：")
    interior_env_info['车内满载率'] = get_input("请输入车内满载率的评分（0到1之间，数值越小表示满载率越低）：")
    interior_env_info['车内是否漏水'] = get_input("请输入车内是否漏水的评分（0表示漏水，1表示不漏水）：")
    interior_env_info['座椅、扶手是否有损坏'] = get_input("请输入座椅、扶手是否有损坏的评分（0表示损坏严重，1表示完好无损）：")
    interior_env_info['车内是否有无障碍设施'] = get_input("请输入车内是否有无障碍设施的评分（0表示没有，1表示有）：")
    save_to_file(interior_env_info, "车内环境.txt", folder_path)

if __name__ == "__main__":
    main()