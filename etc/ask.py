CONFIG = {
    'mode': 'wsgi',
    'environment': {
        'PYTHONPATH': '/usr/bin/python',
    },
    'working_dir': '/home/box/web/ask',
    'user': 'www-data',
    'group': 'www-data',
    'args': (
        '--bind=0.0.0.0:8080',
        '--workers=4',
        '--timeout=60',
        'ask.wsgi:application',
    ),
}
