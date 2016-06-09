import click, json, jsonschema, sys, functools

@click.command()
@click.argument('target', nargs=1, type=click.File('r'))
@click.argument('path', nargs=-1)
@click.option('-s', '--schema', type=click.File('r'), default=None,
              help='a file containing a JSON schema to validate the target '
                    'against.')
def parse_json(target, schema, path):
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
        click.echo(functools.reduce(
            json_get_item,
            path, target_json))
    else:
        click.echo(target_json)

def json_get_item(json, item):
    if isinstance(json, dict):
        return json.__getitem__(item)
    elif isinstance(json, list):
        return json.__getitem__(int(item))
