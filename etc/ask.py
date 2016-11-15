CONFIG = {
    'mode': 'django',
    'environment': {
        'PYTHONPATH': '/usr/bin/python',
    },
    'working_dir': '/home/leonid/web/ask',
    'user': 'www-data',
    'group': 'www-data',
    'args': (
        '--bind=0.0.0.0:8000',
        '--workers=4',
        '--timeout=60',
        'ask.wsgi:application',
    ),
}
