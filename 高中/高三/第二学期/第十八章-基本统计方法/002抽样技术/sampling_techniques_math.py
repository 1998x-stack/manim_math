"""40名互异个体中三类抽样的独立数学模型，随机数生成器仅局部使用。"""
from fractions import Fraction
import random

POPULATION = tuple(range(1, 41))
LAYERS = (tuple(range(1, 21)), tuple(range(21, 33)), tuple(range(33, 41)))
ALLOCATIONS = (5, 3, 2)


def simple_random(population=POPULATION, size=5, seed=7):
    members = tuple(population)
    if not members or len(set(members)) != len(members) or type(size) is not int or not 1 <= size <= len(members):
        raise ValueError("总体须非空且个体互异；样本量为合法正整数")
    return tuple(sorted(random.Random(seed).sample(members, size)))


def systematic(population=POPULATION, size=5, start=4):
    """等分 N=n*k，先在首段1..k等可能随机选择起点，之后等距选 n 人。"""
    members = tuple(population)
    n = len(members)
    if not members or len(set(members)) != n or type(size) is not int or size <= 0 or n % size:
        raise ValueError("总体个体互异且容量必须可被样本量整除")
    gap = n // size
    if type(start) is not int or not 1 <= start <= gap:
        raise ValueError("起点必须是首段中的1到k")
    return tuple(members[start - 1 + index * gap] for index in range(size))


def random_systematic(population=POPULATION, size=5, seed=13):
    members = tuple(population)
    if type(size) is not int or size <= 0 or len(members) % size:
        raise ValueError("系统抽样的样本量必须整除总体容量")
    start = random.Random(seed).randrange(1, len(members) // size + 1)
    return start, systematic(members, size, start)


def stratified(layers=LAYERS, allocations=ALLOCATIONS, seed=19):
    """在互不重叠的层内分别等可能无放回抽样。"""
    layers = tuple(tuple(layer) for layer in layers)
    alloc = tuple(allocations)
    if not layers or len(layers) != len(alloc):
        raise ValueError("各层与分配样本量必须一一对应")
    all_members = tuple(member for layer in layers for member in layer)
    if len(set(all_members)) != len(all_members):
        raise ValueError("分层必须互不重叠")
    rng = random.Random(seed)
    draws = []
    for layer, size in zip(layers, alloc):
        if not layer or type(size) is not int or not 0 <= size <= len(layer):
            raise ValueError("层容量和分配量非法")
        draws.append(tuple(sorted(rng.sample(layer, size))))
    return tuple(draws)


def allocation_rates(layers=LAYERS, allocations=ALLOCATIONS):
    if len(layers) != len(allocations) or not layers:
        raise ValueError("各层必须配有样本容量")
    if any(not layer or type(count) is not int or not 0 <= count <= len(layer)
           for layer, count in zip(layers, allocations)):
        raise ValueError("层容量或样本容量非法")
    return tuple(Fraction(count, len(layer)) for layer, count in zip(layers, allocations))
