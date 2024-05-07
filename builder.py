import primitif.basic as basic
import tools.utility as utility
import tools.objectProperty as objectProperty
import tools.modifier as modifier
import elements.hysteria as hysteria
from importlib import reload

reload(basic)
reload(utility)
reload(objectProperty)
reload(modifier)
reload(hysteria)

utility.clear_scene()

hysteria = hysteria.Hysteria("hysteria", (0, 0, 100))