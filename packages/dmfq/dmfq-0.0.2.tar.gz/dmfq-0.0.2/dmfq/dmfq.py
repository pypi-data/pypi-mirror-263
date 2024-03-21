
import numpy as np
import torch


'''
https://www.barwe.cc/2022/06/24/dist-my-pkg-to-pypi

'''
def get_np_info(varNp):
   
    '''
    import sys 
    sys.path.append("/Users/hjy/workspace/00_utils_sync/utils_folder")
    from utils import get_numpy_info
    '''
    # print("-"*20)
    print("".center(50, "-"))
    print(f"nummpy's shape is :{varNp.shape}")
    print(f"nummpy's dtype is :{varNp.dtype}")
    print(f"nummpy's max  num is :{varNp.max()}")
    print(f"nummpy's mean num is :{varNp.mean()}")
    print(f"nummpy's min  num is :{varNp.min()}")

    print(f"==>> varNp: {varNp}")
    # plt.hist(arrayNp.ravel(), bins='auto')
    # plt.ylim(10000)
    # plt.hist(arrayNp.ravel(), bins=255)
    # plt.show()
    # plt.close()

def get_tc_info(varTorch):
    '''
    import sys 
    sys.path.append("/Users/hjy/workspace/00_utils_sync/utils_folder")
    from utils import get_numpy_info
    '''
    # print("-"*20)
    print("".center(50, "-"))
    print(f"tensor's shape is :{varTorch.shape}")
    print(f"tensor's dtype is :{varTorch.dtype}")
    print(f"tensor's device is :{varTorch.device}")
    print(f"tensor's max  num is :{varTorch.max()}")
    print(f"tensor's mean num is :{varTorch.mean()}")
    print(f"tensor's min  num is :{varTorch.min()}")
    # plt.hist(arrayNp.ravel(), bins='auto')
    # plt.ylim(10000)
    # plt.hist(arrayNp.ravel(), bins=255)
    # plt.show()
    # plt.close()






def get_dict_info(a_dict=None):
    a_dict = {'a':1,'b':np.array([1,2]),'c':[4,2]}
    count = 0
    for k, v in a_dict.items():
        count+=1
        print("".center(25, "="),f"keys num = {count}","".center(25, "="))
        print(f"key, type(value) is : {k}: {type(v)}")

        if type(v) in (int,float,complex):
           print("".center(50, "-"))
           print(f"{k}: {v}")

        if isinstance(v, list):
            print("".center(50, "-"))
            print(f"len of list is: {len(v)}")
            print(f"value is: {v}")

        if isinstance(v, tuple):
            print("".center(50, "-"))
            print(f"len of tuple is: {len(v)}")
            for i in range(len(v)):
                print(f"==>> type(v[i]): {type(v[i])}")


        if isinstance(v, dict):
            print(f"{k}:{v.keys()}")
        
        if isinstance(v, np.ndarray):
            get_numpy_info(v)
        
        if isinstance(v, torch.Tensor):
            get_tensor_info(v)

# get_dict_info(a_dict=None)



def get_list_info(a_list=None):
    print(f"==>> len(a_list): {len(a_list)}")
    if len(a_list)>0:
        print(f"==>> a_list[0]: {a_list[0]}")