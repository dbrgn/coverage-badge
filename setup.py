from setuptools import setup

readme = open('README.rst').read()

setup(name='coverage-badge',
      version='1.0.1',
      description='Generate coverage badges for Coverage.py.',
      author='Danilo Bargen',
      author_email='mail@dbrgn.ch',
      url='https://github.com/dbrgn/coverage-badge',
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
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Testing',
      ],
)
