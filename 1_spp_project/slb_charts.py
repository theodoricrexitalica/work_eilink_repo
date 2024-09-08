import pandas as pd

def slb_cp1cd_nphi_rhob():
# Schlumberger, CP-1c & CP-1d, Neutron Porosity vs Bulk Density, NPHI
    def rhob_nphi_cp1cd_ss():
        y_lst_ss = []
        x_lst_ss = []
        rhoma = 2.65
        rhof = 1
        A = -0.0210322
        B = 1.03699
        C = 1.10667
        for t in range(0,50,1):
            y = (t*0.01) * rhof + (1 - (t*0.01)) * rhoma
            if (t*0.01) < 0:
                x = -0.02 
            else:
                if (t*0.01) <= 0.45:
                    x = A + B * pow((t*0.01), C)  
                else:
                    x = 1.07724833 * (t*0.01) - 0.07724833
            x_lst_ss.append(x) 
            y_lst_ss.append(y)
            snd = zip(x_lst_ss, y_lst_ss)
            snd = pd.DataFrame(snd, columns=['x','y'])
        return snd
    snd = rhob_nphi_cp1cd_ss()

    def rhob_nphi_cp1cd_dol():
        y_lst_dol = []
        x_lst_dol = []
        rhoma = 2.87
        rhof = 1
        A = 0.0230147
        B = 0.764867
        C = 0.692188
        for t in range(0,50,1):
            y = (t*0.01) * rhof + (1 - (t*0.01)) * rhoma
            if (t*0.01) < 0:
                x = 0.025 
            else:
                if (t*0.01) <= 0.45:
                    x = A + B * pow((t*0.01), C)  
                else:
                    x = 0.97616953 * (t*0.01) + 0.02383050
            y_lst_dol.append(y) 
            x_lst_dol.append(x)
        dol = zip(x_lst_dol, y_lst_dol)
        dol = pd.DataFrame(dol, columns=['x','y'])
        return dol
    dol = rhob_nphi_cp1cd_dol()

    def rhob_nphi_cp1cd_lms():
        y_lst_lms = []
        x_lst_lms = []
        rhoma = 2.71
        rhof = 1
        for t in range(0,50,1):
            y = (t*0.01) * rhof + (1 - (t*0.01)) * rhoma 
            x = (t*0.01) 
            y_lst_lms.append(y) 
            x_lst_lms.append(x)
        lms = zip(x_lst_lms, y_lst_lms)
        lms = pd.DataFrame(lms, columns=['x','y'])
        return lms
    lms = rhob_nphi_cp1cd_lms()

    result = {'snd':snd, 'dol':dol, 'lms':lms}
    return result