import numpy as np
from xraydb.xray import xray_edge, xray_edges

def get_e0(atsym:str, edge:str)->float:
    e0_calc = xray_edge(atsym, edge, energy_only=True)
    return e0_calc

def get_edges(atsym:str):
    edges = xray_edges(atsym)
    edgelist = list(edges.keys())
    return edgelist