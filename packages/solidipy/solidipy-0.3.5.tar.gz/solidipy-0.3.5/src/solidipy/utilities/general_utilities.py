# /utilities/general_utilities.py

""" General utilities module. """

# import inspect
# import typing
#
#
# def enforce_typing(func):
# 	"""
# 	Decorator for enforcing type-checking on the arguments of a function.
#
# 	Arguments supplied to parameters without a specified typing will not be checked.
# 	:return: Actual decorator that performs type-checking.
# 	"""
#
# 	def wrapper(*args, **kwargs):
# 		"""
# 		Wrapper function that performs type-checking on the arguments of a function.
# 		"""
#
# 		parameters = inspect.signature(func).parameters
# 		print("\n", parameters, "<==parameters==::\n")
# 		annotations = typing.get_type_hints(func)
#
# 		for name, value in kwargs.items():
# 			if name in annotations:
# 				type_hint = annotations[name]
# 				if isinstance(type_hint, type_hint.__args__):
# 					valid_types = typing.get_args(type_hint)
# 					if not any(isinstance(value, t) for t in valid_types):
# 						raise TypeError(
# 							f"Expected one of the types {valid_types} for argument '{name}', "
# 							f"but received type '{type(value)}'"
# 						)
# 				elif not isinstance(value, type_hint):
# 					raise TypeError(
# 						f"Expected type '{type_hint}' for argument '{name}', "
# 						f"but received type '{type(value)}'"
# 					)
#
# 		return func(*args, **kwargs)
#
# 	return wrapper
