import numpy as np
def uniform_weight(distance):
    """
    均匀权重函数。为所有点提供相同的权重。

    参数:
    distance -- numpy数组，包含从当前点到邻居点的距离。

    返回:
    一个所有元素都为1的numpy数组，与输入数组同形状。
    """
    return np.ones_like(distance)
def inverse_distance_weight(distance, power=1):
    """
    距离反比权重函数。根据距离的反比例来计算权重。

    参数:
    distance -- numpy数组，包含从当前点到邻居点的距离。
    power -- 控制衰减速率的幂次参数，默认为1。

    返回:
    一个根据距离反比例计算得出的权重数组。
    """
    with np.errstate(divide='ignore', invalid='ignore'):
        return 1 / np.power(distance, power)
def epanechnikov_kernel(distance, kernel_width=1.0):
    """
    Epanechnikov核权重函数。在一定范围内提供权重，超出这个范围权重急剧下降。

    参数:
    distance -- numpy数组，包含从当前点到邻居点的距离。
    kernel_width -- 核宽度参数，控制有效邻域的大小。

    返回:
    根据Epanechnikov核计算的权重数组。
    """
    scaled_distance = (distance / kernel_width) ** 2
    mask = scaled_distance < 1
    return 0.75 * (1 - scaled_distance) * mask
def cubic_spline_weight(distance, kernel_width=1.0):
    """
    三次样条权重函数。使用三次样条函数计算权重，提供平滑的权重变化。

    参数:
    distance -- numpy数组，包含从当前点到邻居点的距离。
    kernel_width -- 核宽度参数，影响权重变化的范围。

    返回:
    根据三次样条函数计算的权重数组。
    """
    q = np.abs(distance / kernel_width)
    weights = np.zeros_like(q)
    mask1 = q <= 0.5
    mask2 = (q > 0.5) & (q <= 1.0)
    weights[mask1] = 2/3 - 4 * q[mask1] ** 2 + 4 * q[mask1] ** 3
    weights[mask2] = 4/3 - 4 * q[mask2] + 4 * q[mask2] ** 2 - (4/3) * q[mask2] ** 3
    return weights
def wendland_weight(distance, kernel_width=1.0):
    """
    Wendland权重函数。使用Wendland函数计算局部光滑的权重。

    参数:
    distance -- numpy数组，包含从当前点到邻居点的距离。
    kernel_width -- 核宽度参数，决定权重衰减的速度和范围。

    返回:
    根据Wendland函数计算的权重数组。
    """
    q = distance / kernel_width
    mask = q < 1
    return ((1 - q) ** 4) * (4 * q + 1) * mask
def shepard_weight(distance, power=2):
    """
    Shepard权重函数。使用距离的负幂计算权重，权重随距离增大而减小。

    参数:
    distance -- numpy数组，包含从当前点到邻居点的距离。
    power -- 幂参数，控制权重衰减的速率。

    返回:
    根据Shepard方法计算的权重数组。
    """
    with np.errstate(divide='ignore', invalid='ignore'):
        weights = 1 / np.power(distance, power)
        weights[distance == 0] = np.inf  # 当距离为0时处理除以0的情况
        return weights


# 定义高斯权重函数
def gaussian_weight(distance, bandwidth):
    """
    高斯权重函数。根据距离计算权重，权重随距离增大而减小。
    参数:
    distance -- numpy数组，包含从当前点到邻居点的距离。
    bandwidth -- 带宽参数，控制权重衰减的范围。
    返回:
    根据高斯函数计算的权重数组。
    """
    return np.exp(-0.5 * (distance / bandwidth) ** 2)
def encode_rgb(length, points):
    # rgb编码
    xyz = points[:, :3]  # 位置
    color = points[:, 3:6]  # 颜色
    color_tmp = []
    for i in range(color.shape[0]):
        color_tmp.append([int(color[i, 0]) << 16 | int(color[i, 1]) << 8 | int(color[i, 2])])  # 颜色重新编码
    if length == 4:
        ep_points = np.concatenate((xyz, np.asarray(color_tmp)), axis=1)  # 拼接位置信息和颜色信息

    if length == 7:
        nxyz = points[:, 6:]
        ep_points = np.concatenate((xyz, np.asarray(color_tmp), nxyz), axis=1)  # 拼接位置信息和颜色信息
    return ep_points
def decode_rgb(rgb):
    # rgb解码
    r = (rgb >> 16) & 0x0000ff
    g = (rgb >> 8) & 0x0000ff
    b = (rgb) & 0x0000ff
    return [r, g, b]

def processing_str(input, s, length):
    """功能：输入一个字符、将其增加到length长度"""
    for i in range(length):
        input += " "
        input += str(s)
    return input


def write_file(save_path, pcd_init, points, mode):
    with open(save_path, mode=mode) as f:
        if pcd_init:
            for i in pcd_init:
                f.write(pcd_init[i] + '\n')
        np.savetxt(f, points, delimiter=' ', fmt='%.8e')
        
def get_head(points, color, normal, _SIZE, _TYPE, _COUNT, _HEIGHT, _VIEWPOINT, _DATA, pcd_head, VERSION):
    if color == True and normal == False:
        length = 4
        TYPE = processing_str("TYPE", _TYPE, length - 1) + ' U'
        FIELDS = "FIELDS x y z rgb"
        points = encode_rgb(length, points)

    if color == False and normal == False:
        length = 3
        TYPE = processing_str("TYPE", _TYPE, length)
        FIELDS = "FIELDS x y z"
    if color == False and normal == True:
        length = 6
        TYPE = processing_str("TYPE", _TYPE, length)
        FIELDS = "FIELDS x y z nx ny nz"
    if color == True and normal == True:
        length = 7
        TYPE = processing_str("TYPE", _TYPE, length - 4) + " U" + processing_str("", _TYPE,
                                                                                           length - 4)
        FIELDS = "FIELDS x y z rgb nx ny nz"
        points = encode_rgb(length, points)
    pcd_init = {
        "pcd_head": pcd_head,
        "VERSION": VERSION,
        "FIELDS": FIELDS,
        "SIZE": processing_str("SIZE", _SIZE, length),
        "TYPE": TYPE,
        "COUNT": processing_str("COUNT", _COUNT, length),
        "WIDTH": "WIDTH " + str(len(points)),
        "HEIGHT": 'HEIGHT ' + str(_HEIGHT),
        "VIEWPOINT": 'VIEWPOINT ' + str(_VIEWPOINT),
        "POINTS": "POINTS " + str(len(points)),
        "DATA": 'DATA ' + str(_DATA)
    }
    return pcd_init


def file_is_empty(file_name):
    try:
        # 尝试以读模式打开文件来检查内容
        with open(file_name, 'r') as f:
            if f.read():
                return False
    except FileNotFoundError:
        # 文件不存在，可以视为“空”
        pass
    # 文件不存在或为空
    return True

def choose_weight(weights_name, distances, tau):
    try:
        if weights_name == "gaussian":
            weights = gaussian_weight(distances, tau)
        if weights_name == "epanechnikov":
            weights = epanechnikov_kernel(distances, tau)
        if weights_name == "cubic_spline":
            weights = cubic_spline_weight(distances, tau)
        if weights_name == "uniform":
            weights = uniform_weight(distances)
        if weights_name == "inverse_distance":
            weights = inverse_distance_weight(distances, tau)
        if weights_name == "wendland":
            weights = wendland_weight(distances, tau)
        if weights_name == "shepard_weight":
            weights = shepard_weight(distances, tau)
    except:
        weights = gaussian_weight(distances, tau)
    return weights