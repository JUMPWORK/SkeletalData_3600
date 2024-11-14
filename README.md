# SkeletalData_3600
3600 frames of point cloud skeleton data

[DataLink](https://drive.google.com/drive/folders/1YxQroqR_O4J7gCLLJuETdVxpurHJUgd2?usp=drive_link)

- `depth.h5`(3600,5,512*512):Depth Data.Represents 3600 frames, five cameras, and depth information.

- `external_param.h5`(3600,5,4,4):Extrinsic Data.Represents 3600 frames, five cameras, and extrinsic information.

- `intrinsic_param.h5`(3600,5,15):Intrinsic Data.Represents 3600 frames, five cameras, and intrinsic information.

- `ske2d.h5`(3600,5,32,3):2D Skeleton Data.Represents 3600 frames, five cameras, and 32 skeleton points with corresponding xy coordinates and validity values.Only 20 out of the 32 skeleton points are actually used, with indices as follows:```SKE_INDEX_20_TO_32 = np.asarray([0, 1, 2, 3, 5, 6, 7, 12, 13, 14, 18, 19, 20, 21, 22, 23, 24, 25, 28, 30])```The validity value indicates whether a point is occluded(int 1) or unoccluded(int 2).

- `ske3d.h5`(3600,5,32,4):3D Skeleton Data.Similar to the 2D skeleton points, only the last dimension differs, representing xyz coordinates and a validity value.

### Point clouds can be obtained through `depth.h5` and `external_param.h5`. Please refer to the content in `demo.py`.

##### Reading data from an h5 file:

```
import h5py
data = h5py.File("path/to/ske3d.h5","r")["data"]
```



