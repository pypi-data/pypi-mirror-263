from setuptools import find_packages, setup


setup(
    name='msanic',
    version='1.0.5',
    author='DHDONG',
    author_email='zscych@qq.com',
    license='MIT',
    packages=find_packages(),

    description='A web framework who is use sanic + tortoise-orm + redis to quick create http&websocket server',
    long_description='A web framework who is use sanic + tortoise-orm + redis to quick create http&websocket server. '
                     '\nYou can quickly build a new project by command -- sanicGuider',

    install_requires=[
        'sanic >= 22.12.0',
        'redis[hiredis] >= 4.4.0',
        'pyjwt >= 0.2.6',
        'httpx >= 0.23.0',
        'orjson >= 3.9.15',
        'pycryptodome >= 3.16.0',
    ],
    entry_points={
        "console_scripts": [
            "sanicGuider=msanic:mult_creator",
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.9,<3.12',
    keywords=['WebServer', 'Sanic', 'WebSite Develop', 'Web Framework']
)
