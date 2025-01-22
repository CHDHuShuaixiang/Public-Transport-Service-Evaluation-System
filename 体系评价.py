import os
import json

def read_full_scores_from_json(file_path):
    """从JSON文件中读取满分得分"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            scores_data = json.load(file)
            return scores_data['full_scores'], scores_data['total_full_score']
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
        exit(1)
    except json.JSONDecodeError:
        print(f"文件内容格式错误，应为JSON格式: {file_path}")
        exit(1)

def calculate_framework_score(framework_score, total_full_score):
    """计算单个框架的实际得分"""
    return (framework_score / total_full_score) * 100

def read_score_from_file(file_path):
    """从文件中读取得分"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            line = file.readline().strip()
            # 假设文件的第一行就是得分信息，格式为 "一级指标得分总和：1.58"
            score_str = line.split("：")[1]  # 注意这里使用的是中文冒号
            return float(score_str)
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
        return None
    except ValueError as e:
        print(f"文件内容格式错误: {file_path}\n{e}")
        return None

def main(base_path):
    # 定义路径
    full_score_path = os.path.join(base_path, "公交体系得分", "满分得分.json")
    result_path = os.path.join(base_path, "公交体系得分", "体系得分计算.txt")
    frameworks = ["安全性", "便捷性", "经济性", "舒适性", "无障碍友好性"]

    # 读取满分得分
    full_scores, total_full_score = read_full_scores_from_json(full_score_path)

    # 初始化变量
    total_system_score = 0  # 公交系统评分总和
    individual_scores = {}  # 存储每个框架的实际得分

    # 遍历每个框架文件夹
    for framework in frameworks:
        framework_folder = f"建立{framework}框架"
        score_file_path = os.path.join(base_path, framework_folder, f"{framework}-准则层得分计算.txt")
        score_sum = read_score_from_file(score_file_path)
        if score_sum is not None:
            actual_score = calculate_framework_score(score_sum, total_full_score)
            individual_scores[framework] = actual_score
            total_system_score += actual_score  # 累加到公交系统评分

    # 将各框架评分和公交系统评分写入文件
    with open(result_path, 'w', encoding='utf-8') as file:
        file.write("各框架实际得分如下：\n")
        for framework, score in individual_scores.items():
            file.write(f"{framework}: {score:.2f}\n")
        file.write(f"\n公交系统评分: {total_system_score:.2f}\n")

    print(f"公交服务评价体系得分已计算并写入 {result_path}")

if __name__ == "__main__":
    base_path = "D:\\公交适老化"
    main(base_path)