# -*- coding: UTF-8 -*-
'''
@Project ：easypcd
@File    ：easypcd.py
@Author  ：王泽辉
@Date    ：2023-12-08 15:49
'''
import numpy as np
from scipy.spatial import KDTree
import easypcd.utils as utils


class DotDict(dict):
    def __init__(self, *args, **kwargs):
        super(DotDict, self).__init__(*args, **kwargs)

    def __getattr__(self, key):
        value = self[key]
        if isinstance(value, dict):
            value = DotDict(value)
        return value


class ep():
    def __init__(self):
        self.format_dic = {0: 'pcd', 1: "txt"}
        self.pcd_head = '# .PCD v0.7 - Point Cloud Data file format'
        self.VERSION = 'VERSION 0.7'

    def read_pcd(self, pcd_file):
        """功能：读取pcd文件
        pcd_file：输入读取pcd文件的路径
        """
        format_type = {"I": np.int32, "U": np.uint, "F": np.float32}
        pcd_data = []
        pcd_information = {}
        with open(pcd_file, 'r') as f:
            lines = f.readlines()
            for i in lines[1:11]:
                info = list(i.strip('\n').split(' '))
                if len(info) > 2:
                    info_line = [info[0], ' '.join(info[1:])]
                else:
                    info_line = info
                pcd_information.update({info_line[0]: info_line[1]})
            pcd_type = pcd_information['TYPE'].split(" ")
            for line in lines[11:]:
                line = list(line.strip('\n').split(' '))
                if line == ['']:
                    pass
                else:
                    tmp = []
                    for i in range(len(line)):
                        tmp.append(format_type[pcd_type[i]](line[i]))
                    pcd_data.append(tmp)
            points = np.array(pcd_data)

            pcd_information.update({"points": points})
        return DotDict(pcd_information)

    def contract_point_list(self, point_list):
        """
        将如下的数组进行拼接
        [array([[-710.34927002, -237.10757877,  215.2757621 ],
                [-709.46899019, -236.99056383,  214.81596639]]),
        array([[-708.6379193 , -238.05448845,  219.71073159],
               [-706.88288009, -237.81858778,  218.7811006 ]]),
        array([[-707.06327968, -239.84758949,  222.8262728 ],
               [-706.18809347, -239.72758696,  222.35760756]])]
        返回：
        [array(
                [-710.34927002, -237.10757877,  215.2757621 ],
                [-709.46899019, -236.99056383,  214.81596639],
                [-708.6379193 , -238.05448845,  219.71073159],
                [-706.88288009, -237.81858778,  218.7811006 ],
                [-707.06327968, -239.84758949,  222.8262728 ],
                [-706.18809347, -239.72758696,  222.35760756]
                )]
        """
        for p in point_list:
            p = list(p)
            if len(p) == 0:
                point_list.remove(p)
        points_tmp = point_list[0]
        for i in range(1, len(point_list)):
            points_tmp = np.concatenate((points_tmp, point_list[i]), axis=0)
        return points_tmp


    def write_pcd(self, save_name, points, color=False, normal=False, _SIZE=4,
                  _TYPE="F", _COUNT=1, _HEIGHT=1, _VIEWPOINT='0 0 0 1 0 0 0', _DATA='ascii', mode='w'):
        """功能：写入pcd文件
            必要参数：
                save_name:保存的文件名
                points：需要保存的点云数据

            可选参数
                color：是否有颜色信息（True/False），默认False
                normal：是否有向量信息（True/False），默认False
                _SIZE：字节数量，默认为4
                _TYPE：字符类型，默认为F
                _DATA：编码格式
                mode:
                'w':覆盖写入
                'a'追加写入
        """
        if mode == 'w':
            try:
                pcd_init = utils.get_head(points, color, normal, _SIZE, _TYPE, _COUNT, _HEIGHT, _VIEWPOINT, _DATA, self.pcd_head, self.VERSION)
                utils.write_file(save_name, pcd_init, points, mode='w')

            except:
                assert "一个未知的错误！"
        if mode == 'a':
            try:
                if utils.file_is_empty(save_name):# 当文件为空时，直接写入
                    pcd_init = utils.get_head(points, color, normal, _SIZE, _TYPE, _COUNT, _HEIGHT, _VIEWPOINT, _DATA, self.pcd_head, self.VERSION)
                    # 文件为空，写入pcd_init和points
                    utils.write_file(save_name, pcd_init, points, 'a')
                else:# 当文件不为空时，将新点云与旧点云合并
                    pcd_file = self.read_pcd(save_name)
                    new_points = self.contract_point_list([pcd_file['points'], points])
                    pcd_init = utils.get_head(new_points, color, normal, _SIZE, _TYPE, _COUNT, _HEIGHT, _VIEWPOINT, _DATA, self.pcd_head, self.VERSION)
                    utils.write_file(save_name, pcd_init, points=new_points, mode='w')
            except:
                assert "一个未知的错误！"
    def write_txt(self, save_name, points):
        """功能：写入txt文件
            save_name:保存的文件名
            points：需要保存的点云数据
        """
        with open(save_name, mode='w') as f:
            for line in points:
                for p in line:
                    p = str(int(p))
                    f.write(p)
                    f.write(" ")
                f.write("\n")

    def Moving_Least_Squares_UpSampling(self, points, radius, tau, upsampling_rate=2, setUpsamplingRadius=1.0,
                                      weights_name='gaussian'):
        """
        功能：使用Moving Least Squares Upsampling进行点云的Upsampling
        必要参数：
            points: 点云数据[[x1,y1,z1],[x2,y2,z2],...,[xn,yn,zn]]
            radius: 邻居搜索半径
            tau: 权重系数
            upsampling_rate: 采样率，每个点周围采样几次
            setUpsamplingRadius: 采样半径
        可选参数：
            weights_name: 权重函数，可选：
            gaussian:高斯权重函数。根据距离计算权重，权重随距离增大而减小。
            epanechnikov:Epanechnikov核权重函数。在一定范围内提供权重，超出这个范围权重急剧下降。
            cubic_spline:三次样条权重函数。使用三次样条函数计算权重，提供平滑的权重变化。
            uniform:均匀权重函数。为所有点提供相同的权重。
            inverse_distance:距离反比权重函数。根据距离的反比例来计算权重。
            wendland:Wendland权重函数。使用Wendland函数计算局部光滑的权重。
            shepard_weight:Shepard权重函数。使用距离的负幂计算权重，权重随距离增大而减小。
        """
        x = points[:, 0]
        y = points[:, 1]
        z = points[:, 2]
        # 构建KD树以快速找到邻居
        tree = KDTree(np.vstack((x, y, z)).T)
        new_points = []
        for xi, yi, zi in zip(x, y, z):
            # 使用KD树找到指定半径内的所有邻居
            idx = tree.query_ball_point([xi, yi, zi], r=radius)

            # 获取邻居点
            x_neigh = x[idx]
            y_neigh = y[idx]
            z_neigh = z[idx]
            # 计算权重
            # 计算邻居点到当前点的距离
            distances = np.sqrt((x_neigh - xi) ** 2 + (y_neigh - yi) ** 2 + (z_neigh - zi) ** 2)
            weights = utils.choose_weight(weights_name, distances, tau)

            # 二次曲面拟合: z = ax^2 + by^2 + cxy + dx + ey + f
            # 构建加权最小二乘问题
            A = np.vstack(
                [x_neigh ** 2 * weights, y_neigh ** 2 * weights, x_neigh * y_neigh * weights, x_neigh * weights,
                 y_neigh * weights, weights]).T
            b = z_neigh * weights

            # 解线性方程组得到拟合参数
            fit_params = np.linalg.lstsq(A, b, rcond=None)[0]

            # 在当前点附近生成新点
            for _ in range(int(upsampling_rate)):
                new_x = np.random.uniform(xi - setUpsamplingRadius / 2, xi + setUpsamplingRadius / 2)
                new_y = np.random.uniform(yi - setUpsamplingRadius / 2, yi + setUpsamplingRadius / 2)
                new_z = fit_params[0] * new_x ** 2 + fit_params[1] * new_y ** 2 + fit_params[2] * new_x * new_y + \
                        fit_params[3] * new_x + fit_params[4] * new_y + fit_params[5]
                new_points.append([new_x, new_y, new_z])
        result = self.contract_point_list([points, new_points])
        return np.array(result)
    def Moving_Least_Squares_Smoothing(self, points, radius, tau, weights_name='gaussian'):
        """
        功能：使用Moving Least Squares Smooth进行点云的平滑
        必要参数：
            points: 点云数据[[x1,y1,z1],[x2,y2,z2],...,[xn,yn,zn]]
            radius: 邻居搜索半径
            tau: 权重系数
        可选参数：
            weights_name: 权重函数，可选：
            gaussian:高斯权重函数。根据距离计算权重，权重随
            epanechnikov:Epanechnikov核权重函数。在一定范围内提供权重，超出这个范围权重急剧下降。
            cubic_spline:三次样条权重函数。使用三次样条函数计算权重，提供平滑的权重变化。
            uniform:均匀权重函数。为所有点提供相同的权重。
            inverse_distance:距离反比权重函数。根据距离的反比例来计算权重。
            wendland:Wendland权重函数。使用Wendland函数计算局部光滑的权重。
            shepard_weight:Shepard权重函数。使用距离的负幂计算权重，权重随距离增大而减小。
        """
        x = points[:, 0]
        y = points[:, 1]
        z = points[:, 2]
        # 构建KD树以快速找到邻居
        tree = KDTree(np.vstack((x, y)).T)
        smoothed_points = np.zeros((len(x), 3))
        for i in range(len(x)):
            # 使用KD树找到指定半径内的所有邻居
            idx = tree.query_ball_point([x[i], y[i]], r=radius)
            # 获取邻居点
            x_neigh = x[idx]
            y_neigh = y[idx]
            z_neigh = z[idx]

            # 如果邻域内没有足够的点，则跳过
            if len(x_neigh) < 3:
                continue

            # 计算邻居点到当前点的距离
            distances = np.sqrt((x_neigh - x[i]) ** 2 + (y_neigh - y[i]) ** 2)

            # 计算权重
            weights = utils.choose_weight(weights_name, distances, tau)

            # 二次曲面拟合: z = ax^2 + by^2 + cxy + dx + ey + f
            # 构建加权最小二乘问题
            A = np.vstack(
                [x_neigh ** 2 * weights, y_neigh ** 2 * weights, x_neigh * y_neigh * weights, x_neigh * weights,
                 y_neigh * weights, weights]).T
            b = z_neigh * weights

            # 解线性方程组得到拟合参数
            fit_params = np.linalg.lstsq(A, b, rcond=None)[0]

            # 计算当前点的平滑值
            smoothed_z = fit_params[0] * x[i] ** 2 + fit_params[1] * y[i] ** 2 + fit_params[2] * x[i] * y[i] + \
                         fit_params[
                             3] * x[i] + fit_params[4] * y[i] + fit_params[5]
            smoothed_points[i] = [x[i], y[i], smoothed_z]
        result = self.contract_point_list([points, smoothed_points])
        return np.array(result)