import argparse
import os
import torch
import matplotlib.pyplot as plt
from attrdict import AttrDict

from sgan.data.loader import data_loader
from sgan.models import TrajectoryGenerator
from sgan.losses import displacement_error, final_displacement_error
from sgan.utils import relative_to_abs, get_dset_path

parser = argparse.ArgumentParser()
parser.add_argument('--model_path', type=str, default='models/sgan-models')
parser.add_argument('--num_samples', default=20, type=int)
parser.add_argument('--dset_type', default='test', type=str)


def get_generator(checkpoint):
    args = AttrDict(checkpoint['args'])
    generator = TrajectoryGenerator(
        obs_len=args.obs_len,
        pred_len=args.pred_len,
        embedding_dim=args.embedding_dim,
        encoder_h_dim=args.encoder_h_dim_g,
        decoder_h_dim=args.decoder_h_dim_g,
        mlp_dim=args.mlp_dim,
        num_layers=args.num_layers,
        noise_dim=args.noise_dim,
        noise_type=args.noise_type,
        noise_mix_type=args.noise_mix_type,
        pooling_type=args.pooling_type,
        pool_every_timestep=args.pool_every_timestep,
        dropout=args.dropout,
        bottleneck_dim=args.bottleneck_dim,
        neighborhood_size=args.neighborhood_size,
        grid_size=args.grid_size,
        batch_norm=args.batch_norm)
    
    generator.load_state_dict(checkpoint['g_state'])
    # generator.cuda()
    generator.train()
    return generator


def evaluate_helper(error, seq_start_end):
    sum_ = 0
    error = torch.stack(error, dim=1)

    for (start, end) in seq_start_end:
        start = start.item()
        end = end.item()
        _error = error[start:end]
        _error = torch.sum(_error, dim=0)
        _error = torch.min(_error)
        sum_ += _error
    return sum_


def evaluate(args, loader, generator, num_samples):
    ade_outer, fde_outer = [], []
    total_traj = 0
    
    # plt 2021-02
    plt.figure(num='global map', figsize=(8,10)) 
    plt.axis('equal')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title('Global')
    plt.pause(1)
    
    with torch.no_grad():   # dont calculate grad
        for batch in loader:
            # batch = [tensor.cuda() for tensor in batch]
            # obs_traj[num, x_size, y_size]-[:,0,0],[:,0,1]为一条轨迹坐标
            batch = [tensor for tensor in batch]
            (obs_traj, pred_traj_gt, obs_traj_rel, pred_traj_gt_rel,
             non_linear_ped, loss_mask, seq_start_end) = batch

            ade, fde = [], []
            total_traj += pred_traj_gt.size(1)

            for _ in range(num_samples):
                pred_traj_fake_rel = generator(
                    obs_traj, obs_traj_rel, seq_start_end   # run TrajectoryGenerator
                )                                           # 预测-未来轨迹-相对坐标
                pred_traj_fake = relative_to_abs(
                    pred_traj_fake_rel, obs_traj[-1]
                )
                ade.append(displacement_error(
                    pred_traj_fake, pred_traj_gt, mode='raw'
                ))
                fde.append(final_displacement_error(
                    pred_traj_fake[-1], pred_traj_gt[-1], mode='raw'
                ))
                
                
                # plt 2021-02
                plt.pause(1)
                plt.cla()
                
                center_point = obs_traj[-1,0:2,0]
                plt_axis = [center_point[0]-15,center_point[0]+15,
                            center_point[1]-15,center_point[1]+15]
                for index in range(seq_start_end[0,0],seq_start_end[0,1]):
                    # obs_traj
                    plt.plot(obs_traj[:,index,0],obs_traj[:,index,1],c='gray',linestyle='--')
                    
                    # pred_traj_fake
                    plt.plot(pred_traj_fake[:,index,0],pred_traj_fake[:,index,1],c='blue',linestyle='-.')
                    
                    # pred_traj_gt
                    plt.plot(pred_traj_gt[:,index,0],pred_traj_gt[:,index,1],c='black',linestyle='--')
                    
                plt.legend( ['trajcetory', 'prediction', 'real'], loc='upper right', scatterpoints=1)
                plt.axis('equal')
                plt.axis(plt_axis)
                
                
            ade_sum = evaluate_helper(ade, seq_start_end)
            fde_sum = evaluate_helper(fde, seq_start_end)

            ade_outer.append(ade_sum)
            fde_outer.append(fde_sum)
        ade = sum(ade_outer) / (total_traj * args.pred_len)
        fde = sum(fde_outer) / (total_traj)
        return ade, fde


def main(args):
    if os.path.isdir(args.model_path):
        filenames = os.listdir(args.model_path)
        filenames.sort()
        paths = [
            os.path.join(args.model_path, file_) for file_ in filenames
        ]
    else:
        paths = [args.model_path]

    for path in paths:
        # set model file
        path = '/home/yuanwang/Data/Pyhton/sgan-master/models/sgan-models/eth_12_model.pt'
        print(path)
        
        # load model
        # checkpoint = torch.load(path)
        checkpoint = torch.load(path, map_location=lambda storage, loc: storage)
        generator = get_generator(checkpoint)                               # generator
        
        
        # get data set
        _args = AttrDict(checkpoint['args'])
        path = get_dset_path(_args.dataset_name, args.dset_type)
        path = '/home/yuanwang/Data/Pyhton/sgan-master/datasets/hotel/test'
        print(path)
        dset, loader = data_loader(_args, path)
        
        # evaluate
        _args.batch_size = 1
        num_samples = 1
        print(_args.batch_size)
        ade, fde = evaluate(_args, loader, generator, num_samples)
        print('Dataset: {}, Pred Len: {}, ADE: {:.2f}, FDE: {:.2f}'.format(
            _args.dataset_name, _args.pred_len, ade, fde))
        
        '''
        | Model  | ADE-8 | ADE-12| FDE-8 | FDE-12|
        | `eth`  | 0.58  | 0.71  | 1.13  | 1.29  |
        | `hotel`| 0.36  | 0.48  | 0.71  | 1.02  |
        | `univ` | 0.33  | 0.56  | 0.70  | 1.18  |
        | `zara1`| 0.21  | 0.34  | 0.42  | 0.69  |
        | `zata2`| 0.21  | 0.31  | 0.42  | 0.64  |
        '''

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
