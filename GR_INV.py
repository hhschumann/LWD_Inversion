# Created by Harrison Schumann
# Regularized inversion for borehole positioning of a horizontal well within a reservoir
# Inputs:
# Pilot well - gamma ray log, vertical depths, reservoir top/bottom
# Horizontal well - gamm ray log, approximated 2-D vertical/horizontal coordinates, initial reservoir depth model 

import numpy as np

class GR_Inversion():
    
    def set_pilot_log_vals(self,pilot_gr,pilot_tvd,res_top):
        self.pilot_gr = pilot_gr
        self.pilot_tvd = pilot_tvd - res_top
        
    def find_nearest_val(self,value):
        idx = (np.abs(self.pilot_tvd - value)).argmin()
        return self.pilot_gr[idx]
    
    # gets response from pilot well gamma log for given depth vector
    def get_GR_response(self,zs):
        self.response = np.zeros(len(zs))
        for i in range(len(zs)):
            self.response[i] = self.find_nearest_val(zs[i])
        return self.response

    # returns the jacobian matrix 
    def get_jacobian(self,init_mod_tvd,hwell_tvd,dz):
        self.z = hwell_tvd - init_mod_tvd
        self.N = self.M = len(hwell_tvd)
        self.gzsum = self.get_GR_response(self.z)
        self.J=np.zeros((self.N,self.M))
        for hh in range(self.M):
            h=self.z.copy()
            h[hh]=self.z[hh]+dz
            gzsum_h=self.get_GR_response(h)
            self.J[:,hh]=(gzsum_h-self.gzsum)/dz
        self.J
        
    def tikhonov(self,gr_obs,hwell_x,beta):
        dx = hwell_x[1]-hwell_x[0]
        std=np.std(gr_obs)
        
        # create weighted matrices
        Wd=np.eye(self.N)*(1/std)
        WsTWs = np.eye(self.M)*dx
        Wx = np.diag(-1/(std**.5)*np.ones(self.M),0)+np.diag(1/(std**0.5)*np.ones(self.M-1),1)
        WmTWm = np.add(WsTWs,np.dot(Wx.T,Wx)*10**8) 
    
        # calculate gradients of data misfit, objective function,
        phi_d_grad = self.J.T@Wd.T@Wd@(self.gzsum-gr_obs)
        phi_m_grad = self.z.dot(WmTWm)
        phi_grad = phi_d_grad + beta * phi_m_grad
    
        # calculate the predicted z changes and the predicted data
        dh_pred = np.linalg.solve((self.J.T@Wd.T@Wd@self.J+beta*WmTWm),-phi_grad)
        gr_pred = self.get_GR_response(dh_pred+self.z)
        return dh_pred, gr_pred



