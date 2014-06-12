from setuptools import setup


setup(
    name='sphinx-kr-theme',
    description='The third-part package of kennethreitz/kr-sphinx-themes.',
    version='0.1.0.dev',
    maintainer='Jiangge Zhang',
    maintainer_email='tonyseek@gmail.com',
    url='https://github.com/tonyseek/sphinx-kr-theme',
    license='MIT',
    zip_safe=False,
    packages=['sphinx_kr_theme'],
    package_data={
        'sphinx_kr_theme': [
            'kr/theme.conf',
            'kr/*.html',
            'kr/static/*.css',
            'kr/static/*.css_t',
            'kr_small/theme.conf',
            'kr_small/*.html',
            'kr_small/static/*.css_t',
        ],
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
