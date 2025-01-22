import os


def calculate_total_score(folder_path, weight):
    total_score = 0
    files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

    for file in files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if "得分" in line:
                    parts = line.split("：")
                    if len(parts) == 2:
                        try:
                            score = float(parts[1].strip().replace('\n', ''))
                            total_score += score
                        except ValueError:
                            print(f"无法解析文件 {file} 中的得分。")

    # 计算加权得分
    weighted_score = total_score * weight
    return weighted_score


def save_total_score(folder_path, total_score, category):
    score_file = f"{category}-准则层得分计算.txt"
    with open(os.path.join(folder_path, score_file), 'w', encoding='utf-8') as f:
        f.write(f"一级指标得分总和：{total_score:.2f}\n")


def main():
    folder_paths = {
        "便捷性": r"D:\公交适老化\建立便捷性框架",
        "安全性": r"D:\公交适老化\建立安全性框架",
        "无障碍友好性": r"D:\公交适老化\建立无障碍友好性框架",
        "经济性": r"D:\公交适老化\建立经济性框架",
        "舒适性": r"D:\公交适老化\建立舒适性框架"
    }
    weights = {
        "便捷性": 0.1,
        "安全性": 0.38,
        "无障碍友好性": 0.3,
        "经济性": 0.16,
        "舒适性": 0.06
    }

    for category, folder_path in folder_paths.items():
        weight = weights[category]
        total_score = calculate_total_score(folder_path, weight)
        save_total_score(folder_path, total_score, category)
        print(f"{category} 的一级指标加权得分总和已计算并保存。")


if __name__ == "__main__":
    main()