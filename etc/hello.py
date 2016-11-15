CONFIG = {
    'mode': 'wsgi',
    'environment': {
        'PYTHONPATH': '/usr/bin/python',
    },
    'working_dir': '/home/leonid/web',
    'user': 'www-data',
    'group': 'www-data',
    'args': (
        '--bind=0.0.0.0:8080',
        '--workers=4',
        '--timeout=30',
        'hello',
    ),
}
