"""总体与样本：真实无放回抽样和样本均值的纯数学模型。"""
from fractions import Fraction
from itertools import combinations
import random

POPULATION = tuple(range(1, 21))
MEASUREMENTS = {individual: 50 + 2 * individual for individual in POPULATION}


def sample_without_replacement(population=POPULATION, size=6, seed=42):
    individuals = tuple(population)
    if len(individuals) == 0 or len(set(individuals)) != len(individuals):
        raise ValueError("总体必须非空且每个个体有唯一标识")
    if type(size) is not int or not 1 <= size <= len(individuals):
        raise ValueError("样本容量应是1到总体容量之间的整数")
    return tuple(sorted(random.Random(seed).sample(individuals, size)))


def sample_mean(measurements, sampled_ids):
    ids = tuple(sampled_ids)
    if not ids or len(set(ids)) != len(ids):
        raise ValueError("样本中个体必须非空且不重复")
    if any(individual not in measurements for individual in ids):
        raise ValueError("样本不能包含总体以外的个体")
    return Fraction(sum(measurements[individual] for individual in ids), len(ids))


def inclusion_probability(total, sample_size):
    """从N个互异个体均匀抽取容量n的子集时，每人的入样概率n/N。"""
    if type(total) is not int or type(sample_size) is not int or total < 1 or not 0 <= sample_size <= total:
        raise ValueError("要求整数N>=1和0<=n<=N")
    return Fraction(sample_size, total)


def all_equal_size_subsets(population, size):
    """仅用于小规模数学验证：每个大小相同的子集等可能。"""
    individuals = tuple(population)
    if len(set(individuals)) != len(individuals) or type(size) is not int or not 0 <= size <= len(individuals):
        raise ValueError("输入非法")
    return tuple(combinations(individuals, size))
