# SkeletalData_3600
3600 frames of point cloud skeleton data

###   Website：

The first two dimensions of each data point represent the frame count and camera ID.

The camera extrinsic parameters are represented by a 4x4 matrix. Camera 0 uses an identity matrix, while other cameras are aligned to Camera 0 through their respective extrinsic parameters.

The 2D skeleton points are represented by a 32x3 matrix, where only 20 of the 32 skeleton points are actually used. The indices of these used points are: [0, 1, 2, 3, 5, 6, 7, 12, 13, 14, 18, 19, 20, 21, 22, 23, 24, 25, 28, 30]. The 3 represents the x and y coordinates along with a validity value. The validity value differentiates between occluded and unoccluded points, where 1 indicates occlusion and 2 indicates no occlusion. The 3D skeleton points are represented by a 32x4 matrix, with 4 representing the x, y, z coordinates and the validity value similarly.

