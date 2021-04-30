import hou
import re

def get_duplicate_mats(selected_nodes):
	duplicates = []
	if len(selected_nodes) > 0:
		for n in selected_nodes:
			if "shader" in n.type().name() or "material" in n.type().name():
				if re.search("[0-9]$", n.name()):
					duplicates.append(n)
			else:
				print(n.name() + " is not a shader!")
	else:
		print("No nodes selected!")

	return duplicates

def remove_duplicate_mats(duplicates):
	num_duplicates = len(duplicates)
	if num_duplicates > 0:
		if hou.ui.displayConfirmation(str(num_duplicates) + " duplicates found.\nProceed deletion?"):
			for d in duplicates:
				d.destroy()
		else:
			print("Deletion cancelled!")
	else:
		print("No duplicates found!") 

def purge_fbx_subnets(selected_nodes):
	fbx_subnets = []
	shaders = []

	if len(selected_nodes) > 0:		
		for n in selected_nodes:
			if n.type().name() == "subnet" and "fbx" in n.name():
				fbx_subnets.append(n)

	if len(fbx_subnets) > 0:
		for n in fbx_subnets:
			to_destroy = []
			matnets = []
			children = n.children()			
			for c in children:				
				if c.type().name() == "matnet":
					matnets.append(c)
				else:
					to_destroy.append(c)

			num_to_destroy = len(to_destroy)
			if num_to_destroy > 0:
				if hou.ui.displayConfirmation(str(num_to_destroy) + " nodes found to destroy inside " + n.name() + "'\nProceed deletion?",
					title=n.name()):
					for d in to_destroy:
						d.destroy()
					print(str(num_to_destroy) + " nodes destroyed inside " + n.name())
				else:
					print("Deletion cancelled")
			else:
				print("No nodes for deletion found!")

			num_matnets = len(matnets)
			if num_matnets > 0:
				if hou.ui.displayConfirmation("Do you want to check shaders for duplicates?",
					title=n.name()):
					for m in matnets:
						for shader in m.children():
							shaders.append(shader)
	else:
		print("No FBX Subnets selected!")

	return shaders