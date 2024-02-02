import torch
from torch import nn

class EncoderCell(nn.Module):
    def __init__(self, grid_dim, param_dim, hidden_dim, kernels):
        super(EncoderCell,self).__init__()
        self.hidden_dim = hidden_dim
        self.Parameterslstm = nn.LSTM(param_dim, hidden_dim)
        self.Gridscnn = nn.Conv2d(grid_dim + hidden_dim, hidden_dim*4, kernel_size=kernels)
        self.LinearHiddenState = nn.Linear(2*hidden_dim, hidden_dim)
        self.LinearCurrentState = nn.Linear(2*hidden_dim, hidden_dim)
        self.LinearOutput = nn.Linear(hidden_dim*2, hidden_dim)
    
    def empty_state(self):
        return (torch.zeros(1,7,self.hidden_dim),torch.zeros(1,7,self.hidden_dim))
        
    def forward(self, Grids, Parameters, hiddenstate):
        output, (h_n, c_n) = self.Parameterslstm(Parameters, hiddenstate)
        
        all_t = self.Gridscnn(torch.cat([Grids, hiddenstate[0]]))
        f_t, i_t, o_t, c_t_tilde = torch.split(all_t)
        f_t = torch.sigmoid(f_t)
        i_t = torch.sigmoid(i_t)
        o_t = torch.sigmoid(o_t)
        c_t_tilde = torch.tanh(c_t_tilde)
        c_t = f_t*hiddenstate[1] + i_t*c_t_tilde
        h_t = o_t*torch.tanh(c_t)
        
        combine_output = self.LinearOutput([output,o_t])
        combine_h_t = self.LinearHiddenState([h_n, h_t])
        combine_c_t = self.LinearCurrentState([c_n, c_t])
        return combine_output, (combine_h_t, combine_c_t)

class Encoder(nn.Module):
    pass

class DecoderCell(nn.Module):
    pass

class Decoder(nn.Module):
    pass



