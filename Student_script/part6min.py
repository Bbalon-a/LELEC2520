import pandapower as pp 
from pandapower.control.controller.trafo.ContinuousTapControl import ContinuousTapControl
import pandapower.topology as top
import pandapower.plotting as plot
from pandapower.plotting.plotly import pf_res_plotly
from pandapower.plotting.plotly import simple_plotly
import pandapower.control as ct
net = pp.create_empty_network(f_hz=50, sn_mva=100)
    
vmin = 0.9
vmax = 1.1
load_max = 100.

    
# list of Buses
M1 = pp.create_bus(net, vn_kv=20.0, name="M1", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (1.5,4))
M2 = pp.create_bus(net, vn_kv=20.0, name="M2", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (3,4))
M3 = pp.create_bus(net, vn_kv=20.0, name="M3", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (0,0))
M4 = pp.create_bus(net, vn_kv=20.0, name="M4", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (4,0))
M5 = pp.create_bus(net, vn_kv=20.0, name="M5", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (4.5,-3))
M6 = pp.create_bus(net, vn_kv=20.0, name="M6", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (1,-5))
N11 = pp.create_bus(net, vn_kv=380.0, name="N11", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (0,-4))
N8 = pp.create_bus(net, vn_kv=380.0, name="N8", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (0.5,-3))
N9 = pp.create_bus(net, vn_kv=380.0, name="N9", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (1,-3))
N10 = pp.create_bus(net, vn_kv=380.0, name="N10", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (1,-4))
N13 = pp.create_bus(net, vn_kv=380.0, name="N13", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (5,-4))
N104 = pp.create_bus(net, vn_kv=150.0, name="N104", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (2,-2))
N203 = pp.create_bus(net, vn_kv=15.0, name="N203", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (2,-3))
N206 = pp.create_bus(net, vn_kv=15.0, name="N206", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (6,0))
N102 = pp.create_bus(net, vn_kv=150.0, name="N102", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (2,1))
N202 = pp.create_bus(net, vn_kv=15.0, name="N202", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (2,0))
N105 = pp.create_bus(net, vn_kv=150.0, name="N105", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (5,-2))
N205 = pp.create_bus(net, vn_kv=15.0, name="N205", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (5.5,-3))
N101 = pp.create_bus(net, vn_kv=150.0, name="N101", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (0.5,1))
N201 = pp.create_bus(net, vn_kv=15.0, name="N201", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (1,0))
N107 = pp.create_bus(net, vn_kv=150.0, name="N107", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (8,1))
N207 = pp.create_bus(net, vn_kv=15.0, name="N207", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (8,0))
N204 = pp.create_bus(net, vn_kv=15.0, name="N204", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (5,0))
N12 = pp.create_bus(net, vn_kv=380.0, name="N12", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (0,-3))
N6 = pp.create_bus(net, vn_kv=380.0, name="N6", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (1.5,-1))
N4 = pp.create_bus(net, vn_kv=380.0, name="N4", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (2.5,2))
N7 = pp.create_bus(net, vn_kv=380.0, name="N7", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (4.5,-1))
N1 = pp.create_bus(net, vn_kv=380.0, name="N1", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (2.5,3))
N2 = pp.create_bus(net, vn_kv=380.0, name="N2", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (8,2))
N3 = pp.create_bus(net, vn_kv=380.0, name="N3", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (0.5,2))
N5 = pp.create_bus(net, vn_kv=380.0, name="N5", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (6,2))
N103 = pp.create_bus(net, vn_kv=150.0, name="N103", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (4.5,1))
N106 = pp.create_bus(net, vn_kv=150.0, name="N106", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (6,1))
N14 = pp.create_bus(net, vn_kv=380.0, name="N14", in_service=True, max_vm_pu=vmax, min_vm_pu = vmin, controllable = True, geodata = (6,-4))


# list of Loads:
LOAD_M1 = pp.create_load(net, bus=M1, p_mw=50.0, q_mvar=40.0, name="M1", in_service=True, max_p_mw=50., min_p_mw=50.0, max_q_mvar=40., min_q_mvar=40., controllable = True)
LOAD_M2 = pp.create_load(net, bus=M2, p_mw=50.0, q_mvar=40.0, name="M2", in_service=True, max_p_mw=50.0, min_p_mw=50.0, max_q_mvar=40., min_q_mvar=40., controllable = True)
LOAD_N11 = pp.create_load(net, bus=N11, p_mw=100.0, q_mvar=30.0, name="N11", in_service=True, max_p_mw=100., min_p_mw=100., max_q_mvar=30., min_q_mvar=30., controllable = True)
LOAD_N8 = pp.create_load(net, bus=N8, p_mw=230.0, q_mvar=75.0, name="N8", in_service=True, max_p_mw=230., min_p_mw=230., max_q_mvar=75., min_q_mvar=75., controllable = True)
LOAD_N9 = pp.create_load(net, bus=N9, p_mw=220.0, q_mvar=70.0, name="N9", in_service=True, max_p_mw=220., min_p_mw=220., max_q_mvar=70., min_q_mvar=70., controllable = True)
LOAD_N13 = pp.create_load(net, bus=N13, p_mw=300.0, q_mvar=75.0, name="N13", in_service=True, max_p_mw=300., min_p_mw=300., max_q_mvar=75., min_q_mvar=75., controllable = True)
LOAD_N203 = pp.create_load(net, bus=N203, p_mw=360.0, q_mvar=180.0, name="N203", in_service=True, max_p_mw=540., min_p_mw=360., max_q_mvar=180., min_q_mvar=180., controllable = True)
LOAD_N206 = pp.create_load(net, bus=N206, p_mw=360.0, q_mvar=180.0, name="N206", in_service=True, max_p_mw=360., min_p_mw=360., max_q_mvar=180., min_q_mvar=180., controllable = True)
LOAD_N202 = pp.create_load(net, bus=N202, p_mw=360.0, q_mvar=180.0, name="N202", in_service=True, max_p_mw=360., min_p_mw=360., max_q_mvar=180., min_q_mvar=180., controllable = True)
LOAD_N205 = pp.create_load(net, bus=N205, p_mw=360.0, q_mvar=180.0, name="N205", in_service=True, max_p_mw=360., min_p_mw=360., max_q_mvar=180., min_q_mvar=180., controllable = True)
LOAD_N201 = pp.create_load(net, bus=N201, p_mw=360.0, q_mvar=180.0, name="N201", in_service=True, max_p_mw=360., min_p_mw=360., max_q_mvar=180., min_q_mvar=180., controllable = True)
LOAD_N207 = pp.create_load(net, bus=N207, p_mw=360.0, q_mvar=180.0, name="N207", in_service=True, max_p_mw=360., min_p_mw=360., max_q_mvar=180., min_q_mvar=180., controllable = True)
LOAD_N204 = pp.create_load(net, bus=N204, p_mw=360.0, q_mvar=180.0, name="N204", in_service=True, max_p_mw=360., min_p_mw=360., max_q_mvar=180., min_q_mvar=180., controllable = True)




# List of Shunts:
pp.create_shunt(net, bus=N104, q_mvar=-75.0, in_service=True)
pp.create_shunt(net, bus=N203, q_mvar=-45.0, in_service=True)
pp.create_shunt(net, bus=N206, q_mvar=-45.0, in_service=True)
pp.create_shunt(net, bus=N102, q_mvar=-75.0, in_service=True)
pp.create_shunt(net, bus=N202, q_mvar=-45.0, in_service=True)
pp.create_shunt(net, bus=N105, q_mvar=-75.0, in_service=True)
pp.create_shunt(net, bus=N205, q_mvar=-45.0, in_service=True)
pp.create_shunt(net, bus=N101, q_mvar=-75.0, in_service=True)
pp.create_shunt(net, bus=N201, q_mvar=-45.0, in_service=True)
pp.create_shunt(net, bus=N107, q_mvar=-75.0, in_service=True)
pp.create_shunt(net, bus=N207, q_mvar=-45.0, in_service=True)
pp.create_shunt(net, bus=N204, q_mvar=-45.0, in_service=True)


# list of Lines
pp.create_line_from_parameters(net, from_bus= N11, to_bus= N10, name="'N11N10", length_km=1, r_ohm_per_km=1.141, x_ohm_per_km=12.086, max_i_ka=2.157467, c_nf_per_km=434.703079165756, in_service=True,max_loading_percent = load_max , controllable = True, geodata = [(0,-4),(1,-4)])
pp.create_line_from_parameters(net, from_bus= N6, to_bus= N8, name="'N6N8", length_km=1, r_ohm_per_km=1.444, x_ohm_per_km=14.44, max_i_ka=2.157467, c_nf_per_km=537.867313277922, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(1.5,-1),(0.5,-3)])
pp.create_line_from_parameters(net, from_bus= N6, to_bus= N9, name="'N6N9", length_km=1, r_ohm_per_km=1.357, x_ohm_per_km=14.368, max_i_ka=2.157467, c_nf_per_km=538.306580920856, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(1.5,-1),(1,-3)])
pp.create_line_from_parameters(net, from_bus= N6, to_bus= N4, name="'N6N4", length_km=1, r_ohm_per_km=1.213, x_ohm_per_km=10.224, max_i_ka=2.157467, c_nf_per_km=380.915074598419, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(1.5,-1),(1.5,1.5),(2.5,2)])
pp.create_line_from_parameters(net, from_bus= N6, to_bus= N7, name="'N6N7", length_km=1, r_ohm_per_km=1.213, x_ohm_per_km=10.224, max_i_ka=2.157467, c_nf_per_km=380.915074598419, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(1.5,-1),(4.5,-1)])
pp.create_line_from_parameters(net, from_bus= N8, to_bus= N10, name="'N8N10", length_km=1, r_ohm_per_km=2.166, x_ohm_per_km=23.104, max_i_ka=2.157467, c_nf_per_km=881.718384729100, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(0.5,-3),(1,-4)])
pp.create_line_from_parameters(net, from_bus= N9, to_bus= N10, name="'N9N10", length_km=1, r_ohm_per_km=2.166, x_ohm_per_km=23.104, max_i_ka=2.157467, c_nf_per_km=881.718384729100, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(1,-3),(1,-4)])
pp.create_line_from_parameters(net, from_bus= N1, to_bus= N4, name="'N1N41", length_km=1, r_ohm_per_km=0.765, x_ohm_per_km=6.7, max_i_ka=2.051113, c_nf_per_km=249.975119817855, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(2.5,3),(2.5,2.5),(2.5,2)])
pp.create_line_from_parameters(net, from_bus= N1, to_bus= N4, name="'N1N42", length_km=1, r_ohm_per_km=0.708, x_ohm_per_km=7.538, max_i_ka=2.051113, c_nf_per_km=282.601883151693, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(2.5,3),(2.25,2.5),(2.5,2)])
pp.create_line_from_parameters(net, from_bus= N1, to_bus= N4, name="'N1N43", length_km=1, r_ohm_per_km=0.708, x_ohm_per_km=7.538, max_i_ka=2.051113, c_nf_per_km=282.601883151693, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(2.5,3),(2.75,2.5),(2.5,2)])
pp.create_line_from_parameters(net, from_bus= N1, to_bus= N2, name="'N1N2", length_km=1, r_ohm_per_km=0.202, x_ohm_per_km=2.094, max_i_ka=2.157467, c_nf_per_km=71.422372261919, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(2.5,3),(8,2)])
pp.create_line_from_parameters(net, from_bus= N10, to_bus= N13, name="'N10N13", length_km=1, r_ohm_per_km=1.256, x_ohm_per_km=13.992, max_i_ka=2.157467, c_nf_per_km=510.091592609524, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(1,-4),(5,-4)])
pp.create_line_from_parameters(net, from_bus= N4, to_bus= N3, name="'N4N3", length_km=1, r_ohm_per_km=1.054, x_ohm_per_km=11.148, max_i_ka=2.157467, c_nf_per_km=417.947246757041, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(2.5,2),(0.5,2)])
pp.create_line_from_parameters(net, from_bus= N5, to_bus= N4, name="'N5N41", length_km=1, r_ohm_per_km=0.664, x_ohm_per_km=7.076, max_i_ka=2.157467, c_nf_per_km=240.273034486973, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(6,2),(4.25,2.25),(2.5,2)])
pp.create_line_from_parameters(net, from_bus= N5, to_bus= N4, name="'N5N42", length_km=1, r_ohm_per_km=0.664, x_ohm_per_km=7.076, max_i_ka=2.157467, c_nf_per_km=240.273034486973, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(6,2),(4.25,1.75),(2.5,2)])
pp.create_line_from_parameters(net, from_bus= N102, to_bus= N103, name="'N102N103", length_km=1, r_ohm_per_km=0.225, x_ohm_per_km=2.565, max_i_ka=1.347151, c_nf_per_km=56.589131565754, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(2,1),(4.5,1)])
pp.create_line_from_parameters(net, from_bus= N102, to_bus= N101, name="'N102N101", length_km=1, r_ohm_per_km=3.825, x_ohm_per_km=14.218, max_i_ka=1.347151, c_nf_per_km=325.382731854794, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(2,1),(0.5,1)])
pp.create_line_from_parameters(net, from_bus= N106, to_bus= N103, name="'N106N103", length_km=1, r_ohm_per_km=1.237, x_ohm_per_km=5.625, max_i_ka=1.347151, c_nf_per_km=113.178263131509, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(6,1),(4.5,1)])
pp.create_line_from_parameters(net, from_bus= N106, to_bus= N105, name="'N106N105", length_km=1, r_ohm_per_km=1.8, x_ohm_per_km=9.675, max_i_ka=1.347151, c_nf_per_km=198.058777381278, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(6,1),(5,-2)])
pp.create_line_from_parameters(net, from_bus= N104, to_bus= N105, name="'N104N105", length_km=1, r_ohm_per_km=1.395, x_ohm_per_km=6.75, max_i_ka=1.347151, c_nf_per_km=141.469645815524, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(2,-2),(5,-2)])
pp.create_line_from_parameters(net, from_bus= N104, to_bus= N103, name="'N104N103", length_km=1, r_ohm_per_km=1.395, x_ohm_per_km=6.75, max_i_ka=1.347151, c_nf_per_km=141.469645815524, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(2,-2),(4.5,1)])
pp.create_line_from_parameters(net, from_bus= N13, to_bus= N14, name="'N13N14", length_km=1, r_ohm_per_km=3.148, x_ohm_per_km=33.342, max_i_ka=2.051113, c_nf_per_km=636.180504724648, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(5,-4),(6,-4)])
pp.create_line_from_parameters(net, from_bus= N11, to_bus= N12, name="'N11N12", length_km=1, r_ohm_per_km=1.819, x_ohm_per_km=19.22, max_i_ka=2.051113, c_nf_per_km=597.384895796567, in_service=True,max_loading_percent = load_max, controllable = True, geodata = [(0,-4),(0,-3)])

# list of Transformers:
pp.create_transformer_from_parameters(net, hv_bus=N2, lv_bus=N107, sn_mva=550.0, name='N2N107', shift_degree=0.0, vn_hv_kv=380.0, vn_lv_kv=150.0, vkr_percent=0.312, vk_percent=22.72114224681497, pfe_kw=0, i0_percent=0.0, tap_min=8, tap_max=8, tap_step_percent=1, tap_pos=8,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N3, lv_bus=N101, sn_mva=550.0, name='N3N101', shift_degree=0.0, vn_hv_kv=380.0, vn_lv_kv=150.0, vkr_percent=0.26, vk_percent=22.621494203522456, pfe_kw=0, i0_percent=0.0, tap_min=3, tap_max=3, tap_step_percent=1, tap_pos=3,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N7, lv_bus=N105, sn_mva=550.0, name='N7N105', shift_degree=0.0, vn_hv_kv=380.0, vn_lv_kv=150.0, vkr_percent=0.26, vk_percent=22.621494203522456, pfe_kw=0, i0_percent=0.0, tap_min=7, tap_max=7, tap_step_percent=1, tap_pos=7,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N4, lv_bus=N102, sn_mva=550.0, name='N4N102', shift_degree=0.0, vn_hv_kv=380.0, vn_lv_kv=150.0, vkr_percent=0.416, vk_percent=24.542525888750735, pfe_kw=0, i0_percent=0.0, tap_min=14, tap_max=14, tap_step_percent=1, tap_pos=14,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N5, lv_bus=N106, sn_mva=550.0, name='N5N106', shift_degree=0.0, vn_hv_kv=380.0, vn_lv_kv=150.0, vkr_percent=0.151, vk_percent=11.596983099065032, pfe_kw=0, i0_percent=0.0, tap_min=6, tap_max=6, tap_step_percent=1, tap_pos=6,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N6, lv_bus=N104, sn_mva=550.0, name='N6N104', shift_degree=0.0, vn_hv_kv=380.0, vn_lv_kv=150.0, vkr_percent=0.146, vk_percent=11.440931605424446, pfe_kw=0, i0_percent=0.0, tap_min=2, tap_max=2, tap_step_percent=1, tap_pos=2,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N1, lv_bus=M1, sn_mva=1000.0, name='M1N1', shift_degree=0.0, vn_hv_kv=380.0, vn_lv_kv=20.0, vkr_percent=0.23, vk_percent=10.702471677140752, pfe_kw=0, i0_percent=0.0, tap_min=8, tap_max=8, tap_step_percent=1, tap_pos=8,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N1, lv_bus=M2, sn_mva=1000.0, name='M2N1', shift_degree=0.0, vn_hv_kv=380.0, vn_lv_kv=20.0, vkr_percent=0.117, vk_percent=9.854694566550501, pfe_kw=0, i0_percent=0.0, tap_min=6, tap_max=6, tap_step_percent=1, tap_pos=6,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N10, lv_bus=M6, sn_mva=1000.0, name='M6N10', shift_degree=0.0, vn_hv_kv=380.0, vn_lv_kv=20.0, vkr_percent=0.25, vk_percent=13.002403623945844, pfe_kw=0, i0_percent=0.0, tap_min=10, tap_max=10, tap_step_percent=1, tap_pos=10,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N105, lv_bus=M5, sn_mva=500.0, name='M5N105', shift_degree=0.0, vn_hv_kv=150.0, vn_lv_kv=20.0, vkr_percent=0.25, vk_percent=13.002403623945844, pfe_kw=0, i0_percent=0.0, tap_min=10, tap_max=10, tap_step_percent=1, tap_pos=10,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N101, lv_bus=M3, sn_mva=500.0, name='M3N101', shift_degree=0.0, vn_hv_kv=150.0, vn_lv_kv=20.0, vkr_percent=0.25, vk_percent=13.002403623945844, pfe_kw=0, i0_percent=0.0, tap_min=10, tap_max=10, tap_step_percent=1, tap_pos=10,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N103, lv_bus=M4, sn_mva=350.0, name='M4N103', shift_degree=0.0, vn_hv_kv=150.0, vn_lv_kv=20.0, vkr_percent=0.25, vk_percent=13.002403623945844, pfe_kw=0, i0_percent=0.0, tap_min=10, tap_max=10, tap_step_percent=1, tap_pos=10,tap_neutral=0, tap_side="hv", in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N101, lv_bus=N201, sn_mva=500.0, name="'N201N101'", vn_hv_kv=150.0, vn_lv_kv=15.0, vkr_percent=0.277, vk_percent=11.53832544176147, pfe_kw=0, i0_percent=0.0, tap_pos=0, tap_neutral=0, tap_step_percent=1.0, tap_side="lv", tap_min=-4, tap_max=20, in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N102, lv_bus=N202, sn_mva=500.0, name="'N202N102'", vn_hv_kv=150.0, vn_lv_kv=15.0, vkr_percent=0.271, vk_percent=11.298250572544406, pfe_kw=0, i0_percent=0.0, tap_pos=0, tap_neutral=0, tap_step_percent=1.0, tap_side="lv", tap_min=-4, tap_max=20, in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N104, lv_bus=N203, sn_mva=500.0, name="'N203N104'", vn_hv_kv=150.0, vn_lv_kv=15.0, vkr_percent=0.271, vk_percent=11.298250572544406, pfe_kw=0, i0_percent=0.0, tap_pos=0, tap_neutral=0, tap_step_percent=1.0, tap_side="lv", tap_min=-4, tap_max=20, in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N103, lv_bus=N204, sn_mva=500.0, name="'N204N103'", vn_hv_kv=150.0, vn_lv_kv=15.0, vkr_percent=0.277, vk_percent=11.53832544176147, pfe_kw=0, i0_percent=0.0, tap_pos=0, tap_neutral=0, tap_step_percent=1.0, tap_side="lv", tap_min=-4, tap_max=20, in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N105, lv_bus=N205, sn_mva=500.0, name="'N205N105'", vn_hv_kv=150.0, vn_lv_kv=15.0, vkr_percent=0.283, vk_percent=11.785398296196867, pfe_kw=0, i0_percent=0.0, tap_pos=0, tap_neutral=0, tap_step_percent=1.0, tap_side="lv", tap_min=-4, tap_max=20, in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N106, lv_bus=N206, sn_mva=500.0, name="'N206N106'", vn_hv_kv=150.0, vn_lv_kv=15.0, vkr_percent=0.277, vk_percent=11.53832544176147, pfe_kw=0, i0_percent=0.0, tap_pos=0, tap_neutral=0, tap_step_percent=1.0, tap_side="lv", tap_min=-4, tap_max=20, in_service=True,max_loading_percent = load_max)
pp.create_transformer_from_parameters(net, hv_bus=N107, lv_bus=N207, sn_mva=500.0, name="'N207N107'", vn_hv_kv=150.0, vn_lv_kv=15.0, vkr_percent=0.277, vk_percent=11.53832544176147, pfe_kw=0, i0_percent=0.0, tap_pos=0, tap_neutral=0, tap_step_percent=1.0, tap_side="lv", tap_min=-4, tap_max=20, in_service=True,max_loading_percent = load_max)

# list of Generators:
G1 = pp.create_gen(net, p_mw=700.0, max_q_mvar=638.58, min_q_mvar=-250.0, sn_mva=1000.0, bus=M1, vm_pu=0.99958, name="M1", slack=False, in_service=True, min_p_mw=0., max_p_mw=850., controllable = True)
G2 = pp.create_gen(net, p_mw=600.0, max_q_mvar=696.53, min_q_mvar=-250.0, sn_mva=1000.0, bus=M2, vm_pu=0.99958, name="M2", slack=False, in_service=True, min_p_mw=0., max_p_mw=850., controllable = True)
G3=pp.create_gen(net, p_mw=375.0, max_q_mvar=220.83, min_q_mvar=-50.0, sn_mva=450.00, bus=M3, vm_pu=0.99000, name="M3", slack=False, in_service=True, min_p_mw=0., max_p_mw=405., controllable = True)
G4=pp.create_gen(net, p_mw=250.0, max_q_mvar=143.76, min_q_mvar=-50.0, sn_mva=300.00, bus=M4, vm_pu=0.97580, name="M4", slack=False, in_service=True, min_p_mw=0., max_p_mw=270., controllable = True)
G5=pp.create_gen(net, p_mw=375.0, max_q_mvar=220.97, min_q_mvar=-50.0, sn_mva=450.00, bus=M5, vm_pu=0.99040, name="M5", slack=False, in_service=True, min_p_mw=0., max_p_mw=405., controllable = True)
G6=pp.create_gen(net, p_mw=804.0, max_q_mvar=572.16, min_q_mvar=-250.0, sn_mva=1000.0, bus=M6, vm_pu=1.0100, name="M6", slack=True, in_service=True, min_p_mw=0., max_p_mw=850., controllable = True)
G7=pp.create_gen(net, p_mw=255.0, max_q_mvar=9999.0, min_q_mvar=-999.0, sn_mva=1000.0, bus=N12, vm_pu=1.0994, name="N12", slack=False, in_service=True, min_p_mw=0., max_p_mw=5000., controllable = True)
G8=pp.create_gen(net, p_mw=174.0, max_q_mvar=9999.0, min_q_mvar=-999.0, sn_mva=1000.0, bus=N14, vm_pu=1.0929, name="N14", slack=False, in_service=True, min_p_mw=0., max_p_mw=2450., controllable = True)

# Controllers :
ct.controller.trafo.DiscreteTapControl.DiscreteTapControl(net,12, 1.01,1.021, order = 0)
ct.controller.trafo.DiscreteTapControl.DiscreteTapControl(net,13, 1.01,1.021, order = 0)
ct.controller.trafo.DiscreteTapControl.DiscreteTapControl(net,14, 1.01,1.021, order = 0)
ct.controller.trafo.DiscreteTapControl.DiscreteTapControl(net,15, 1.01,1.021, order = 0)
ct.controller.trafo.DiscreteTapControl.DiscreteTapControl(net,16, 1.01,1.021, order = 0)
ct.controller.trafo.DiscreteTapControl.DiscreteTapControl(net,17, 1.01,1.021, order = 0)
ct.controller.trafo.DiscreteTapControl.DiscreteTapControl(net,18, 1.01,1.021, order = 0)


"""
Create the constraints here
+
Launch the right routine too

"""