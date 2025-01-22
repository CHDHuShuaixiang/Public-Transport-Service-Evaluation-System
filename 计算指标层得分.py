import os


def calculate_score_in_file(file_path):
    total_sum = 0
    keyword_count = 0

    # 读取文件并计算总和以及关键字数量
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if "：" in line:
                parts = line.split("：")
                if len(parts) == 2:
                    try:
                        value = float(parts[1].strip())
                        total_sum += value
                        keyword_count += 1
                    except ValueError:
                        print(f"无法解析文件 {file_path} 中的数值。")

    # 计算得分
    score = total_sum * (10 / keyword_count) if keyword_count > 0 else 0

    return score, lines


def update_file_with_score(file_path, score):
    # 更新文件，添加得分
    with open(file_path, 'a', encoding='utf-8') as f:  # 使用 'a' 模式追加内容
        f.write(f"\n得分：{score:.2f}\n")


def main():
    folder_paths = {
        "便捷性": r"D:\公交适老化\建立便捷性框架",
        "安全性": r"D:\公交适老化\建立安全性框架",
        "无障碍友好性": r"D:\公交适老化\建立无障碍友好性框架",
        "经济性": r"D:\公交适老化\建立经济性框架",
        "舒适性": r"D:\公交适老化\建立舒适性框架"
    }

    for category, folder_path in folder_paths.items():
        files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        for file in files:
            file_path = os.path.join(folder_path, file)
            score, _ = calculate_score_in_file(file_path)
            update_file_with_score(file_path, score)
            print(f"{category} - {file} 的得分已更新。")


if __name__ == "__main__":
    main()