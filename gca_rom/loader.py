import sys
from torch_geometric.data import Dataset
import torch
import scipy


class LoadDataset(Dataset):
    """
    A custom dataset class which loads data from a .mat file using scipy.io.loadmat.

    data_mat : scipy.io.loadmat
        The loaded data in a scipy.io.loadmat object.
    U : torch.Tensor
        The tensor representation of the specified variable from the data_mat.
    xx : torch.Tensor
        The tensor representation of the 'xx' key from the data_mat.
    yy : torch.Tensor
        The tensor representation of the 'yy' key from the data_mat.
    T : torch.Tensor
        The tensor representation of the 'T' key from the data_mat, casted to int.
    E : torch.Tensor
        The tensor representation of the 'E' key from the data_mat, casted to int.

    __init__(self, root_dir, variable)
        Initializes the LoadDataset object by loading the data from the .mat file at the root_dir location and converting the specified variable to a tensor representation.
    """

    def __init__(self, root_dir, variable):
        self.data_mat = scipy.io.loadmat(root_dir)
        self.U = torch.tensor(self.data_mat[variable])
        self.xx = torch.tensor(self.data_mat['xx'])
        self.yy = torch.tensor(self.data_mat['yy'])
        self.T = torch.tensor(self.data_mat['T'].astype(int))
        self.E = torch.tensor(self.data_mat['E'].astype(int))