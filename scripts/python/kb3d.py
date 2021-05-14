import hou
import re

def batch_replace_texture_paths():
	selected_nodes = hou.selectedNodes()

	if len(selected_nodes) > 0:
		# Replace multiline input with dir selections?
		button_idx, values = hou.ui.readMultiInput(
			"Path Replace", ("Old Path", "New Path"), buttons=("OK", "Cancel")
		)
		if button_idx == 0:
			shaders = []
			for n in selected_nodes:
				name = n.type().name()
				if name == "principledshader::2.0":
					shaders.append(n)
				elif name == "materialbuilder":
					for c in n.children():
						child_name = c.type().name()
						if child_name == "principledshader::2.0":
							shaders.append(c)
			# MAKE CHECK FOR FOUND SHADERS!
			for s in shaders:
				textures = []
				types = [
					"basecolor", "ior", "rough", "aniso", "anisodir",
					"metallic", "reflect", "reflecttint", "coat", "coatrough",
					"transparency", "transcolor", "transdist", "dispersion",
					"sss", "sssdist", "ssscolor", "sheen", "sheentint",
					"emitcolor", "opaccolor"
				]

				for t in types:
					useTexture = t + "_useTexture"
					if s.evalParm(useTexture):
						textures.append(t + "_texture")

				if s.evalParm("baseBumpAndNormal_enable"):
					if s.evalParm("baseBumpAndNormal_type") == "bump":
						textures.append("baseBump_bumpTexture")
					elif s.evalParm("baseBumpAndNormal_type") == "normal":
						textures.append("baseNormal_texture")

				for tex in textures:
					oldpath = s.evalParm(tex)
					newpath = re.sub(values[0], values[1], oldpath)
					s.setParms({tex:newpath})

		else:
			print("Path Replace cancelled!")
	else:
		print("No shaders selected!")