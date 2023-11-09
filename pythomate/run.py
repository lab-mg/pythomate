from pywinauto.application import Application

def run_flow(flow):
	power_automate_exe_path = 'C:/Program Files (x86)/Power Automate Desktop/PAD.Console.Host.exe'
	app = Application(backend="uia").start(power_automate_exe_path).connect(
																			title='Power Automate',
																			timeout=100,
																			)
	dlg_spec = app.PowerAutomate
	
	# Clica linha do fluxo
	flow_line = dlg_spec.child_window(
									  title=flow, 
									  control_type='DataItem',
									  ).wrapper_object()
	flow_line.click_input()
	# Clica na execução do fluxo	
	flow_button = dlg_spec.child_window(
										title="Executar", 
										auto_id="StartFlowButton", 
										control_type="Button"
										).wrapper_object()
	flow_button.click_input()


	ok_button = dlg_spec.child_window(
									  title="OK",
									  auto_id="Button",
									  control_type="Button"
									  )
	
	ok_button.click_input()