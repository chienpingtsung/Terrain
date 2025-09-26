import numpy as np
import open3d as o3d
from einops import rearrange


if __name__ == '__main__':
    terrain = np.load('terrain.npy')
    terrain = rearrange(terrain, 'xyz h w -> (h w) xyz')
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(terrain)
    o3d.io.write_point_cloud('terrain.pcd', pcd)
