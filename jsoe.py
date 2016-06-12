import click, json, jsonschema, sys, functools, pprint

@click.command()
@click.argument('target', nargs=1, type=click.File('r'))
@click.argument('path', nargs=-1)
@click.option('-s', '--schema', type=click.File('r'), default=None,
              help='Validate the target against a JSON schema.')
@click.option('--descend/--no-descend', default=True,
              help="If the pathed-to node is an object, print the object's "
                   "contents instead of just its keys; defaults to descending.")
@click.option('--one-line/--multi-line', default=True,
              help='Print every node below the pathed-to node on a separate '
                   'line; defaults to printing them all on a single line.')
def parse_json(target, schema, path, descend, one_line):
    """This script will key and index into a JSON structure passed to it, and
    optionally validate that structure against a JSON schema.
    """
    target_contents = target.read()
    target_json = json.loads(target_contents)

    if schema is not None:
        try:
            jsonschema.validate(target_json, json.loads(schema.read()))
        except jsonschema.ValidationError as e:
            sys.exit(1)

    if len(path) != 0:
        print_object = functools.reduce(
                                    json_get_item,
                                    path, target_json)
    else:
        print_object = target_json

    print_object = switch_descend(print_object, descend)

    if not one_line:
        print_object = pprint.pformat(print_object, width=1, compact=True)

    click.echo(json.dumps(print_object))

def switch_descend(json, descend):
    if isinstance(json, dict):
        elements = lambda j: list(j.keys())
    elif isinstance(json, list):
        elements = lambda j: list(map(lambda x: switch_descend(x, False), j))
    else:
        elements = lambda j: j

    if descend:
        return json
    else:
        return elements(json)

def json_get_item(json, item):
    if isinstance(json, dict):
        return json.__getitem__(item)
    elif isinstance(json, list):
        return json.__getitem__(int(item))
