"""Utility functions of niceplot package."""
import matplotlib
import matplotlib.pyplot as plt
import uproot as uproot
import pandas
import numpy as np
from pathlib import Path
from niceplot.reader import DotAccessibleDict

import warnings
warnings.simplefilter(action='ignore', category=pandas.errors.PerformanceWarning)
warnings.simplefilter(action='ignore', category=pandas.errors.SettingWithCopyWarning)

def printwelcome() -> None:
    from niceplot.__init__ import __version__,__author__,__credits__
    """Print Welcome message and package version number."""
    
    # Note: ASCII art generated with https://patorjk.com/software/taag/ (Small, Fitted)
    print("\n"+r"""  _  _  _                 _       _           __  
 | \| |(_) __  ___  _ __ | | ___ | |_  __ __ /  \ 
 | .` || |/ _|/ -_)| '_ \| |/ _ \|  _| \ V /| () |
 |_|\_||_|\__|\___|| .__/|_|\___/ \__|  \_/  \__/ 
                   |_|                            """+"\n")

    print(f"Welcome to Niceplot v{__version__}!")
    print(f"Author: {__author__} ({__credits__})\n")
    
    return None

def getaddinfo(conflist: list[dict], name: str) -> str:
    """Get and return addinfo entry from conflist for entry with name."""
    addinfo = None
    for conf in conflist:
        addinfo = conf.addinfo if conf.name == name else addinfo
    
    return addinfo

def softpad(value, default):
        """Replace value by default if None."""
        return default if value is None else value

def paddefaults(obj: DotAccessibleDict, mode: str) -> None:
    """Function for padding configuration dicts. Contains default plotting/config values!"""
        
    if mode == 'plot':
        obj.logy = softpad(obj.logy, default=False)
        obj.range = softpad(obj.range, default=None)
        obj.nbins = softpad(obj.nbins, default=None)
        obj.ylab = softpad(obj.ylab, default='events')
        obj.ratio = softpad(obj.ratio, default=True)
        obj.zopt = softpad(obj.zopt, default='counts')
        obj.addnumbers = softpad(obj.addnumbers, default=False)
        obj.subdir = softpad(obj.subdir, default='')
    elif mode == 'reader':
        obj.output_dir = softpad(obj.output_dir, default='plots')    
    else:
        raise ValueError(f"Padding mode {mode} not supported!")
    
    return

def getnicestr(string: str) -> str:
    """Function to get nice TeX version of string."""
    nicedict = {
        'GM2_gmuon': r"$\Delta a_{\mu}$",
        'GM2_Delta_gmuon': r"$\Delta(\Delta a_{\mu})$",
        'SPfh_m_h': r"$m(h)$",
        'SPfh_m_mu_L': r"$m(\tilde{\mu}_L)$",
        'SPfh_m_mu_R': r"$m(\tilde{\mu}_R)$",
        'SPfh_min_m_mu_LR': r"$\mathrm{min}(m(\tilde{\mu}_L), m(\tilde{\mu}_R))$",
        'SPfh_m_chi_10': r"$m(\tilde{\chi}_1^0)$",
        'SPfh_m_chi_20': r"$m(\tilde{\chi}_2^0)$",
        'SPfh_m_chi_30': r"$m(\tilde{\chi}_3^0)$",
        'SPfh_m_chi_40': r"$m(\tilde{\chi}_4^0)$",
        'SPfh_m_chi_1p': r"$m(\tilde{\chi}_1^\pm)$",
        'SPfh_m_chi_2p': r"$m(\tilde{\chi}_2^\pm)$",
        'SPfh_m_chi_3p': r"$m(\tilde{\chi}_3^\pm)$",
        'SPfh_BF_chi_10_to_gravitino_Z': r"$\mathrm{BF}(\tilde{\chi}_1^0\rightarrow \tilde{G}Z)$",
        'SPfh_BF_chi_10_to_gravitino_h': r"$\mathrm{BF}(\tilde{\chi}_1^0\rightarrow \tilde{G}h)$",
        'SPfh_BF_chi_10_to_gravitino_gam': r"$\mathrm{BF}(\tilde{\chi}_1^0\rightarrow \tilde{G}\gamma)$",
        'SPfh_BF_chi_1p_to_gravitino': r"$\mathrm{BF}(\tilde{\chi}_1^\pm\rightarrow \tilde{G}X)$",
        'SPfh_BF_chi_2p_to_gravitino': r"$\mathrm{BF}(\tilde{\chi}_2^\pm\rightarrow \tilde{G}X)$",
        'SPfh_BF_chi_20_to_gravitino': r"$\mathrm{BF}(\tilde{\chi}_2^0\rightarrow \tilde{G}X)$",
        'SPfh_BF_chi_30_to_gravitino': r"$\mathrm{BF}(\tilde{\chi}_3^0\rightarrow \tilde{G}X)$",
        'SPfh_BF_chi_40_to_gravitino': r"$\mathrm{BF}(\tilde{\chi}_4^0\rightarrow \tilde{G}X)$",
        'SPfh_BF_u_L_to_gravitino': r"$\mathrm{BF}(\tilde{u}_L\rightarrow \tilde{G}X)$",
        'SPfh_BF_u_R_to_gravitino': r"$\mathrm{BF}(\tilde{u}_R\rightarrow \tilde{G}X)$",
        'SPfh_BF_d_L_to_gravitino': r"$\mathrm{BF}(\tilde{d}_L\rightarrow \tilde{G}X)$",
        'SPfh_BF_d_R_to_gravitino': r"$\mathrm{BF}(\tilde{d}_R\rightarrow \tilde{G}X)$",
        'SPfh_BF_b_1_to_gravitino': r"$\mathrm{BF}(\tilde{b}_1\rightarrow \tilde{G}X)$",
        'SPfh_BF_b_2_to_gravitino': r"$\mathrm{BF}(\tilde{b}_2\rightarrow \tilde{G}X)$",
        'SPfh_BF_t_1_to_gravitino': r"$\mathrm{BF}(\tilde{t}_1\rightarrow \tilde{G}X)$",
        'SPfh_BF_t_2_to_gravitino': r"$\mathrm{BF}(\tilde{t}_2\rightarrow \tilde{G}X)$",
        'SPfh_BF_e_L_to_gravitino': r"$\mathrm{BF}(\tilde{e}_L\rightarrow \tilde{G}X)$",
        'SPfh_BF_e_R_to_gravitino': r"$\mathrm{BF}(\tilde{e}_R\rightarrow \tilde{G}X)$",
        'SPfh_BF_mu_L_to_gravitino': r"$\mathrm{BF}(\tilde{\mu}_L\rightarrow \tilde{G}X)$",
        'SPfh_BF_mu_R_to_gravitino': r"$\mathrm{BF}(\tilde{\mu}_R\rightarrow \tilde{G}X)$",
        'SPfh_BF_tau_1_to_gravitino': r"$\mathrm{BF}(\tilde{\tau}_1\rightarrow \tilde{G}X)$",
        'SPfh_BF_tau_2_to_gravitino': r"$\mathrm{BF}(\tilde{\tau}_2\rightarrow \tilde{G}X)$",
        'SPfh_BF_nu_e_L_to_gravitino': r"$\mathrm{BF}(\tilde{\nu}_{e L}\rightarrow \tilde{G}X)$",
        'SPfh_BF_nu_mu_L_to_gravitino': r"$\mathrm{BF}(\tilde{\nu}_{\mu L}\rightarrow \tilde{G}X)$",
        'SPfh_BF_nu_tau_L_to_gravitino': r"$\mathrm{BF}(\tilde{\nu}_{\tau L}\rightarrow \tilde{G}X)$",
        'SPfh_BF_gl_to_gravitino': r"$\mathrm{BF}(\tilde{g}\rightarrow \tilde{G}X)$",
        'SPfh_chi_10_Bino_frac': r"$\tilde{\chi}_1^0$ Bino fraction",
        'SPfh_chi_10_Wino_frac': r"$\tilde{\chi}_1^0$ Wino fraction",
        'SPfh_chi_10_Higgsino_frac': r"$\tilde{\chi}_1^0$ Higgsino fraction",
        'm_h': r"$m(h)$",
        'm_mu_L': r"$m(\tilde{\mu}_L)$",
        'm_mu_R': r"$m(\tilde{\mu}_R)$",
        'min_m_mu_LR': r"$\mathrm{min}(m(\tilde{\mu}_L), m(\tilde{\mu}_R))$",
        'm_chi_10': r"$m(\tilde{\chi}_1^0)$",
        'm_chi_20': r"$m(\tilde{\chi}_2^0)$",
        'm_chi_30': r"$m(\tilde{\chi}_3^0)$",
        'm_chi_40': r"$m(\tilde{\chi}_4^0)$",
        'm_chi_1p': r"$m(\tilde{\chi}_1^\pm)$",
        'm_chi_2p': r"$m(\tilde{\chi}_2^\pm)$",
        'm_chi_3p': r"$m(\tilde{\chi}_3^\pm)$",
        'BF_chi_10_to_gravitino_Z': r"$\mathrm{BF}(\tilde{\chi}_1^0\rightarrow \tilde{G}Z)$",
        'BF_chi_10_to_gravitino_h': r"$\mathrm{BF}(\tilde{\chi}_1^0\rightarrow \tilde{G}h)$",
        'BF_chi_10_to_gravitino_gam': r"$\mathrm{BF}(\tilde{\chi}_1^0\rightarrow \tilde{G}\gamma)$",
        'BF_chi_1p_to_gravitino': r"$\mathrm{BF}(\tilde{\chi}_1^\pm\rightarrow \tilde{G}X)$",
        'BF_chi_2p_to_gravitino': r"$\mathrm{BF}(\tilde{\chi}_2^\pm\rightarrow \tilde{G}X)$",
        'BF_chi_20_to_gravitino': r"$\mathrm{BF}(\tilde{\chi}_2^0\rightarrow \tilde{G}X)$",
        'BF_chi_30_to_gravitino': r"$\mathrm{BF}(\tilde{\chi}_3^0\rightarrow \tilde{G}X)$",
        'BF_chi_40_to_gravitino': r"$\mathrm{BF}(\tilde{\chi}_4^0\rightarrow \tilde{G}X)$",
        'BF_u_L_to_gravitino': r"$\mathrm{BF}(\tilde{u}_L\rightarrow \tilde{G}X)$",
        'BF_u_R_to_gravitino': r"$\mathrm{BF}(\tilde{u}_R\rightarrow \tilde{G}X)$",
        'BF_d_L_to_gravitino': r"$\mathrm{BF}(\tilde{d}_L\rightarrow \tilde{G}X)$",
        'BF_d_R_to_gravitino': r"$\mathrm{BF}(\tilde{d}_R\rightarrow \tilde{G}X)$",
        'BF_b_1_to_gravitino': r"$\mathrm{BF}(\tilde{b}_1\rightarrow \tilde{G}X)$",
        'BF_b_2_to_gravitino': r"$\mathrm{BF}(\tilde{b}_2\rightarrow \tilde{G}X)$",
        'BF_t_1_to_gravitino': r"$\mathrm{BF}(\tilde{t}_1\rightarrow \tilde{G}X)$",
        'BF_t_2_to_gravitino': r"$\mathrm{BF}(\tilde{t}_2\rightarrow \tilde{G}X)$",
        'BF_e_L_to_gravitino': r"$\mathrm{BF}(\tilde{e}_L\rightarrow \tilde{G}X)$",
        'BF_e_R_to_gravitino': r"$\mathrm{BF}(\tilde{e}_R\rightarrow \tilde{G}X)$",
        'BF_mu_L_to_gravitino': r"$\mathrm{BF}(\tilde{\mu}_L\rightarrow \tilde{G}X)$",
        'BF_mu_R_to_gravitino': r"$\mathrm{BF}(\tilde{\mu}_R\rightarrow \tilde{G}X)$",
        'BF_tau_1_to_gravitino': r"$\mathrm{BF}(\tilde{\tau}_1\rightarrow \tilde{G}X)$",
        'BF_tau_2_to_gravitino': r"$\mathrm{BF}(\tilde{\tau}_2\rightarrow \tilde{G}X)$",
        'BF_nu_e_L_to_gravitino': r"$\mathrm{BF}(\tilde{\nu}_{e L}\rightarrow \tilde{G}X)$",
        'BF_nu_mu_L_to_gravitino': r"$\mathrm{BF}(\tilde{\nu}_{\mu L}\rightarrow \tilde{G}X)$",
        'BF_nu_tau_L_to_gravitino': r"$\mathrm{BF}(\tilde{\nu}_{\tau L}\rightarrow \tilde{G}X)$",
        'BF_gl_to_gravitino': r"$\mathrm{BF}(\tilde{g}\rightarrow \tilde{G}X)$",
        'chi_10_Bino_frac': r"$\tilde{\chi}_1^0$ Bino fraction",
        'chi_10_Wino_frac': r"$\tilde{\chi}_1^0$ Wino fraction",
        'chi_10_Higgsino_frac': r"$\tilde{\chi}_1^0$ Higgsino fraction",
        
    }
    return nicedict[string] if string in nicedict else string

def bottom_offset(self, bboxes, bboxes2):
    """Function for correcting offset of exponent label on x-axis."""
    pad = plt.rcParams["xtick.major.size"] + plt.rcParams["xtick.major.pad"]
    bottom = self.axes.bbox.ymin
    self.offsetText.set(va="top", ha="left") 
    oy = bottom - pad * self.figure.dpi / 72.0
    # self.offsetText.set_position((1, oy))
    self.offsetText.set_position((1+0.01, oy))

def top_offset(self, bboxes, bboxes2):
    """Function for correcting offset of exponent label on y-axis."""
    pad = plt.rcParams["xtick.major.size"] + plt.rcParams["xtick.major.pad"]
    top = self.axes.bbox.ymax
    self.offsetText.set(va="top", ha="left") 
    oy = top + pad * self.figure.dpi / 72.0
    # self.offsetText.set_position((1, oy))
    self.offsetText.set_position((-0.1, oy*1.03))
    
def saferatio(numlist: list, denomlist: list) -> tuple[list, list]:
    """Function for calculate safe ratio numlist/denomlist and the corresponding Poission uncertianty, replacing infinities in the ratio by -1. Returns (ratio, ratioerr)."""
    ratio = [denomlist[i]/numlist[i] if denomlist[i] != 0 else -1. for i in range(len(numlist))]
    # Assume Poissionian errors on both numlist and denomlist; set unc. to 0 for invalid ratio values:
    ratioerr = [ratio[i]*np.sqrt( 1./numlist[i] + 1./denomlist[i] ) if denomlist[i] != 0 else 0 for i in range(len(numlist))]
    
    return ratio, ratioerr
        
def savefile(fig: matplotlib.figure.Figure, dirn: str, filen: str) -> None:
    """Make dirn if it does not exist already and save fig into filen in dirn."""
    # Set dirn to default if None:
    dirn = 'plots' if dirn == None else dirn
    # Make dir and parents if they don't exist already:
    Path(dirn).mkdir(parents=True, exist_ok=True)
    
    # Save file and close plot:
    filepath = f'{dirn}/{filen}'
    # print(f"Saving plot: {filepath}")
    savestr = f"Saving plot: {filepath}\n"
    fig.savefig(filepath)
    plt.close(fig)
    
    return savestr
    
def frac_excl(z: pandas.core.series.Series) -> float:
    """Aggregation function for calculating fraction of excluded models."""
    return len(z[ z.abs() < 0.05 ])/len(z)

def get_simplified_limit(x: str, y: str, z: pandas.core.series.Series) -> pandas.core.frame.DataFrame:
    """Checks if simplified limit exists for z-option in x-y plane and returns df with limit."""
    from pkg_resources import resource_filename
    import os
    
    try:
      CLssuffix = "Exp" if "Exp" in z.name else "Obs"
    except:
      CLssuffix = "Obs"
    
    csv_dir = resource_filename('niceplot', f'contours/')
    matching_files = [filen for filen in os.listdir(csv_dir) if (CLssuffix in filen and f"_{x}_" in filen and f"_{y}_" in filen)]

    if len(matching_files) > 1:
        raise ValueError("More matches for csv files found than expected!")
    elif len(matching_files) == 0:
        return None
    else:
        return pandas.read_csv(os.path.join(csv_dir, matching_files[0]))