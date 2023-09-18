from setuptools import setup

setup(name='my_tools',
      version='0.0.2',
      description='My own short tools',
    #   url='http://github.com/dummy_user/useful',
      author='Vitalii Savenko',
    #   author_email='flyingcircus@example.com',
      license='MIT',
      packages=['my_tools'],
      entry_points={'console_scripts': ['make_file = my_tools.main_create_file_for_exsercises:main']}
)