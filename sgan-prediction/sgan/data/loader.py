from torch.utils.data import DataLoader

from sgan.data.trajectories import TrajectoryDataset, seq_collate


def data_loader(args, path):
    dset = TrajectoryDataset(
        path,
        obs_len=args.obs_len,
        pred_len=args.pred_len,
        skip=args.skip,
        delim=args.delim)

    loader = DataLoader(
        dset,                                   # data set
        batch_size = 1,
        # batch_size=args.batch_size,             # batch_size 64
        shuffle=False,                          # 要不要打乱数据
        num_workers=args.loader_num_workers,    # 多线程来读数据
        collate_fn=seq_collate)
    return dset, loader
