#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Packages needed
import pybinding as pb
import numpy as np
import cupy as cp
import os
import argparse
import time
import scipy
import sys
from tqdm import tqdm




# In[3]:


#Wilson Loop Calculation
def HamBlk(kx,ky,kz,syst,kwant=False):
    if kwant==True:
        syst = syst(kx,ky,kz)
        syst = syst.finalized()
        ham_mat = syst.hamiltonian_submatrix(sparse=True)
        EV,EVec=cp.linalg.eigh(cp.array(ham_mat.toarray()))
    else:
        solver= pb.solver.lapack(syst)
        solver.set_wave_vector([kx,ky,kz])
        H=cp.array(getattr((getattr(solver,'model')),'hamiltonian').todense())
        EV, EVec=cp.linalg.eigh(H)
        #=solver.eigenvalues
        #EVec=solver.eigenvectors
    return EV, EVec
def proj(kx,ky,kz,syst,bnds,kwant=False):
    w,v=HamBlk(kx,ky,kz,syst,kwant)
    #w,v=np.linalg.eigh(H)
    ft=cp.zeros(cp.shape(cp.outer(cp.transpose(cp.conjugate(v[:,[0]])),v[:,[0]])))
    for i in bnds:
        ft=ft+cp.outer(v[:,[i]],cp.transpose(cp.conjugate(v[:,[i]])))
    return ft
def eig(kx,ky,kz,syst,bnds,kwant=False):
    w,v=HamBlk(kx,ky,kz,syst,kwant)
    #w,v=np.linalg.eigh(H)
    return v[:,bnds]

def WSurf(vec,syst,bnds,ds,ds2,rvec0,kwant=False):
    #rvec0 = np.array(lat.reciprocal_vectors())
    rvec=np.zeros((3,3))
    for j in range(np.shape(rvec0)[0]):
        rvec[j]=rvec0[j]
    #rvec=cp.asnumpy(rvec)
    WCC=[]
    #rf3=np.dot(rvec,vec(0,1))
    #kp = np.linspace(0,rf3,ds2)
    for kk1 in range(int(ds2+1)):
        kk=np.dot(vec(0,kk1/ds2),rvec)
        #rf=np.dot(vec(1,0),rvec)
        #rf2=np.dot(vec(1,0),rvec)+kk
        rf=np.dot(np.array(vec(1,0))-np.array(vec(0,0)),rvec)
        rf2=rf+kk
        kpts=np.linspace(rf/ds+kk,rf-rf/ds+kk,ds)
        w,v=HamBlk(rf2[0],rf2[1],rf2[2],syst,kwant)
        #w,v=np.linalg.eigh(H)
        sp=v[:,bnds]
        ft=proj(rf2[0],rf2[1],rf2[2],syst,bnds,kwant)
        ff=ft
        for i in kpts:
            ft=cp.dot(ft,proj(i[0],i[1],i[2],syst,bnds,kwant))
        ft=cp.dot(ft,ff)
        WCC.append(np.imag(np.log(np.linalg.eigvals(cp.asnumpy(cp.dot(cp.dot(cp.transpose(cp.conjugate(sp)),ft),sp))))))
    return cp.asnumpy(cp.array(WCC))

import scipy
def projnwl(WCC, bnds2):
    v=cp.array(WCC)
    ft=cp.zeros(cp.shape(cp.outer(cp.transpose(cp.conjugate(v[:,[0]])),v[:,[0]])))
    #ft=np.outer(np.transpose(np.conjugate(v)),v)
    for i in bnds2:
        ft=ft+cp.outer(v[:,[i]],cp.transpose(cp.conjugate(v[:,[i]])))
    return ft
def Hermitize(X):
    return 0.5*(X+cp.conjugate(cp.transpose(X)))
def WNWL(vec,syst,bnds,bnds2,ds,ds2,rvec0,kwant=False):
    #rvec0 = np.array(lat.reciprocal_vectors())
    rvec=np.zeros((3,3))
    for j in range(np.shape(rvec0)[0]):
        rvec[j]=rvec0[j]
    WCC=[]
    #rf3=np.dot(vec(0,1),rvec)
    #kp = np.linspace(0,rf3,ds2)
    for kk1 in range(int(ds2+1)):
        kk=np.dot(vec(0,kk1/ds2),rvec)
        #rf=np.dot(vec(1,0),rvec)
        #rf2=np.dot(vec(1,0),rvec)+kk
        rf=np.dot(np.array(vec(1,0))-np.array(vec(0,0)),rvec)
        rf2=rf+kk
        kpts=np.linspace(rf/ds+kk,rf-rf/ds+kk,ds)
        w,v=HamBlk(rf2[0],rf2[1],rf2[2],syst,kwant)
        #w,v=np.linalg.eigh(H)
        sp=v[:,bnds]
        ft=proj(rf2[0],rf2[1],rf2[2],syst,bnds,kwant)
        ff=ft
        for i in kpts:
            ft=cp.dot(ft,proj(i[0],i[1],i[2],syst,bnds,kwant))
        ft=cp.dot(ft,ff)
        WH=Hermitize(-1j*cp.array(scipy.linalg.logm(cp.asnumpy(cp.dot(cp.dot(cp.transpose(cp.conjugate(sp)),ft),sp)))))
        w, v= cp.linalg.eigh(WH)
        WCC.append(cp.dot(eig(rf2[0],rf2[1],rf2[2],syst,bnds,kwant),v))
    sp=WCC[0][:,bnds2]
    ft=projnwl(WCC[0],bnds2)
    ff=ft
    for i in range(int(ds2+1)):
        ft=cp.dot(ft,projnwl(WCC[i],bnds2))
    ft=cp.dot(ft,ff)
    return np.imag(np.log(np.linalg.eigvals(cp.asnumpy(cp.dot(cp.dot(cp.transpose(cp.conjugate(sp)),ft),sp)))))

#Spin resolved Wilson loop:
def proj2(kx,ky,kz,syst,bnds,op,kwant=False):
    H=cp.dot(cp.dot(proj(kx,ky,kz,syst,bnds,kwant),op),proj(kx,ky,kz,syst,bnds,kwant))
    w,v=cp.linalg.eigh(H)
    ft=cp.zeros(cp.shape(cp.outer(cp.transpose(cp.conjugate(v[:,[0]])),v[:,[0]])))
    for i in bnds[:int(cp.shape(bnds)[0]/2)]:
        ft=ft+cp.outer(v[:,[i]],cp.transpose(cp.conjugate(v[:,[i]])))
    return ft
def WSpinSurf(vec,syst,bnds,ds,ds2,op,rvec0,kwant=False):
    #rvec0 = np.array(lat.reciprocal_vectors())
    rvec=np.zeros((3,3))
    for j in range(np.shape(rvec0)[0]):
        rvec[j]=rvec0[j]
    WCC=[]
    #rf3=np.dot(rvec,vec(0,1))
    #kp = np.linspace(0,rf3,ds2)
    for kk1 in range(int(ds2+1)):
        kk=np.dot(vec(0,kk1/ds2),rvec)
        #rf=np.dot(vec(1,0),rvec)
        #rf2=np.dot(vec(1,0),rvec)+kk
        rf=np.dot(np.array(vec(1,0))-np.array(vec(0,0)),rvec)
        rf2=rf+kk
        kpts=np.linspace(rf/ds+kk,rf-rf/ds+kk,ds)
        H=cp.dot(cp.dot(proj(rf2[0],rf2[1],rf2[2],syst,bnds[:int(cp.shape(bnds)[0]/2)],kwant),op),proj(rf2[0],rf2[1],rf2[2],syst,bnds[:int(cp.shape(bnds)[0]/2)],kwant))
        w,v=cp.linalg.eigh(H)
        sp=v[:,bnds[:int(cp.shape(bnds)[0]/2)]]
        ft=proj2(rf2[0],rf2[1],rf2[2],syst,bnds,op,kwant)
        ff=ft
        for i in kpts:
            ft=cp.dot(ft,proj2(i[0],i[1],i[2],syst,bnds,op,kwant))
        ft=cp.dot(ft,ff)
        WCC.append(np.imag(np.log(np.linalg.eigvals(cp.asnumpy(cp.dot(cp.dot(cp.transpose(cp.conjugate(sp)),ft),sp))))))
    return cp.asnumpy(cp.array(WCC))

def WSpinLine(kpts,syst,bnds,op,kwant=False):
    WCC=[]
    rf2=kpts[0]
    H=cp.dot(cp.dot(proj(rf2[0],rf2[1],rf2[2],syst,bnds[:int(cp.shape(bnds)[0]/2)],kwant),op),proj(rf2[0],rf2[1],rf2[2],syst,bnds[:int(cp.shape(bnds)[0]/2)],kwant))
    w,v=cp.linalg.eigh(H)
    sp=v[:,bnds[:int(cp.shape(bnds)[0]/2)]]
    ft=proj2(rf2[0],rf2[1],rf2[2],syst,bnds,op,kwant)
    ff=ft
    for i in kpts[1:]:
        ft=cp.dot(ft,proj2(i[0],i[1],i[2],syst,bnds,op,kwant))
    ft=cp.dot(ft,ff)
    WCC.append(np.imag(np.log(np.linalg.eigvals(cp.asnumpy(cp.dot(cp.dot(cp.transpose(cp.conjugate(sp)),ft),sp))))))
    return cp.asnumpy(cp.array(WCC))

def WLine(kpts,syst,bnds,kwant=False):
    WCC=[]
    #rvec0 = np.array(lat.reciprocal_vectors())
    rf2=kpts[0]
    w,v=HamBlk(rf2[0],rf2[1],rf2[2],syst,kwant)
    #w,v=np.linalg.eigh(H)
    sp=v[:,bnds]
    ft=proj(rf2[0],rf2[1],rf2[2],syst,bnds,kwant)
    ff=ft
    for i in kpts[1:]:
        ft=cp.dot(ft,proj(i[0],i[1],i[2],syst,bnds,kwant))
    ft=cp.dot(ft,ff)
    WCC.append(np.imag(np.log(np.linalg.eigvals(cp.asnumpy(cp.dot(cp.dot(cp.transpose(cp.conjugate(sp)),ft),sp))))))
    return cp.asnumpy(cp.array(WCC))

def spin_spectrum(kx,ky,kz,syst,bnds,op,kwant=False):
    H=cp.dot(cp.dot(proj(kx,ky,kz,syst,bnds,kwant),op),proj(kx,ky,kz,syst,bnds,kwant))
    w =cp.linalg.eigvalsh(H)
    
    w= cp.asnumpy(w)
    #v= cp.asnumpy(v)
    idx = np.argsort(np.abs(w))
    ev = w[idx[int(np.shape(w)[0]-np.shape(bnds)[0]):]]
    return np.sort(ev)


# In[4]:


def read_tb(Filename):
    Filename=Filename+'_tb.dat'
    '''
    Parser for Seedname_tb.dat file.
    '''
    if os.path.exists(Filename) == False:
        print(f"ERROR: {Filename} not found." )
        exit()

    print(f"Reading: {Filename}... \t\t", end='', flush=True)
    # read in all data
    with open(Filename, 'r') as f:
        data = f.readlines()

    # lattice vectors
    lat_vec = np.array([data[1].strip().split(),
                        data[2].strip().split(),
                        data[3].strip().split()], dtype=float)

    # basic data
    num_wann = int(data[4])
    num_kpts = int(data[5])

    # get degeneracy data
    nrpt_lines = int(np.ceil(num_kpts / 15.0))
    istart = 6 + nrpt_lines
    deg=[]
    for i in range(6,istart):
        deg.append(np.array([int(j) for j in data[i].split()]))
    deg=np.concatenate(deg,0)

    # get hoppings
    # some initialization
    icount=0
    Rlatt = []
    hopps = []
    r_hop= np.zeros([num_wann,num_wann], dtype=complex)

    for i in range(istart,istart+(num_wann**2+2)*num_kpts):
        line=data[i].split()
        if len(line) > 3:
            # Let's use 0 based index
            m = int(line[0]) - 1
            n = int(line[1]) - 1
            r_hop[m,n] = complex(round(float(line[2]),6),round(float(line[3]),6))
        else:
            R = np.array([float(x) for x in line[0:3]])
        icount+=1
        if(icount % (num_wann**2 + 2) == 0):
            Rlatt.append(R)
            hopps.append(r_hop)
            # reinitialize r_hop
            r_hop= np.zeros([num_wann,num_wann], dtype=complex)

    Rlatt=np.asarray(Rlatt, dtype=int)
    hopps=np.asarray(hopps)
    deg = np.reshape(deg,[num_kpts,1,1])
    hopps=hopps/deg

    print("done.",flush=True)

    return lat_vec, Rlatt, hopps, deg, num_wann, num_kpts

# lat_vec, Rlatt, hopps, deg, num_wann, num_kpts = read_tb(Filename='wannier90_tb.dat')

def read_center(Filename):
    Filename=Filename+'_centres.xyz'
    '''
    Parser for seedname_centers.xyz
    '''
    if os.path.exists(Filename) == False:
        print(f"ERROR: {Filename} not found." )
        exit()

    print(f"Reading: {Filename}... \t", end='', flush=True)

    with open(Filename, 'r') as f:
        data = f.readlines()

    wan_centers = []
    for i in range(2,len(data)):
        if data[i].split()[0] == 'X':
            wan_centers.append(data[i].split()[1:])

    wan_centers = np.asarray(wan_centers,dtype=float)

    print("done.",flush=True)
    return wan_centers


# In[5]:




def progressbar(it, prefix="", size=60, file=sys.stdout):
    '''
    progress bar function from https://stackoverflow.com/a/34482761/12660859
    '''
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

def wan90_lat(E_cutoff, R_cutoff, seedname):
    '''
    main function to covert w90's hamiltonian to pybinding's format
    '''
    # read-in stuff
    lat_vec, Rlatt, hopps, deg, num_wann, num_kpts = read_tb(Filename=seedname)
    wan_centers = read_center(Filename=seedname)

    #print(f"Converting fromat: \t\t\t\t",flush=True)

    # generate lat object
    lat = pb.Lattice(a1 = lat_vec[0],
                     a2 = lat_vec[1],
                     a3 = lat_vec[2])

    # putting in all sites and their on-site energies.
    print("Converting on-site energyies: ")
    for i in tqdm(range(len(Rlatt))):
        if all(Rlatt[i]==[0, 0, 0]):
            for m in range(num_wann):
                # icount1+=1
                lat.add_one_sublattice(str(m), wan_centers[m], onsite_energy=np.real(hopps[i,m,m]))

    # putting in all hopping elements.
    # NOTE: pybinding reports error when adding hermitian conjugate of existing hoppings.
    # we just do brute force error handling on this since it's faster that using if
    # to determine which hoppings to add. (like in pythtb's interfce.)
    # note that this means we assume Wannier Hamiltonian is Hermitian.
    print("Converting hopping energyies: ")
    for i in tqdm(range(len(Rlatt))):
        for m in range(num_wann):
            for n in range(num_wann):
                try:
                    if np.abs(hopps[i,m,n])>E_cutoff and np.linalg.norm(Rlatt[i])<R_cutoff:
                        lat.add_one_hopping(Rlatt[i],
                                            str(m),
                                            str(n),
                                            hopps[i,m,n])
                except:
                    continue


    #print("done.",flush=True)

    return lat

