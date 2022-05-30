import nuke


class Toggler():

	def __init__(self):
		self.name = 'Toggler GUI'
		self.link_selected_str = 'node.link_nodes(node.get_selected_nodes())'
		self.link_classes_str = 'node.link_nodes(node.get_class_nodes())'
		self.remove_selected_str = 'node.remove_nodes(node.get_selected_nodes())'
		self.remove_classes_str = 'node.remove_nodes(node.get_class_nodes())'
		self.create_node()

	def create_node(self):
		'''
		Builds group nuke node
		'''
		# Create node
		toggler_node = nuke.nodes.Group(tile_color='0x20d34ff')

		# Create knobs
			# Links
		link_selected = nuke.PyScript_Knob('link_selected', 'Link Selected', self.link_selected_str)
		link_classes = nuke.PyScript_Knob('link_classes', 'Link Classes', self.link_classes_str)
		link_classes.setFlag(nuke.STARTLINE)
			# Removal
		remove_selected = nuke.PyScript_Knob('remove_selected', 'Remove Selected', self.remove_selected_str)
		remove_classes = nuke.PyScript_Knob('remove_classes', 'Remove Classes', self.remove_classes_str)
			# Other Knobs
		classes = nuke.String_Knob('classes', 'Classes')
		divider = nuke.Text_Knob('divider', '')

		# Attach knobs to tab
		toggler_node.addKnob(link_selected)
		toggler_node.addKnob(remove_selected)
		toggler_node.addKnob(divider)
		toggler_node.addKnob(classes)
		toggler_node.addKnob(link_classes)
		toggler_node.addKnob(remove_classes)

		# Node Renaming
		toggler_node.knob('User').setName('Toggler')
		toggler_node.setName(self.name)

	def get_selected_nodes(self):
		'''
		Returns a list of nodes based on selection in node graph
		'''
		nodes = nuke.root().selectedNodes()
		return nodes

	def get_class_nodes(self):
		'''
		Returns a list of nodes based on classes input knob
		'''
		this_node = nuke.thisNode()
		classes = this_node['classes'].value().split(',')
		node_list = []

		for node in nuke.allNodes(group=nuke.root()):
			node_class = node.Class()
			for i in classes: 
				if node_class.__contains__(i.title()):
					node_list.append(node)

		return node_list

	def link_nodes(self, nodes):
		node_list = nodes
		for node in node_list:
			if node != nuke.thisNode():
				node['disable'].setExpression(nuke.thisNode().name() + '.disable')

	def remove_nodes(self, nodes):
		node_list = nodes
		for node in node_list:
			if node['disable'].hasExpression():
				node['disable'].clearAnimated()


node = Toggler()









