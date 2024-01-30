import argparse
from cayenne.simulation import Simulation
import sys

def get_args():
    # CO_Oxidation = """
    #         const compartment comp1;
    #         comp1 = 1; # volume of compartment
    #         r1: CO_g + E => CO_s; k1;
    #         r2: CO_s => CO_g + E; k2;
    #         r3: O2_g + 2E => 2O_s; k3;
    #         r4: 2O_s => O2_g + 2E; k4;
    #         r5: CO_s + O_s => CO2_g + 2E; k5;
    #         k1 = 5.78e5;
    #         k2 = 1.65e3;
    #         k3 = 1.62e5;
    #         k4 = 2.33e11;
    #         k5 = 1.71e2
    #         CO_g = 0;
    #         CO_s = 1;
    #         E = 1;
    #         O2_g = 0;
    #         O_s = 1;
    #         CO2_g = 0;
    #         chem_flag = true;
    #     """

    NH3_Decomposition = """
            const compartment comp1;
            comp1 = 1; # volume of compartment
            
            r1: 2H_s => 2E + H2_g; k1;
            r2: 2N_s => 2E + N2_g; k2;
            r3: NH3_g + E => NH3_s; k3;
            r4: NH3_s => NH3_g + E; k4;
            r5: N_s + H_s => NH_s + E; k5;
            r6: NH_s + E => N_s + H_s; k6;
            r7: NH_s + H_s => NH2_s + E; k7;
            r8: NH2_s + E => NH_s + H_s; k8;
            r9: NH2_s + H_s => NH3_s + E; k9;
            r10: NH3_s + E => NH2_s + H_s; k10;
            k1=3.68e5;
            k2=1.41e1;
            k3=3.94e4;
            k4=9e6;
            k5=0.18;
            k6=1.15e10;
            k7=4.45e5;
            k8=4.27e6;
            k9=1.87e6;
            k10=1.05e7;
            H_s = 1;
            E = 1;
            H2_g = 0;
            N_s = 1;
            N2_g = 0;
            NH3_g = 0;
            NH3_s = 1;
            NH_s = 1;
            NH2_s = 1;  
            chem_flag = true;
        """

    sim = Simulation.load_model(NH3_Decomposition, "ModelString")
    parser = argparse.ArgumentParser(description='Parser For Arguments', formatter_class=argparse.ArgumentDefaultsHelpFormatter, allow_abbrev=False)
    parser.add_argument('--exp_name',		type=str,             default="nh3",			help='name of the exp, can be nh3 or co2')
    parser.add_argument('--lattice_size',		type=int,             default=50,			help='Size of the lattice surface')
    parser.add_argument('--sim_round',		type=int,             default=10000000,			help='number of simulations')
    parser.add_argument('--num_samples',		type=int,             default=50,			help='number of samples N')
    parser.add_argument('--end_time',		type=float,             default=0.00011,			help='when to stop the simulation')
    parser.add_argument('--alg1_lambda',		type=float,             default=0.1,			help='algo 1 param')
    parser.add_argument('--alg2_lambda',		type=float,             default=0.1,			help='algo 2 param')
    parser.add_argument('--alg3_lambda',		type=float,             default=1e-3,			help='algo 3 param')
    parser.add_argument('--tau_max',		type=float,             default=1e-8,			help='algo 2 param')
    parser.add_argument('--algo',		type=int,             default=-1,			help='which alg to run')
    parser.add_argument('--path',		type=str,             default='24_1_11/',			help='path to save results')
    
    # use default values if in jupyter enviornment
    if 'ipykernel' in sys.argv[0]:
        args = parser.parse_args([])
    else:
        args = parser.parse_args()
        
    print(args)
    args.sim = sim
    return args
