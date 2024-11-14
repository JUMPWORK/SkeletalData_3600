# JUMPWORK Multi-Camera 4D Human Poindcloud Estimation Dataset.

[DataLink](https://drive.google.com/drive/folders/1YxQroqR_O4J7gCLLJuETdVxpurHJUgd2?usp=drive_link)

![项目截图](https://github.githubassets.com/images/modules/logos_page/Octocat.png)

[![GitHub Guide Video](https://img.youtube.com/vi/dQw4w9WgXcQ/0.jpg)][SkeletalData_3600/demo_video.mp4 at main · JUMPWORK/SkeletalData_3600](https://github.com/JUMPWORK/SkeletalData_3600/blob/main/demo_video.mp4)

- `JUMPWORK_Human4D_depth.h5`(3600,5,512*512):Depth Data.Represents 3600 frames, five cameras, and depth information.

- `JUMPWORK_Human4D_external_param.h5`(3600,5,4,4):Extrinsic Data.Represents 3600 frames, five cameras, and extrinsic information.

- `JUMPWORK_Human4D_intrinsic_param.h5`(3600,5,15):Intrinsic Data.Represents 3600 frames, five cameras, and intrinsic information.

- `JUMPWORK_Human4D_ske2d.h5`(3600,5,32,3):2D Skeleton Data.Represents 3600 frames, five cameras, and 32 skeleton points with corresponding xy coordinates and validity values.Only 20 out of the 32 skeleton points are actually used, with indices as follows:```SKE_INDEX_20_TO_32 = np.asarray([0, 1, 2, 3, 5, 6, 7, 12, 13, 14, 18, 19, 20, 21, 22, 23, 24, 25, 28, 30])```The validity value indicates whether a point is occluded(int 1) or unoccluded(int 2).

- `JUMPWORK_Human4D_ske3d.h5`(3600,5,32,4):3D Skeleton Data.Similar to the 2D skeleton points, only the last dimension differs, representing xyz coordinates and a validity value.

### Point clouds can be obtained through `JUMPWORK_Human4D_depth.h5` and `JUMPWORK_Human4D_external_param.h5`. Please refer to the content in `demo.py`.

##### Reading data from an h5 file:

```
import h5py
data = h5py.File("path/to/ske3d.h5","r")["data"]
```







