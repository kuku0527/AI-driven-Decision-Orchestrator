# 工具函数，可用于扩展
def normalize_score(score, min_val=0, max_val=10):
    return max(min(score, max_val), min_val)
