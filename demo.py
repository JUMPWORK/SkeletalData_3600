import h5py
#读取h5数据
external_param = h5py.File("path/to/external_param.h5","r")["data"]
#从depth和内参获取点云数据
