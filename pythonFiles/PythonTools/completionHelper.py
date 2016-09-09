import jedi
def _get_definition_type(definition):
    basic_types = {
        'module': 'import',
        'instance': 'variable',
        'statement': 'value',
        'param': 'variable',
    }
    is_built_in = definition.in_builtin_module
    if definition.type not in ['import', 'keyword'] and is_built_in():
        return 'builtin'
    if definition.type in ['statement'] and definition.name.isupper():
        return 'constant'
    return basic_types.get(definition.type, definition.type)
__COMPLETIONS__ = ''
for completion in jedi.Interpreter('$text', [locals()]).completions():
    __COMPLETIONS__ = __COMPLETIONS__ + "{'text':'" + completion.name + "', 'type':'" + _get_definition_type(completion) + "'},"