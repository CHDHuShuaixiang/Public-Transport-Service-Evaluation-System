import os
import json

def calculate_full_score(weights, framework, n):
    """计算单个框架的满分"""
    return n * 10 * weights[framework]

def write_full_scores_to_txt_file(score_folder_path, full_scores, total_full_score):
    """将满分得分以文本形式写入.txt文件"""
    file_name = '满分得分.txt'
    file_path = os.path.join(score_folder_path, file_name)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('各框架满分如下：\n')
        for framework, score in full_scores.items():
            f.write(f'{framework}: 满分为 {score:.2f}\n')
        f.write(f'\n总满分应为: {total_full_score:.2f}\n')

def write_full_scores_to_json_file(score_folder_path, full_scores, total_full_score):
    """将满分得分以JSON形式写入.json文件"""
    file_name = '满分得分.json'
    file_path = os.path.join(score_folder_path, file_name)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump({'full_scores': full_scores, 'total_full_score': total_full_score}, f, indent=4)

def main(base_folder_path):
    # 权重字典
    weights = {
        '便捷性': 0.1,
        '安全性': 0.38,
        '无障碍友好性': 0.3,
        '经济性': 0.16,
        '舒适性': 0.06
    }

    # 初始化满分字典和总满分
    full_scores = {}
    total_full_score = 0

    # 遍历每个框架文件夹
    for framework in ['安全性', '便捷性', '经济性', '舒适性', '无障碍友好性']:
        framework_path = os.path.join(base_folder_path, f'建立{framework}框架')
        # 统计该框架文件夹中txt文件的数量，忽略包含“-准则层得分计算”的文件
        n = sum(1 for file in os.listdir(framework_path) if file.endswith('.txt') and '准则层得分计算' not in file)
        # 计算该框架的满分
        full_score = calculate_full_score(weights, framework, n)
        # 存储满分到字典
        full_scores[framework] = full_score
        # 累加总满分
        total_full_score += full_score

    # 指定得分文件夹路径
    score_folder_path = os.path.join(base_folder_path, '公交体系得分')
    # 创建txt文件并写入满分得分
    write_full_scores_to_txt_file(score_folder_path, full_scores, total_full_score)
    # 创建json文件并写入满分得分
    write_full_scores_to_json_file(score_folder_path, full_scores, total_full_score)

if __name__ == "__main__":
    base_folder_path = r'D:\公交适老化'
    main(base_folder_path)