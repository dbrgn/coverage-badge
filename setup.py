from setuptools import setup

readme = open('README.rst').read()

setup(name='coverage-badge',
      version='1.0.2',
      description='Generate coverage badges for Coverage.py.',
      author='Danilo Bargen',
      author_email='mail@dbrgn.ch',
      url='https://github.com/dbrgn/coverage-badge',
      install_requires=['coverage==5.*'],
      packages=['coverage_badge'],
      zip_safe=True,
      include_package_data=True,
      license='MIT',
      keywords='coverage badge shield',
      long_description=readme,
      entry_points={
          'console_scripts': [
              'coverage-badge = coverage_badge.__main__:main',
          ]
      },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Testing',
      ],
)
